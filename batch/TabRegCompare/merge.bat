@echo off
setlocal enabledelayedexpansion

rem Set file names
set "differencesFile=differences.csv"
rem set "similaritiesFile=similarities.csv"
set "mergedFile=9-TabReg.csv"

rem Merge similarities.csv and differences.csv
rem copy /Y "%similaritiesFile%" "%mergedFile%" > nul
(for /F "usebackq tokens=*" %%A in ("%differencesFile%") do (
    echo %%A
    echo %%A >> "%mergedFile%"
))

echo Files merged successfully!