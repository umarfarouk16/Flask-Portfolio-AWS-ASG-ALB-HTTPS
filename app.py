from flask import Flask, render_template_string

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Umar Farouk Muftau | Cloud &amp; DevOps Engineer</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <style>
    :root {
      --bg: #0b1622;
      --surface: #111f2f;
      --surface2: #172336;
      --text: #e6edf3;
      --muted: #7a8fbb;
      --accent: #4F7CAC;
      --accent-hover: #5d89bb;
      --line: #1e2f42;
      --tag-bg: #0f1c2b;
      --radius: 10px;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    html { scroll-behavior: smooth; }

    body {
      font-family: 'Inter', sans-serif;
      background: radial-gradient(ellipse at 50% 0%, #0f2035 0%, var(--bg) 60%);
      background-attachment: fixed;
      color: var(--text);
      line-height: 1.65;
    }

    /* ── NAV ── */
    nav {
      position: sticky;
      top: 0;
      z-index: 100;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 14px 32px;
      background: rgba(11, 22, 34, 0.88);
      backdrop-filter: blur(14px);
      border-bottom: 1px solid var(--line);
    }

    .nav-logo {
      font-weight: 800;
      font-size: 1rem;
      color: var(--accent);
      letter-spacing: 0.06em;
    }

    .nav-links {
      display: flex;
      list-style: none;
      gap: 24px;
    }

    .nav-links a {
      color: var(--muted);
      text-decoration: none;
      font-size: 0.875rem;
      font-weight: 500;
      transition: color 0.2s;
    }

    .nav-links a:hover { color: var(--text); }

    /* ── PAGE WRAPPER ── */
    .page {
      max-width: 740px;
      margin: 0 auto;
      padding: 0 24px;
    }

    /* ── HERO ── */
    #hero {
      padding: 96px 24px 72px;
      text-align: center;
    }

    .hero-tag {
      display: inline-block;
      background: rgba(79, 124, 172, 0.12);
      border: 1px solid rgba(79, 124, 172, 0.35);
      color: var(--accent);
      padding: 5px 14px;
      border-radius: 999px;
      font-size: 0.78rem;
      font-weight: 600;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      margin-bottom: 22px;
    }

    #hero h1 {
      font-size: clamp(2.2rem, 5vw, 3.4rem);
      font-weight: 800;
      color: #f0f8ff;
      line-height: 1.15;
      margin-bottom: 14px;
    }

    #hero h1 span { color: var(--accent); }

    .hero-subtitle {
      font-size: 1.1rem;
      font-weight: 600;
      color: var(--text);
      margin-bottom: 8px;
    }

    .hero-desc {
      color: var(--muted);
      font-size: 0.95rem;
      margin-bottom: 32px;
    }

    .hero-btns {
      display: flex;
      gap: 12px;
      justify-content: center;
      flex-wrap: wrap;
      margin-bottom: 36px;
    }

    .btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 10px 24px;
      border-radius: var(--radius);
      font-size: 0.92rem;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.2s;
      cursor: pointer;
    }

    .btn-primary { background: var(--accent); color: #fff; border: 1px solid var(--accent); }
    .btn-primary:hover { background: var(--accent-hover); border-color: var(--accent-hover); }

    .btn-outline { background: transparent; color: var(--text); border: 1px solid var(--line); }
    .btn-outline:hover { border-color: var(--accent); color: var(--accent); }

    /* ── BADGE PILLS ── */
    .badge-row {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 10px;
      margin-bottom: 36px;
    }

    .badge {
      display: inline-flex;
      align-items: center;
      gap: 7px;
      background: var(--surface);
      border: 1px solid var(--line);
      color: var(--muted);
      padding: 7px 16px;
      border-radius: 999px;
      font-size: 0.85rem;
      font-weight: 500;
    }

    .badge-icon { font-size: 0.95rem; }

    /* ── DIVIDER ── */
    .divider {
      border: none;
      border-top: 1px solid var(--line);
      margin: 0 0 60px;
    }

    /* ── SECTION HEADING (lines flanking title) ── */
    .section-heading {
      display: flex;
      align-items: center;
      gap: 14px;
      margin-bottom: 28px;
    }

    .section-heading::before,
    .section-heading::after {
      content: '';
      flex: 1;
      height: 1px;
      background: var(--line);
    }

    .section-heading h2 {
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--text);
      white-space: nowrap;
    }

    /* ── CARD GRID (3-col, icon top-center) ── */
    .card-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 14px;
      margin-bottom: 60px;
    }

    .card {
      background: var(--surface);
      border: 1px solid var(--line);
      border-radius: var(--radius);
      padding: 24px 18px;
      text-align: center;
      transition: border-color 0.2s;
    }

    .card:hover { border-color: var(--accent); }

    .card-icon {
      font-size: 2rem;
      margin-bottom: 12px;
      display: block;
    }

    .card-title {
      font-weight: 700;
      font-size: 0.95rem;
      color: #f0f8ff;
      margin-bottom: 8px;
    }

    .card-desc {
      color: var(--muted);
      font-size: 0.83rem;
      line-height: 1.55;
    }

    /* ── TAG CHIPS ── */
    .tag-wrap {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 6px;
      margin-top: 10px;
    }

    .tag {
      background: var(--tag-bg);
      border: 1px solid var(--line);
      color: #8ba5c8;
      padding: 3px 9px;
      border-radius: 5px;
      font-size: 0.76rem;
    }

    /* ── FEATURE LIST (experience/projects) ── */
    .feature-list {
      margin-bottom: 60px;
    }

    .feature-item {
      display: flex;
      align-items: flex-start;
      gap: 14px;
      padding: 18px 0;
      border-bottom: 1px solid var(--line);
    }

    .feature-item:first-child { border-top: 1px solid var(--line); }

    .feature-bullet {
      color: var(--line);
      font-size: 0.7rem;
      margin-top: 5px;
      flex-shrink: 0;
    }

    .feature-icon {
      font-size: 1.4rem;
      flex-shrink: 0;
      width: 32px;
      text-align: center;
    }

    .feature-body { flex: 1; }

    .feature-title {
      font-weight: 700;
      font-size: 0.97rem;
      color: #f0f8ff;
      margin-bottom: 2px;
    }

    .feature-meta {
      font-size: 0.82rem;
      color: var(--accent);
      margin-bottom: 6px;
    }

    .feature-desc {
      color: var(--muted);
      font-size: 0.88rem;
    }

    .feature-bullets {
      padding-left: 16px;
      color: var(--muted);
      font-size: 0.86rem;
    }

    .feature-bullets li { margin-bottom: 4px; }

    /* ── CERT / EDU ROWS ── */
    .list-card {
      display: flex;
      align-items: center;
      gap: 14px;
      padding: 16px 0;
      border-bottom: 1px solid var(--line);
    }

    .list-card:first-child { border-top: 1px solid var(--line); }

    .list-icon { font-size: 1.5rem; flex-shrink: 0; }

    .list-title {
      font-weight: 600;
      font-size: 0.94rem;
      color: #f0f8ff;
      margin-bottom: 2px;
    }

    .list-sub {
      font-size: 0.82rem;
      color: var(--muted);
    }

    .list-desc {
      font-size: 0.83rem;
      color: var(--muted);
      margin-top: 4px;
    }

    /* ── CONTACT ── */
    .contact-note {
      text-align: center;
      color: var(--muted);
      font-size: 0.92rem;
      margin-bottom: 20px;
    }

    .contact-row {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 10px;
      margin-bottom: 60px;
    }

    .contact-link {
      display: inline-flex;
      align-items: center;
      gap: 7px;
      padding: 9px 18px;
      border: 1px solid var(--line);
      border-radius: var(--radius);
      color: var(--muted);
      text-decoration: none;
      font-size: 0.88rem;
      transition: all 0.2s;
    }

    .contact-link svg { width: 15px; height: 15px; }
    .contact-link:hover { border-color: var(--accent); color: var(--accent); }

    /* ── FOOTER ── */
    footer {
      text-align: center;
      padding: 24px;
      color: var(--muted);
      font-size: 0.82rem;
      border-top: 1px solid var(--line);
    }

    /* ── RESPONSIVE ── */
    @media (max-width: 640px) {
      .card-grid { grid-template-columns: 1fr; }
      .nav-links { display: none; }
      #hero h1 { font-size: 2rem; }
      .hero-btns { flex-direction: column; align-items: center; }
    }

    @media (max-width: 480px) {
      .badge-row { gap: 7px; }
      .badge { font-size: 0.78rem; padding: 6px 12px; }
    }
  </style>
