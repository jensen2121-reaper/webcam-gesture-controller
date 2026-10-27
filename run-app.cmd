@echo off
title AI 手勢簡報控制器 (本機伺服器)
cd /d "%~dp0"
echo.
echo ========================================================
echo    正在啟動 AI 手勢簡報控制器本機伺服器...
echo    網址: http://localhost:8000
echo ========================================================
echo.
start "" "http://localhost:8000"
python -m http.server 8000
