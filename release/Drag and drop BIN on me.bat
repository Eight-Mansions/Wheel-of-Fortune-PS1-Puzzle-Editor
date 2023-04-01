@echo off
set filename=Lovecraft Wheel of Fortune - Beta 1
set file_type=ISO
set patch_file=Lovecraft-WoF-patch.xdelta

set found_disc=

pushd %~dp0
if "%~1"=="" goto :NOISO

echo #################################
echo Lovecraft Wheel of Fortune (Beta)
echo #################################
echo:
echo:

:: Iterate over all files that get dragged onto here
for %%A in (%*) do (
    echo "Checking %%A..."
    echo:

    patch_data\xdelta.exe -d -f -s %%A "patch_data\%patch_file%" "%filename%.iso" 2>nul
    if not errorlevel 1 (
        set found_disc=true

	echo ***
	echo:
        echo "Perfect! Original disc for 'Wheel of Fortune' found!"
    )

)

if not defined found_disc goto :NOPATCHFOUND

echo "You're ready to go!"
echo:
echo ---
echo The following %file_type% file should have been created next to the bat file:
echo * %filename%.iso
echo ---
echo:
echo "Now just load up this .iso file on your favorite device and enjoy!"
echo:
goto :EXIT

:NOISO
echo To patch %file_type% don't run this bat file.
echo Simply drag and drop the bin file on it and the patch process will start.
goto :EXIT

:NOPATCHFOUND
echo "Uh oh, no patch found suitable for any of the supplied files.
echo  Please make sure to drag in a clean BIN file of the original 'Wheel of Fortune'."
echo:
echo "If the problem persists, go throw a sad puppy at SnowyAria ; _;,
echo  "I'm sure she did something again..."

:EXIT
popd
echo:
echo Press any key to close this window
pause >nul
exit