</head>
<body>

  <!-- NAV -->
  <nav>
    <span class="nav-logo">UFM</span>
    <ul class="nav-links">
      <li><a href="#about">About</a></li>
      <li><a href="#skills">Skills</a></li>
      <li><a href="#experience">Experience</a></li>
      <li><a href="#projects">Projects</a></li>
      <li><a href="#certifications">Certs</a></li>
      <li><a href="#contact">Contact</a></li>
    </ul>
  </nav>

  <div class="page">

    <!-- HERO -->
    <section id="hero">
      <span class="hero-tag">Available for Opportunities</span>
      <h1>Umar Farouk <span>Muftau</span></h1>
      <p class="hero-subtitle">Cloud Security &nbsp;&middot;&nbsp; Cloud Engineer &nbsp;&middot;&nbsp; DevOps Engineer</p>
      <p class="hero-desc">&#128205; New York, USA &nbsp;&mdash;&nbsp; Building secure, scalable AWS infrastructures.</p>
      <div class="hero-btns">
        <a href="#contact" class="btn btn-primary">Get In Touch</a>
        <a href="https://github.com/umarfarouk16" target="_blank" rel="noopener" class="btn btn-outline">
          <svg viewBox="0 0 24 24" fill="currentColor" width="15" height="15"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/></svg>
          View on GitHub
        </a>
        <a href="https://www.linkedin.com/in/umar-farouk-muftau-5621ba185/" target="_blank" rel="noopener" class="btn btn-outline">
          <svg viewBox="0 0 24 24" fill="currentColor" width="15" height="15"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.064 2.064 0 1 1 2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
          LinkedIn
        </a>
      </div>

      <!-- STAT BADGES -->
      <div class="badge-row">
        <span class="badge"><span class="badge-icon">&#128197;</span> 3+ Years Experience</span>
        <span class="badge"><span class="badge-icon">&#9989;</span> 99.9% Availability</span>
        <span class="badge"><span class="badge-icon">&#127942;</span> 3 Certifications</span>
        <span class="badge"><span class="badge-icon">&#128640;</span> 40% Deployment Savings</span>
      </div>
    </section>

    <hr class="divider" id="about" />

    <!-- ABOUT + TOP SKILL CARDS -->
    <div class="section-heading"><h2>About Me</h2></div>
    <p style="color:var(--muted); font-size:0.95rem; text-align:center; margin-bottom:28px;">
      Cloud Engineer with 3+ years of experience designing secure, scalable, and automated cloud infrastructures across enterprise environments.
      Proven expertise in AWS architecture, infrastructure automation, DevOps CI/CD pipelines, cloud security engineering, and production system reliability.
    </p>

    <!-- 3 FEATURE CARDS -->
    <div class="card-grid" id="skills">
      <div class="card">
        <span class="card-icon">&#9729;&#65039;</span>
        <div class="card-title">Cloud Platforms</div>
        <div class="card-desc">Multi-account AWS architectures built for scale and security.</div>
        <div class="tag-wrap">
          <span class="tag">EC2</span><span class="tag">VPC</span><span class="tag">S3</span><span class="tag">EKS</span><span class="tag">Lambda</span><span class="tag">RDS</span>
        </div>
      </div>
      <div class="card">
        <span class="card-icon">&#9881;&#65039;</span>
        <div class="card-title">DevOps &amp; CI/CD</div>
        <div class="card-desc">Automated pipelines from commit to production with zero downtime.</div>
        <div class="tag-wrap">
          <span class="tag">GitHub Actions</span><span class="tag">Docker</span><span class="tag">Terraform</span><span class="tag">ArgoCD</span>
        </div>
      </div>
      <div class="card">
        <span class="card-icon">&#128274;</span>
        <div class="card-title">Security Engineering</div>
        <div class="card-desc">PCI-DSS, HIPAA &amp; GDPR-aligned controls across cloud environments.</div>
        <div class="tag-wrap">
          <span class="tag">IAM</span><span class="tag">WAF</span><span class="tag">Security Hub</span><span class="tag">Macie</span>
        </div>
      </div>
    </div>

    <!-- FULL SKILLS -->
    <div class="section-heading"><h2>All Skills</h2></div>
    <div class="card-grid" style="margin-bottom:60px;">
      <div class="card">
        <span class="card-icon">&#129302;</span>
        <div class="card-title">Automation &amp; Scripting</div>
        <div class="tag-wrap">
          <span class="tag">Python</span><span class="tag">Bash</span><span class="tag">PowerShell</span><span class="tag">Ansible</span><span class="tag">CloudFormation</span>
        </div>
      </div>
      <div class="card">
        <span class="card-icon">&#128202;</span>
        <div class="card-title">Monitoring &amp; Logging</div>
        <div class="tag-wrap">
          <span class="tag">CloudWatch</span><span class="tag">Grafana</span><span class="tag">CloudTrail</span><span class="tag">Alerting</span>
        </div>
      </div>
      <div class="card">
        <span class="card-icon">&#128101;</span>
        <div class="card-title">Compliance</div>
        <div class="tag-wrap">
          <span class="tag">PCI-DSS</span><span class="tag">HIPAA</span><span class="tag">GDPR</span><span class="tag">Incident Response</span>
        </div>
      </div>
    </div>

    <!-- EXPERIENCE -->
    <div class="section-heading" id="experience"><h2>Work History</h2></div>
    <div class="feature-list">
      <div class="feature-item">
        <span class="feature-bullet">&#9679;</span>
        <span class="feature-icon">&#127970;</span>
        <div class="feature-body">
          <div class="feature-title">AWS Cloud Architect / Cloud Engineer</div>
          <div class="feature-meta">Barclays Bank &nbsp;&middot;&nbsp; Whippany, NJ &nbsp;&middot;&nbsp; Nov 2022 &ndash; Nov 2025</div>
          <ul class="feature-bullets">
            <li>Architected secure multi-tier AWS cloud infrastructures achieving 99.9% system availability.</li>
            <li>Automated infrastructure provisioning with CloudFormation, Terraform &amp; Ansible — reduced deployment effort by 40%.</li>
            <li>Built CI/CD pipelines using GitHub Actions, Jenkins, and AWS CodePipeline with EKS and GitOps workflows.</li>
            <li>Migrated on-premise enterprise databases to AWS RDS using Database Migration Service.</li>
            <li>Implemented IAM least-privilege strategies, cross-account role management, and PCI-DSS / HIPAA / GDPR controls.</li>
            <li>Designed centralized logging with Lambda, CloudWatch, and Grafana dashboards.</li>
          </ul>
        </div>
      </div>
      <div class="feature-item">
        <span class="feature-bullet">&#9679;</span>
        <span class="feature-icon">&#128187;</span>
        <div class="feature-body">
          <div class="feature-title">Technical Support Intern</div>
          <div class="feature-meta">DOE Schools &nbsp;&middot;&nbsp; Bronx, NY &nbsp;&middot;&nbsp; Jan 2020 &ndash; Dec 2021</div>
          <ul class="feature-bullets">
            <li>Enterprise IT support across hardware, software, and network infrastructure.</li>
            <li>Maintained asset tracking and improved inventory management for technology lifecycle.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- PROJECTS -->
    <div class="section-heading" id="projects"><h2>Cloud &amp; DevOps Projects</h2></div>
    <div class="feature-list">
      <div class="feature-item">
        <span class="feature-bullet">&#9679;</span>
        <span class="feature-icon">&#128640;</span>
        <div class="feature-body">
          <div class="feature-title">Enterprise Cloud Migration</div>
          <div class="feature-desc">Migrated workloads and databases from on-premise to AWS with minimal downtime. Used RDS, DMS, and EC2 for seamless cutover.</div>
        </div>
      </div>
      <div class="feature-item">
        <span class="feature-bullet">&#9679;</span>
        <span class="feature-icon">&#127959;&#65039;</span>
        <div class="feature-body">
          <div class="feature-title">Infrastructure Automation (IaC)</div>
          <div class="feature-desc">Reusable Terraform and CloudFormation templates for rapid multi-tier environment provisioning across dev and production.</div>
        </div>
      </div>
      <div class="feature-item">
        <span class="feature-bullet">&#9679;</span>
        <span class="feature-icon">&#128260;</span>
        <div class="feature-body">
          <div class="feature-title">CI/CD Pipeline Implementation</div>
          <div class="feature-desc">End-to-end automated pipelines with GitHub Actions, Jenkins, Docker, and EKS for continuous delivery.</div>
        </div>
      </div>
      <div class="feature-item">
        <span class="feature-bullet">&#9679;</span>
        <span class="feature-icon">&#128225;</span>
        <div class="feature-body">
          <div class="feature-title">Centralized Logging &amp; Monitoring</div>
          <div class="feature-desc">Monitoring pipelines using CloudWatch, Grafana, Lambda, and CloudTrail for proactive incident detection.</div>
        </div>
      </div>
    </div>

    <!-- CERTIFICATIONS -->
    <div class="section-heading" id="certifications"><h2>Certifications</h2></div>
    <div class="feature-list" style="margin-bottom:60px;">
      <div class="list-card">
        <span class="list-icon">&#128992;</span>
        <div>
          <div class="list-title">AWS Certified Security &ndash; Specialty</div>
          <div class="list-sub">Amazon Web Services</div>
        </div>
      </div>
      <div class="list-card">
        <span class="list-icon">&#128309;</span>
        <div>
          <div class="list-title">Microsoft Azure Administrator (AZ-104)</div>
          <div class="list-sub">Microsoft</div>
        </div>
      </div>
      <div class="list-card">
        <span class="list-icon">&#128308;</span>
        <div>
          <div class="list-title">CompTIA Security+</div>
          <div class="list-sub">CompTIA</div>
        </div>
      </div>
    </div>

    <!-- EDUCATION -->
    <div class="section-heading"><h2>Education</h2></div>
    <div class="feature-list" style="margin-bottom:60px;">
      <div class="list-card">
        <span class="list-icon">&#127891;</span>
        <div>
          <div class="list-title">BS, Computer Information Systems</div>
          <div class="list-sub">CUNY Lehman College &nbsp;&middot;&nbsp; Bronx, NY</div>
        </div>
      </div>
      <div class="list-card">
        <span class="list-icon">&#9729;&#65039;</span>
        <div>
          <div class="list-title">AWS Cloud Security Bootcamp</div>
          <div class="list-sub">Thinkcloudly</div>
          <div class="list-desc">IAM, KMS encryption, secure VPC architectures, CloudTrail &amp; CloudWatch, incident response, compliance best practices.</div>
        </div>
      </div>
    </div>

    <!-- CONTACT -->
    <div class="section-heading" id="contact"><h2>Let's Connect</h2></div>
    <p class="contact-note">Open to Cloud, DevOps, and Security engineering opportunities. Feel free to reach out.</p>
    <div class="contact-row">
      <a href="mailto:umarmuftau16@gmail.com" class="contact-link">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>
        umarmuftau16@gmail.com
      </a>
      <a href="https://github.com/umarfarouk16" target="_blank" rel="noopener" class="contact-link">
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/></svg>
        GitHub
      </a>
      <a href="https://www.linkedin.com/in/umar-farouk-muftau-5621ba185/" target="_blank" rel="noopener" class="contact-link">
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.064 2.064 0 1 1 2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
        LinkedIn
      </a>
      <a href="tel:+13473795936" class="contact-link">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 12a19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 3.6 1.27h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L7.91 8.91a16 16 0 0 0 6 6l.91-.91a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
        (347) 379-5936
      </a>
    </div>

  </div><!-- /page -->

  <!-- FOOTER -->
  <footer>
    <p>&#169; 2026 Umar Farouk Muftau &nbsp;&middot;&nbsp; Built with Flask &nbsp;&middot;&nbsp; Hosted on AWS EC2</p>
  </footer>

</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(TEMPLATE)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
