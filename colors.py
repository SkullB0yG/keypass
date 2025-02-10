#!/bin/python 

import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

def Color(color, text):
    try:
        if color == "red":
            return Fore.RED + text
        elif color == "blue":
            return Fore.BLUE + text
        elif color == "green":
            return Fore.GREEN + text
        elif color == "yellow":
            return Fore.YELLOW + text
        elif color == "cyan":
            return Fore.CYAN + text
        elif color == "white":
            return Fore.WHITE + text
        else:
            return text  # Devuelve el texto sin cambios si el color no coincide
    except Exception as e:
        print(f"Error: {e}")
        return text  # Devuelve el texto sin cambios en caso de error
    
def Background(color, text):
	try:
		if color == "red":
			return Back.RED + text
		elif color == "blue":
			return Back.BLUE + text
		elif color == "green":
			return Back.GREEN + text
		elif color == "yellow":
			return Back.YELLOW + text
		elif color == "cyan":
			return Back.CYAN + text
		elif color == "white":
			return Back.WHITE + text
		else:
			return text  # Devuelve el texto sin cambios si el color no coincide
	except Exception as e:
		print(f"Error: {e}")
		return text  # Devuelve el texto sin cambios en caso de error
      