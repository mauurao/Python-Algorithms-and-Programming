#!/usr/bin/python

"""
This program will align multiple variables with a specific position parameter.

"""

if __name__ == "__main__":

    E1, E2=20, 15 # Position
    name1, name2, name3= "Ivo Gala", "Joana Silva", "Teresa Gomes"
    local1, local2, local3="Porto", "Lisboa", "Braga"

    print(f"{name1:<{E1}} {local1:<{E2}}")
    print(f"{name2:^{E1}} {local2:^{E2}}")
    print(f"{name3:>{E1}} {local3:>{E2}}")

"""
Result:

Ivo Gala             Porto          
    Joana Silva          Lisboa     
        Teresa Gomes           Braga

"""