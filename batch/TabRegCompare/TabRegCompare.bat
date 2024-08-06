@echo off
setlocal enabledelayedexpansion

set "file1=Export_2024_03_30.csv"
set "file2=9-TabReg.csv"
set "differences_file=differences.csv"
set "similarities_file=similarities.csv"

echo "%file1%"
REM Check if both CSV files exist
if not exist "%file1%" (
    echo CSV file "%file1%" not found.
    exit /b
)

if not exist "%file2%" (
    echo CSV file "%file2%" not found.
    exit /b
)

REM Initialize an array to store values from the first file
set "values="

REM Read values from the first file into the array
for /F "usebackq tokens=1 delims=," %%A in ("%file1%") do (
    set "values[%%A]=1"
)

REM Initialize the similarities file
echo. > "%similarities_file%"

REM Compare values from the second file with the values in the array
REM Output common values to the similarities file
(for /F "usebackq tokens=1,2 delims=," %%B in ("%file2%") do (
    if defined values[%%B] (
        echo %%B,%%C
    )
)) > "%similarities_file%"

echo Similar values have been saved to "%similarities_file%".

REM Initialize the differences file
echo. > "%differences_file%"

REM Compare values from the second file with the values in the array
REM Output differences to the differences file
(for /F "usebackq tokens=1,2 delims=," %%B in ("%file2%") do (
    if not defined values[%%B] (
        echo %%B,%%C
    )
)) > "%differences_file%"

echo Differences have been saved to "%differences_file%".

endlocal