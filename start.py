#!/usr/bin/python 

import base64
import colors as rainbow
import database as db
import sqlite3
import os


# Inicializamos Colors 

# Funciones

'''
    SHELL
    este codigo crea un input que permite escribor comado para interactuar con el programa 
'''
def shell():
    try:
        command = input(rainbow.Color(color="white", text="$> "))
        return command.split()
    except KeyboardInterrupt:
        exit = ["exit"]
        return exit

'''
    HELP 
    esta funcion permite mostar los comados permitidos y que hace cada uno 
'''

def help():
    print(rainbow.Color(color="green", text="[*] Comandos permitidos"))
    print(rainbow.Color(color="cyan", text="[*] init"))
    print(rainbow.Color(color="cyan", text="[*] create -r <username> <password> <app>"))
    print(rainbow.Color(color="cyan", text="[*] view"))
    print(rainbow.Color(color="cyan", text="[*] delete -U <username>"))
    print(rainbow.Color(color="cyan", text="[*] update -U <username> -p <password>"))
    print(rainbow.Color(color="cyan", text="[*] clear"))
    print(rainbow.Color(color="cyan", text="[*] exit"))
    

# Inicializar la base de datos
'''
    controller: permite darle salida del while 
    db: objeto de la importacion de database que gestiona la base de datos realiza las crud 
'''
controller = True
db=db.Database("/home/skull/scripts/keypass/database.db")

'''
    este while permite ejecutar de manera recurrente las funciones y comandos que se pueden ejecutar
'''

while controller:

    terminal = shell()
    if not terminal:
        continue

    if terminal[0] == "init":
        try:      
            create = db.create_table(db.create_table_sql()) 
            if create == True:
                print(rainbow.Color(color="green", text="[*] Successful db creation"))
            else:
                print(rainbow.Color(color="red", text="[!] Alert error creating table"))

        except KeyboardInterrupt:
            print(rainbow.Color(color="red", text="[!] Operation cancelled by user"))
            continue

    elif len(terminal) >= 5 and terminal[0] == "create" and terminal[1] == "-r":
        encod = None
        try:
            user = {"username": terminal[2], "password": terminal[3], "app": terminal[4]}
            db.create_record("users", user)
        except sqlite3.OperationalError as e:
            print(rainbow.Color(color="red", text="[!] Alert no such table"))
        except IndexError:
            print(rainbow.Color(color="red", text="[!] Alert missing arguments"))

    elif terminal[0] == "view":
        try:
            user = db.read_records("users")
	         
            for row in user:
                id, user, password, plataform = row 
                print(rainbow.Color(color="green", text=f"[*] ID {id} User -> {user}\tPasswd -> {password}\tPlataform -> {plataform}"))
        except Exception as e:
            print(rainbow.Color(color="red", text=f"[!] Alert {str(e)}"))

    elif len(terminal) >= 3 and terminal[0] == "delete" and terminal[1] == "-U":
        try:
            db.delete_record("users", f"username = '{terminal[2]}'")
        except IndexError:
            print(rainbow.Color(color="red", text="[!] Alert missing arguments"))
        except Exception as e:
            print(rainbow.Color(color="red", text=f"[!] Alert {str(e)}"))

    elif len(terminal) >= 5 and terminal[0] == "update" and terminal[1] == "-U" and terminal[3] == "-p":
        try:
            db.update_record("users", {"password": terminal[4]}, f"username = '{terminal[2]}'")
        except IndexError:
            print(rainbow.Color(color="red", text="[!] Alert missing arguments"))
        except Exception as e:
            print(rainbow.Color(color="red", text=f"[!] Alert {str(e)}"))

    elif terminal[0] == "help":
        help()
    elif terminal[0] == "exit":
        os.system("clear")
        controller = False
    elif terminal[0] == "clear":
        os.system("clear")
    else:
        print(rainbow.Color(color="red", text="[!] Unknown command"))
