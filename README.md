# Appium Test

This is a basic test project using the Appium framework. It includes a simple test case and is intended to run on an Android emulator.

## Requirements

- Python 3.13.3
- Android emulator  
- Appium server running  
- `.env` file with required environment variables

## Setup and run

1. Create and activate venv

```bash
python -m venv .venv
# On macOS/Linux:
source .venv/bin/activate
# On Windows (Command Prompt):
.venv\Scripts\activate.bat
# On Windows (PowerShell):
.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the test:

```bash
pytest tests/test_checkout.py -svrA
```
