import subprocess
import sys
import os

def install_python_requirements():
    try:
        print("Installing Python requirements...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Python requirements installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing Python requirements: {e}")

def install_npm_packages(path):
    try:
        print(f"Installing npm packages in {path}...")
        subprocess.check_call(["npm", "install"], cwd=path)
        print(f"npm packages installed successfully in {path}.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing npm packages in {path}: {e}")

if __name__ == "__main__":
    # Install Python requirements
    install_python_requirements()

    # Install npm packages for desktop app
    desktop_path = os.path.join("../platform/desktop")
    if os.path.exists(desktop_path):
        install_npm_packages(desktop_path)
    else:
        print(f"Directory {desktop_path} does not exist. Skipping npm install for desktop app.")

    # Install npm packages for mobile app
    mobile_path = os.path.join("mobile")
    if os.path.exists(mobile_path):
        install_npm_packages(mobile_path)
    else:
        print(f"Directory {mobile_path} does not exist. Skipping npm install for mobile app.")

    # Install npm packages for web app
    web_path = os.path.join("web")
    if os.path.exists(web_path):
        install_npm_packages(web_path)
    else:
        print(f"Directory {web_path} does not exist. Skipping npm install for web app.")
