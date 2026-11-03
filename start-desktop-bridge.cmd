@echo off
title AI 手勢全域簡報控制器 (PowerPoint / PDF 系統級橋接)
chcp 65001 >nul
cd /d "%~dp0"
echo.
echo ========================================================
echo    正在啟動 AI 手勢全域簡報控制器...
echo    支援：PowerPoint、Google Slides、Canva、Adobe PDF
echo ========================================================
echo.
python desktop_bridge.py
pause
