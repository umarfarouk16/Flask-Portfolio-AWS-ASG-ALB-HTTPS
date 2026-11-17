#!/bin/bash
# EC2 Launch Template user data — Flask portfolio behind ALB (target group on port 8000).
# Runs as root on first boot of every instance the Auto Scaling Group launches.
set -euxo pipefail
exec > >(tee /var/log/user-data.log) 2>&1

REPO_URL="https://github.com/YOUR_GITHUB_USERNAME/Flask-Portfolio-AWS-ASG-ALB-HTTPS.git"   # <-- change this
APP_USER="ubuntu"
APP_DIR="/home/${APP_USER}/Flask-Portfolio-AWS-ASG-ALB-HTTPS"
PORT=8000

# 1. System packages (python3-venv was the missing piece)
export DEBIAN_FRONTEND=noninteractive
apt-get update -y
apt-get install -y git curl python3 python3-venv python3-pip
PYVER="$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
apt-get install -y "python${PYVER}-venv" || true

# 2. Get the code, owned by the ubuntu user (not root)
rm -rf "$APP_DIR"
sudo -u "$APP_USER" git clone "$REPO_URL" "$APP_DIR"

# 3. Virtual environment + dependencies
cd "$APP_DIR"
sudo -u "$APP_USER" python3 -m venv venv
sudo -u "$APP_USER" venv/bin/python -m pip install --upgrade pip
sudo -u "$APP_USER" venv/bin/python -m pip install -r requirements.txt gunicorn

# 4. Run Gunicorn as a systemd service (survives reboots and crashes)
cat > /etc/systemd/system/portfolio.service <<EOF
[Unit]
Description=Flask Portfolio (Gunicorn)
After=network.target

[Service]
User=${APP_USER}
WorkingDirectory=${APP_DIR}
ExecStart=${APP_DIR}/venv/bin/gunicorn --workers 3 --bind 0.0.0.0:${PORT} app:app
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable --now portfolio

# 5. Confirm it's up (shows in /var/log/user-data.log)
for i in $(seq 1 20); do
  curl -fsS -o /dev/null "http://127.0.0.1:${PORT}/" && { echo "APP OK on port ${PORT}"; exit 0; }
  sleep 2
done
echo "APP FAILED to start"; journalctl -u portfolio -n 50 --no-pager; exit 1