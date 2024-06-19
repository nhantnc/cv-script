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
def renew_assumed_role_db():
    """
    Renew an Assum role
    """
    from app.aws import renew_assumed_role_from_db
    _id = int(input("Enter account id: "))
    renew_assumed_role_from_db(_id)

@app.command()
def menu():
    """
    Choose from the menu
    """
    typer.echo("1. Decrypt data")
    typer.echo("2. Renew Assumed Role")
    typer.echo("3. Renew Assumed Role from DB")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        decrypt()
    elif choice == 2:
        renew_assumed_role()
    elif choice == 3:
        renew_assumed_role_db()


if __name__ == "__main__":
    app()