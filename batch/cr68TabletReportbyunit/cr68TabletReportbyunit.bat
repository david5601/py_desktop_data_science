@echo off
setlocal enabledelayedexpansion

rem Set file names
set "currentFile=cr68TabletReportbyunit.csv"
set "newFile=Export_2024_03_30.csv"
set "differencesFile=differences.csv"
set "similaritiesFile=similarities.csv"

rem Compare files by column B in currentFile and column A in newFile
(for /F "usebackq tokens=1,2 delims=," %%A in (%currentFile%) do (
    set "found="
    for /F "usebackq tokens=1 delims=," %%C in (%newFile%) do (
        if "%%B"=="%%C" (
            set "found=1"
        )
    )
    if not defined found echo %%A,%%B
)) > "%differencesFile%"

(for /F "usebackq tokens=1,2 delims=," %%A in (%currentFile%) do (
    set "found="
    for /F "usebackq tokens=1 delims=," %%C in (%newFile%) do (
        if "%%B"=="%%C" (
            set "found=1"
        )
    )
    if defined found echo %%A,%%B
)) > "%similaritiesFile%"
