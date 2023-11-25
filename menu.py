import sys

from diarybook import Diary, DiaryBook
from util import read_from_json_into_application

class Menu:
    def __init__(self):
        self.users = {}  # Dictionary to store user accounts

    def register_or_login(self):
        choice = input("1. Register\n2. Login\nEnter your choice: ")
        if choice == '1':
            self.register_user()
        elif choice == '2':
            self.login_user()
        else:
            print("Invalid choice.")

    def register_user(self):
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        self.users[username] = User(username, password)

    def login_user(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username in self.users and self.users[username].password == password:
            self.diarybook = self.users[username].diarybook
            print(f"Welcome, {username}!")
        else:
            print("Invalid username or password.")
    def __init__(self):
        self.diarybook = DiaryBook()

        self.choices = {
            "1": self.show_diaries,
            "2": self.add_diary,
            "3": self.search_diaries,
            "4": self.populate_database,
            "5":self.quit
        }

    def display_menu(self):
        print(""" 
                     Notebook Menu  
                    1. Show diaries
                    2. Add diary
                    3. Search diaries
                    4. Populate database
                    5. Quit program
                    """)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))
                
    def show_diaries(self, diaries=None, sort_by='id'):
        if not diaries:
            diaries = self.diarybook.diaries
    
        if sort_by == 'id':
            diaries = sorted(diaries, key=lambda x: x.id)
        elif sort_by == 'memo':
            diaries = sorted(diaries, key=lambda x: x.memo)
    
        for diary in diaries:
            print(f"{diary.id}-{diary.memo}")         
    def add_diary(self):
        memo = input("Enter a memo:         ")
        tags = input("add tags:             ")
        self.diarybook.new_diary(memo, tags)
        print("Your note has been added")

    def search_diaries(self):

        filter_text = input("Search for:  ")
        diaries = self.diarybook.search_diary(filter_text)
        for diary in diaries:
            print(f"{diary.id}-{diary.memo}")
            
    def quit(self):

        print("Thank you for using diarybook today")
        sys.exit(0)

    def populate_database(self):
        if not self.diarybook:
            print("Please log in or register first.")
            return
    
        diaries1 = read_from_json_into_application('data.json')
        for diary in diaries1:
            self.diarybook.diaries.append(diary)
            diary.user = self.diarybook 


if __name__ == "__main__":
    Menu().run()