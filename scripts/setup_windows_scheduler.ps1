# Disha Phase 2 - Setup Windows Task Scheduler for Daily Commits
# Run this in PowerShell as Administrator if you want local daily automated commits on your PC.

$Action = New-ScheduledTaskAction -Execute "python.exe" -Argument "c:\Users\ASUS\Downloads\Disha-phase-2\scripts\run_daily_commits.py --count 4 --push" -WorkingDirectory "c:\Users\ASUS\Downloads\Disha-phase-2"
$Trigger = New-ScheduledTaskTrigger -Daily -At "11:00 AM"
$Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable

Register-ScheduledTask -TaskName "DishaDailyGitCommits" -Action $Action -Trigger $Trigger -Settings $Settings -Description "Runs daily commits for Disha Phase 2"

Write-Host "Scheduled task 'DishaDailyGitCommits' registered successfully for 11:00 AM daily."
