###
# Repository Name
Short description of the repository.

## Table of Contents

- [Repository Name](#repository-name)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)

## Installation

To install this Python project using pyenv, follow these steps:

1. Install pyenv by following the instructions at [pyenv GitHub repository](https://github.com/pyenv/pyenv#installation).
2. Clone the repository: `git clone https://github.com/your/repository.git`.
3. Navigate to the project directory: `cd repository`.
4. Set the Python version for the project: `pyenv local <python_version>`.
5. Install the required dependencies: `pip install -r requirements.txt`.
6. Setup Environment Variables: `cp .env.example .env` and fill in the required environment variables.



## Usage

1. Decrypt data, the input file is `./input/encrypted.json`:

```bash
python3 ./main.py decrypt
```



2. Renew assumed role, the input file is `./input/assume_role.json`:

```bash
python3 ./main.py renew-assume-role
```