@echo off

REM Create NewTablets.csv
echo InmateID,AID> NewTablets.csv
for /f "skip=1 tokens=5,1 delims=," %%a in (cr68TabletReportbyunit.csv) do (
    find "%%a" Protoss.csv > nul || echo %%a,%%b>> NewTablets.csv
)

REM Create Tablet_Replacement.csv
echo InmateID,AID> Tablet_Replacement.csv
for /f "skip=1 tokens=1,2 delims=," %%a in (Protoss.csv) do (
    find "%%a" cr68TabletReportbyunit.csv > nul || echo %%a,%%b>> Tablet_Replacement.csv
)

REM Create Discrepancies.csv
echo InmateID,AID> Discrepancies.csv
for /f "skip=1 tokens=5,1 delims=," %%a in (cr68TabletReportbyunit.csv) do (
    find "%%a" Protoss.csv > nul || echo %%a,%%b>> Discrepancies.csv
)

echo The CSV processing completed successfully.
pause
