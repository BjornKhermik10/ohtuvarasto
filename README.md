# ohtuvarasto
[![CI](https://github.com/bjornkhermik10/ohtuvarasto/actions/workflows/main.yml/badge.svg)](https://github.com/käyttäjänimi/ohtuvarasto/actions)

[![codecov](https://codecov.io/github/BjornKhermik10/ohtuvarasto/graph/badge.svg?token=H7SPXIU1N6)](https://codecov.io/github/BjornKhermik10/ohtuvarasto)

## Installation

### Prerequisites

1. **Python 3.12 or higher**
   - Download from [python.org](https://www.python.org/downloads/)
   - During installation, check "Add Python to PATH"

2. **Poetry** (Python package manager)
   - Install Poetry by running in PowerShell:
     ```powershell
     (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
     ```
   - The installer will display the path where Poetry is installed. Add this path to your system's PATH environment variable (typically `%APPDATA%\pypoetry\venv\Scripts`)
   - Restart PowerShell after installation

### Installing Dependencies

1. Clone the repository:
   ```powershell
   git clone https://github.com/BjornKhermik10/ohtuvarasto.git
   cd ohtuvarasto
   ```

2. Install project dependencies:
   ```powershell
   poetry install
   ```

## Running the Application on Windows PowerShell

### Running the Console Application

```powershell
cd src
poetry run python index.py
```

### Running the Flask Web Application

```powershell
cd src/webapp
poetry run python app.py
```

The web application will start on `http://127.0.0.1:5000/`.

To run in debug mode:
```powershell
cd src/webapp
$env:FLASK_DEBUG = "true"
poetry run python app.py
```

### Running Tests

```powershell
poetry run pytest
```

### Running Tests with Coverage

```powershell
poetry run coverage run --branch -m pytest
poetry run coverage report
```

### Running Linter

```powershell
poetry run pylint src
```
