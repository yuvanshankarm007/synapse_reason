@echo off
echo ========================================================
echo   Starting SynapseReason - Cognitive Architecture Demo
echo   Zetaris 5-Silo Virtual Data Fabric + Agent Swarm
echo ========================================================
cd /d "%~dp0"
if exist ".venv\Scripts\streamlit.exe" (
    echo Launching Streamlit in dedicated virtual environment...
    ".venv\Scripts\streamlit.exe" run app.py
) else (
    echo Launching Streamlit using system python...
    streamlit run app.py
)
pause
