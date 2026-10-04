@echo off
REM ===================================================================
REM Disha Phase 2 - 1-Click Daily Committer
REM Creates 4 realistic documentation commits and pushes to GitHub
REM ===================================================================

echo ===================================================
echo [Disha Phase 2] Generating Daily Commits for GitHub
echo ===================================================

cd /d "%~dp0\.."

python scripts\run_daily_commits.py --count 4 --push

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ===================================================
    echo [SUCCESS] 4 commits successfully generated and pushed!
    echo ===================================================
) else (
    echo.
    echo ===================================================
    echo [ERROR] Commit or push failed. Check your network/git status.
    echo ===================================================
)

pause
