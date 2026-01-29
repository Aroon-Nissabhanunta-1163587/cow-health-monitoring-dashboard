#!/usr/bin/env python3
"""
Cow Health Monitoring Dashboard - Setup Script
Quick-start script that checks dependencies and initializes the system
"""

import sys
import subprocess

def check_python_version():
    if sys.version_info < (3, 7):
        print("Error: Python 3.7 or higher is required")
        sys.exit(1)
    print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor}")

def check_dependencies():
    try:
        import pandas
        import numpy
        import matplotlib
        print("✓ All dependencies installed")
    except ImportError:
        print("Installing dependencies...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

if __name__ == "__main__":
    print("="*50)
    print("Cow Health Monitoring Dashboard Setup")
    print("="*50)
    check_python_version()
    check_dependencies()
    print("\n✓ Setup complete!")
    print("To start: python dashboard.py")
