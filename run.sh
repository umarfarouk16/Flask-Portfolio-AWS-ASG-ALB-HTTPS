#!/bin/bash

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app in background
gunicorn -w 4 -b 0.0.0.0:8000 app:app &

echo "App started on port 8000"
