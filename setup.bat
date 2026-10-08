```bat
@echo off
title AYTRO GEN - Setup
color 0B

:menu
cls

echo ========================================================
echo                       AYTRO GEN
echo ========================================================
echo.
echo [1] Setup and Launch
echo [0] Exit
echo.
set /p choice=AYTRO GEN ^> 

if "%choice%"=="1" goto setup
if "%choice%"=="0" goto exit

echo.
echo [!] Invalid option.
timeout /t 2 >nul
goto menu


:setup
cls

echo.
echo ========================================================
echo                  AYTRO GEN SETUP
echo ========================================================
echo.

echo [1/3] Checking Python...
py --version >nul 2>&1

if errorlevel 1 (
    echo.
    echo [!] Python was not found.
    echo Please install Python and try again.
    echo.
    pause
    goto menu
)

echo [+] Python detected.
echo.

echo [2/3] Installing requirements...
echo.

py -m pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo [!] Failed to install requirements.
    echo.
    pause
    goto menu
)

echo.
echo [+] Requirements installed successfully.
echo.

echo [3/3] Starting AYTRO GEN...
echo.

timeout /t 2 >nul

start "AYTRO GEN" cmd /k "py main.py"

echo [+] AYTRO GEN has been launched in a new window.
echo.
timeout /t 3 >nul

goto menu


:exit
cls
echo.
echo Thanks for using AYTRO GEN!
echo.
timeout /t 2 >nul
exit
```