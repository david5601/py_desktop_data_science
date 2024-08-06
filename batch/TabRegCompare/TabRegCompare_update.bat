@echo off
setlocal enabledelayedexpansion

rem Set file names
set "currentFile=9-TabReg.csv"
set "newFile=Export_2024_03_30.csv"
set "differencesFile=differences.csv"
set "similaritiesFile=similarities.csv"

set "index=0"
(for /F "usebackq tokens=1,2 delims=," %%A in ("%currentFile%") do (
    set "found="
    for /F "usebackq tokens=1 delims=," %%B in ("%newFile%") do (
        if "%%A"=="%%B" (
            set "found=1"
        )
    )
    set /A index += 1
    if not defined found echo %%A,%%B
)) > "%differencesFile%"

(for /F "usebackq tokens=1,2 delims=," %%A in ("%currentFile%") do (
    set "found="
    for /F "usebackq tokens=1 delims=," %%B in ("%newFile%") do (
        if "%%A"=="%%B" (
            set "found=1"
        )
    )
    if defined found echo %%A,%%B
)) > "%similaritiesFile%"