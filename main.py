#!/usr/bin/env python
import typer

app = typer.Typer()

@app.command()
def decrypt():
    """
    Decrypt the data
    """
    from app.kms import decrypt_data
    decrypt_data()

@app.command()
def renew_assumed_role():
    """
    Renew an Assum role
    """
    from app.aws import renew_assumed_role
    renew_assumed_role()


@app.command()
def decrypt():
    """
    Decrypt the data
    """
    from app.kms import decrypt_data
    decrypt_data()

@app.command()
def test():
    """
    test
    """
    from app.test import test
    test()

if __name__ == "__main__":
    app()