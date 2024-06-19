## Installation

To install this Python project using pyenv, follow these steps:

1. Clone the repository: `git clone https://github.com/nhantnc/cv-script.git`.
2. Navigate to the project directory: `cd cv-script`.
3. Install virtualenv via pip: `pip install virtualenv`.
4. Create a virtual environment: `virtualenv local`.
5. Activate the virtual environment: `source local/bin/activate`.
6. Install the required dependencies: `pip install -r requirements.txt`.
7. Setup Environment Variables: `cp .env.example .env` and fill in the required environment variables.
8. Deactivate the virtual environment: `deactivate`.
9. Freeze the virtual environment: `pigar generate`.



## Usage

1. Decrypt data, the input file is `./input/encrypted.json`:

```bash
python3 ./main.py decrypt
```



2. Renew assumed role, the input file is `./input/assume_role.json`:

```bash
python3 ./main.py renew-assume-role
```

3. Using menu to choose the function you want to run:

```bash
python3 ./main.py menu
```