#!/usr/bin/env python3
import sql_manager
import Client
from getpass import getpass
from settings import EXIT_CMD


def main_menu():
    print("""Welcome to our bank service. You are not logged in.
          Please register or login""")

    while True:
        command = input("guest@hackabank$ ")

        if command == "register":
            username = input("Enter your username: ")
            password = getpass(prompt="Enter your password: ")
            sql_manager.register(username, password)
            print("Registration Successfull")
        elif command == "login":
            username = input("Enter your username: ")
            password = getpass(prompt="Enter your password: ")
            logged_user = sql_manager.login(username, password)

            if logged_user:
                logged_menu(logged_user)
            else:
                print("Login failed")
                continue

        elif command == "help":
            print("""login - for logging in!
            register - for creating new account!
            exit - for closing program!""")

        elif command == "exit":
            break

        else:
            print("Not a valid command")
            continue


def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("{}@hackabank# ".format(logged_user.get_username()))

        if command == "info":
            print("You are: " + logged_user.get_username())
            print("Your id is: " + str(logged_user.get_id()))
            print("Your balance is:" + str(logged_user.get_balance()) + "$")

        elif command == "changepass":
            new_pass = input("Enter your new password: ")
            sql_manager.change_pass(new_pass, logged_user)

        elif command == "change-message":
            new_message = input("Enter your new message: ")
            sql_manager.change_message(new_message, logged_user)

        elif command == "show-message":
            print(logged_user.get_message())

        elif command == "help":
            print("info - for showing account info")
            print("changepass - for changing passowrd")
            print("change-message - for changing users message")
            print("show-message - for showing users message")
        elif command in EXIT_CMD:
            break
        else:
            print("Not such a command!")
            continue
