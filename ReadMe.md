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
1. Run the command below and follow the menu:
```bash
source run.sh
```
2. The menu should be:
```bash
1. Decrypt data
2. Renew Assumed Role
3. Renew Assumed Role from DB
```

Note:
1. When you want to `Decrypt data`, the encrypted data should be in `\input\encrypted.json`.
2. When you want to `Renew Assumed Role`, the role data should be in `\input\assumed_role.json`.
