# 404 Not Found

## Setup

* Create a virtual environment
* Install requirements

### Virtual environment (venv)
see [https://docs.python.org/3/library/venv.html]

Windows - cmd.exe
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

Windows - PowerShell
```powershell
# You  On Microsoft Windows, it may be required to enable the Activate.ps1 script by setting the execution policy for the user. You can do this by issuing the following PowerShell command:
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Install requirements.txt
```
pip install -r requirements.txt
```