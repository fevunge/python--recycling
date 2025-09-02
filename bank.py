"""
El usuario comienza con un saldo de 1000.

Puede elegir entre: Depositar, Retirar, Ver saldo, Salir.

No permita que el saldo sea negativo.

El ciclo solo termina si selecciona "Salir".
"""

import sqlite3

def enter():
    print()

def regist():
    print()

def rising():
    print()

def deposit():
    print()

def see_balance():
    print()

connection = sqlite3.connect("bank.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    passwd TEXT NOT NULL,
    balance INTEGER
)""")



connection.commit()
connection.close()
