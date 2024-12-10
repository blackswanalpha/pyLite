import os
import subprocess
import argparse

def run_flask():
    subprocess.run(["python", "app.py"])

def run_nextjs():
    subprocess.run(["npm", "run", "dev"], cwd="platform/desktop")

def run_react_native():
    subprocess.run(["npx", "react-native", "run-android"], cwd="platform/mobile")

def run_react():
    subprocess.run(["npm", "start"], cwd="platform/web")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run PyLite application platforms.")
    parser.add_argument(
        "--platforms",
        nargs="+",
        choices=["desktop", "web", "mobile", "backend"],
        default=["backend"],
        help="Specify which platforms to run (default: backend). Choices: desktop, web, mobile, backend",
    )

    args = parser.parse_args()
    platforms_to_run = args.platforms

    if "backend" in platforms_to_run:
        run_flask()

    if "desktop" in platforms_to_run:
        run_nextjs()

    if "mobile" in platforms_to_run:
        run_react_native()

    if "web" in platforms_to_run:
        run_react()
