import tkinter as tk
from datetime import datetime
from random import random
import re

from Diary_App.Diary import Diary

from Diary_App.Diaries import Diaries
from Diary_App.Diary import Diary


class MainDiary:
    diary = Diaries

    def __init__(self):
        self.username = ""
        self.password = ""
        self.title = ""
        self.body = ""
        self.diaryUser = 0
        self.token = ""
        self.bodyEdited = ""
        self.titleEdited = ""
        self.id = 0
        self.currentDateTime = datetime.now()
        self.diary = Diaries()
        # self.diary1 = Diary

    def main(self):
        self.welcome_menu()
        self.diary_menu()
        self.lock_diary()

    def welcome_menu(self):
        self.diaryUser = int(input("""
            HELLO! WELCOME BUDDY DIARY

            This is a Diary, not a Journal!

            1. Create new diary account

            2. Log in

            3. Exit
        """))
        if self.diaryUser == 1:
            self.create_account()
        elif self.diaryUser == 2:
            self.login()
        elif self.diaryUser == 3:
            self.exit_diary()
        else:
            exit(0)

    def exit_diary(self):
        exit_option = input("Click yes to log out or no to return to Diary menu: ")
        if exit_option.lower() == 'yes':
            print(":( Buddy Diary is closing>>>>\nGoodbye!")
            exit(0)
        elif exit_option.lower() == 'no':
            self.welcome_menu()
        else:
            self.exit_diary()

    def login(self):
        try:
            user_login = input("Enter username: ")
            user_password = input("Enter password: ")

            if self.username != user_login:
                print("Username does not exist")
                if self.password != user_password:
                    print("Invalid password")
        except Exception as error:
            print(error)
            self.welcome_menu()
        self.diary_menu()

    def diary_menu(self):
        self.diaryUser = int(input("""
            To continue, press:

            1. Lock diary
            2. Unlock diary
            3. Confirm diary is locked
            4. Create entry
            5. Delete entry
            6. Find entry by ID
            7. Find updated entry by ID
            8. Update entry
            9. Logout
        """))

        if self.diaryUser == 1:
            self.lock_diary()
        elif self.diaryUser == 2:
            self.unlock_diary()
        elif self.diaryUser == 3:
            self.is_lock_diary()
        elif self.diaryUser == 4:
            self.create_entry()
        elif self.diaryUser == 5:
            self.delete_entry()
        elif self.diaryUser == 6:
            self.find_entry_by_id()
        elif self.diaryUser == 7:
            self.find_updated_entry_by_id()
        elif self.diaryUser == 8:
            self.update_entry()
        elif self.diaryUser == 9:
            self.logout()
        else:
            exit(0)

    def logout(self):
        try:
            logout_option = input("Click yes to log out or no to return to Diary menu: ")
            if logout_option.lower() == 'yes':
                self.welcome_menu()
            elif logout_option.lower() == 'no':
                self.diary_menu()
            else:
                exit(0)

            raise ValueError
        except (ValueError, KeyboardInterrupt):
            print("Invalid details detected")
            self.logout()

    def update_entry(self):
        try:
            get_id = int(input("Enter entry ID to update: "))
            if get_id == 0:
                self.update_entry()
                raise Exception("Entry not found")
            self.diary.find_by_user_name(self.username).find_entry_by_id(get_id).get_diary_info()
            self.diary.find_by_user_name(self.username).update_entry(get_id, self.title, self.body)

            edit_title = input("Enter yes to edit title: ")
            if edit_title.lower() == "yes":
                print(self.title)
                self.titleEdited = input("Edit: ")
            else:
                self.update_entry()

            if not self.titleEdited or self.titleEdited.lower() == "no":
                self.titleEdited = self.title

            edit_body = input("Enter yes to edit body: ")
            if edit_body.lower() == "yes":
                print(self.body)
                self.bodyEdited = input("Edit: ")

            if not self.bodyEdited or self.bodyEdited.lower() == "no":
                self.bodyEdited = self.body

            print("Entry successfully updated.")

            confirm_update = int(input("Enter entry ID to see entry update: "))
            self.diary.find_by_user_name(self.username).find_entry_by_id(confirm_update).get_diary_info()
            print(
                f"Entry successfully updated with new title as: \"{self.titleEdited}\" "
                f"and new body as: \"{self.bodyEdited}\" on {self.currentDateTime}")
            self.diary_menu()

            raise ValueError
        except (ValueError, KeyboardInterrupt):
            print("Invalid details detected")
            self.update_entry()

    def find_entry_by_id(self):
        try:
            id = int(input("Enter entry ID: "))
            if id == 0:
                print("Invalid ID")
                navigate = input("Enter Yes to retry or No to go to Diary menu: ")
                if navigate.lower() == 'yes':
                    self.find_entry_by_id()
                elif navigate.lower() == 'no':
                    self.diary_menu()
            self.diary.find_by_user_name(self.username).find_entry_by_id(id).get_diary_info()
            print("Entry found")
            print(self.title)
            print(self.body)
            self.diary_menu()

            raise ValueError
        except (ValueError, KeyboardInterrupt):
            print("Invalid details detected")
            self.find_updated_entry_by_id()

    def find_updated_entry_by_id(self):
        try:
            id = int(input("Enter entry ID to see the updated version: "))
            if id == 0:
                print("Invalid ID")
                navigate = input("Enter Yes to retry or No to go to Diary menu: ")
                if navigate.lower() == 'yes':
                    self.find_entry_by_id()
                elif navigate.lower() == 'no':
                    self.diary_menu()
            self.diary.find_by_user_name(self.username).find_entry_by_id(id).get_diary_info()
            print("Entry found")
            print(self.titleEdited)
            print(self.bodyEdited)
            self.diary_menu()

            raise ValueError
        except (ValueError, KeyboardInterrupt):
            print("Invalid details detected")
            self.find_updated_entry_by_id()

    def delete_entry(self):
        try:
            id = int(input("Enter id to delete entry: "))
            if self.id != id:
                print("Invalid ID")
                self.delete_entry()
            self.diary.find_by_user_name(self.username).delete_entry(self.ID)
            confirm = input("You are about to delete this entry. Enter yes to continue: ")
            if confirm.lower() == "yes":
                print(self.title)
                print(self.body)
                print("Deleting>>>>\nEntry deleted successfully")
            elif confirm.lower() == "no":
                self.diary_menu()
            self.diary_menu()

            raise ValueError
        except (ValueError, KeyboardInterrupt):
            print("Invalid details detected")
            self.delete_entry()

    def create_entry(self):
        try:
            self.title = input("Create title: ")
            self.body = input("Write body: ")

            if not self.title or not self.body:
                raise (ValueError, KeyboardInterrupt, "Title or body must be entered")

            self.diary.find_by_user_name(self.username).create_entry(self.title, self.body)
            print(
                f"Entry successfully created with title as: \"{self.title}\" "
                f"and body as: \"{self.body}\" on {self.currentDateTime}")
            self.diary_menu()

            raise ValueError
        except (ValueError, KeyboardInterrupt):
            print("Invalid details detected")
            self.create_entry()

    def is_lock_diary(self):
        self.unlock_diary()

    def unlock_diary(self):
        try:
            security = input("Enter password: ")
            if self.password != security:
                raise Exception("Invalid password")
            # new_token = input("Enter token: ")
            else:
                print("Diary is unlocked successfully.")
            self.diary_menu()

            raise ValueError
        except (ValueError, KeyboardInterrupt):
            print("Invalid details detected")
            self.unlock_diary()

    def lock_diary(self):
        print("Diary is locked successfully")
        self.diary_menu()

    def create_account(self):
        try:
            user = input("Enter username: ")
            if user.isalpha():
                self.username = user

            security = input("Enter password: ")
            if user.isalpha():
                self.password = security

            if not user:
                print("Username cannot be blank.")
                self.create_account()

            if not security:
                print("Password cannot be blank.")
                self.create_account()

            self.diary.add_user(self.username, self.password)
            name = f"Hello {user}, your account has been created successfully. You are welcome to use your diary."
            print(name)
            self.diary_menu()

            raise ValueError
        except (ValueError, KeyboardInterrupt):
            print("Invalid details detected")
            self.create_account()




# class Diaries:
    
        # def __init__(self):
        #     self.diary = Diary
        #     self.diaries = []
        #
        # def add_user(self, username, password):
        #     diary = Diary(username, password)
        #     self.diaries.append(diary)
        #
        # def find_by_user_name(self, username):
        #     for self.diary in self.diaries:
        #         if self.diary.get_username() == username:
        #             return self.diary
        #         raise ValueError("Username not found")
        #
        # def delete(self, username, password):
        #     diary = Diary(username, password)
        #     self.diaries.remove(diary)
        #
        # def validate_username(self, username):
        #     if username in self.diary == username:
        #         raise ValueError("Username is unavailable")
        #
        # def validate_password(self, password):
        #     if not re.search("^[0-9]\\d*", password):
        #         raise (ValueError, KeyboardInterrupt, "Password must contain at least one Uppercase character")


if __name__ == "__main__":
    mainDiary = MainDiary()
    mainDiary.main()
