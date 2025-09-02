"""
El usuario comienza con un saldo de 1000.

Puede elegir entre: Depositar, Retirar, Ver saldo, Salir.

No permita que el saldo sea negativo.

El ciclo solo termina si selecciona "Salir".
"""

import sqlite3
import platform
from random import randint, random
import time

def cleancli():
    if "Linux" == platform.system():
        platform.os.system("clear")
    elif "Windows" == platform.system():
        platform.os.system("cls")

def rising():
    print("RISING".center(42, '+'), "-" * 42, sep='\n')
    print("Insert the amount you want to rising:".center(42, '_'))

def deposit(conn, cursos, user):
    print(" DEPOSIT ".center(42, '+'), "-" * 42, sep='\n')
    print("*", "-" * 40, "*", sep="")
    print("|", f"User: {user[2]}".ljust(40, " "), "|", sep="")
    print("|", f"Account Number: {user[4]}".ljust(40, " "), "|", sep="")
    print("*", "-" * 40, "*", sep="")
    print("Insert amount to deposit")
    amount = int(input("amount: $ "))

def enter(conn, cursor):
    print("ENTER".center(42, '+'), "-" * 42, sep='\n')
    print("Insert your credencials".center(42, '_'))
    login = input("login: ")
    pin = input("pin: ")
    try:
        cursor.execute(f"SELECT login, pin FROM user")
        users = cursor.fetchall()
        if (login, pin) in users:
            cleancli()
            print("Success")
            cursor.execute("SELECT * FROM user WHERE login = ?", (login,))
            user = cursor.fetchone()
            print(f" Wellcome {user[2]} ".center(42, '+'))
            choice = None
            while (choice != 5):
                print("-" * 42, "[1] See Balance", "[2] Deposit", "[3] Resing", "[4] Settings", "[5] Exit", sep="\n")
                choice = int(input(":: "))
                if choice not in [1, 2, 3, 4, 5] :
                    cleancli()
                    print("  INVALID CHOICE  ".center(42, 'X'))
                if choice == 1:
                    print("*", "-" * 40, "*", sep="")
                    print("|", f"${float(user[6] / 100)}".center(40, " "), "|", sep="")
                    print("*", "-" * 40, "*", sep="")
                    input("OK? :: [continiue]")
                    cleancli()
                if choice == 2:
                    deposit(conn, cursor)

        else:
            cleancli()
            print(" Invalid credentials ".center(42, 'x'))
        return False
    except:
        cleancli()
        print("\n", " Something went wrong ".center(42, "x"))
        return None
    
def regist(conn, cursor):
    print("REGIST".center(42, '+'), "-" * 42, sep='\n')
    print("Insert your real name and nif please".center(42, '_'))
    names_part = ()
    message = "Full Name: "
    while (True):
        name = input(message)
        names_part = name.partition(" ")
        if names_part[2]:
            break
        message = "!Your really Full Name PLEASE!: "
    nif = input("NIF: ")
    pin = str(time.clock_gettime(1))[-5:-1]
    login = names_part[0][:2] + names_part[2]
    try:
        cursor.execute(f"INSERT INTO user (login, name, nif, pin, accountNum, balance) VALUES (?, ?, ?, ?, ?, ?)",
            (login.lower(), name, nif, pin, str(random())[1:7], 0))
        cleancli()
        print("\n", " Account created ".center(42, "+"))
        print("Your credentials. SAVE IT!", f"login: {login.lower()}", f"pin: {pin}", "-"*42, sep="\n")
        conn.commit()
        return True
    except:
        cleancli()
        print("\n", " Something went wrong ".center(42, "x"))
        return False

def logout(conn, cursor):
    print("Logout. Back soon!")
    

connection = sqlite3.connect("bank.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    pin TEXT NOT NULL,
    nif TEXT NOT NULL,
    accountNum TEXT NOT NULL,
    balance INTEGER
)""")

print(" WELLCOME AT BANK  ".center(42, '+'))
choice = None
menu = [enter, regist, logout]
while (choice != 3):
    print("Choice a valid option:: ".center(42, '_'))
    print("[1] Enter", "[2] Regist", "[3] Exit", sep='\n')
    choice = int(input(':: '))
    if choice not in [1, 2, 3] :
        cleancli()
        print("  INVALID CHOICE  ".center(42, 'X'))
    else:
        cleancli()
        menu[choice - 1](connection, cursor)
        connection.commit()
connection.close()
