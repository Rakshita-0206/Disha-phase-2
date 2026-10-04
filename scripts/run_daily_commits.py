"""
Disha Phase 2 - Daily Commit Runner
Creates N safe documentation commits and pushes to GitHub.
Ensures seamless progress tracking and activity requirements without altering project functionality.
"""

import os
import sys
import time
import argparse
import subprocess

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "scripts"))
from generate_commit import generate_one_update

def run_git(cmd, check=True):
    result = subprocess.run(cmd, cwd=BASE_DIR, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"Git error running {' '.join(cmd)}:\n{result.stderr}")
        raise subprocess.CalledProcessError(result.returncode, cmd, output=result.stdout, stderr=result.stderr)
    return result

def main():
    parser = argparse.ArgumentParser(description="Create daily automated documentation commits")
    parser.add_argument("--count", type=int, default=4, help="Number of commits to create (default: 4)")
    parser.add_argument("--push", action="store_true", default=False, help="Push commits to origin main after creation")
    parser.add_argument("--no-push", action="store_true", default=False, help="Do not push after commit creation")
    parser.add_argument("--interval", type=int, default=2, help="Seconds delay between commits (default: 2)")
    args = parser.parse_args()

    count = max(1, args.count)
    should_push = args.push and not args.no_push

    print(f"Starting daily commit generation: target = {count} commit(s)")

    for i in range(1, count + 1):
        print(f"\n[{i}/{count}] Generating commit...")
        msg = generate_one_update()
        
        # Stage documentation and changelog files
        run_git(["git", "add", "docs/", "CHANGELOG.md"])
        
        # Commit with the conventional message
        run_git(["git", "commit", "-m", msg])
        print(f"[{i}/{count}] Committed: {msg}")

        if i < count and args.interval > 0:
            time.sleep(args.interval)

    print(f"\nSuccessfully created {count} commit(s).")

    if should_push:
        print("Synchronizing with remote repository (origin/main)...")
        run_git(["git", "pull", "--rebase", "origin", "main"], check=False)
        print("Pushing to origin main...")
        run_git(["git", "push", "origin", "main"])
        print("All commits successfully pushed to GitHub!")

if __name__ == "__main__":
    main()
