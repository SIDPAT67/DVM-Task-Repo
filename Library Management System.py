
import sys
from openpyxl import Workbook, load_workbook
from tabulate import tabulate

loggedin_user = None

class Book():
    def __init__(self, name, isbn, author):
      self.name = name
      self.isbn = isbn
      self.author = author
      self.borrowed = False

    def borrow_book(self):
      if self.borrowed:
            return False
      self.borrowed = True
      return True

    def return_book(self):
      if not self.borrowed:
            return False
      self.borrowed = False
      return True

class Library:
      def __init__(self):
            self.availablebooks = {}

      def display_availableBooks(self):
                  
                   print("|THE BOOKS AVAILABLE ARE: |")
                   
                   books = []
                   for book in self.availablebooks.values():
                         if not book.borrowed:
                              books.append([book.name, book.isbn, book.author])
                   print(tabulate(books))
   
      def lendBook(self,requestedBook):
            if requestedBook in self.availablebooks:
                  if self.availablebooks[requestedBook].borrow_book():
                        print("BOOK ISSUED : THANK YOU, KEEP IT WITH CARE")
                  else:
                        print("Sorry the book you have requested has already been borrowed by someone else.")
            else:
                  print("Sorry the book you have requested is not in the library.")
                  
      def addBook(self,returnedBook):
            if returnedBook not in self.availablebooks:
                  print("Invalid input.")
                  return

            if self.availablebooks[returnedBook].return_book():
                  print("Thanks for returning your borrowed book.")
            else:
                  print("This book has already been returned.")

      def populate_books(self):
            wb = load_workbook("excel_2.xlsx")
            header = True
            for row in wb["One"]:
                  if header:
                        header = False
                        continue

                  name = row[0].value
                  self.availablebooks[row[0].value] = Book(row[0].value, row[1].value, row[2].value)
                  pass

            pass
            
class Student:
      def requestBook(self):
            print("Enter the name of the book you'd like to borrow: ")
            self.book=input()
            return self.book

      def returnBook(self):
            print("Enter the name of the book you'd like to return: ")
            self.book=input()
            return self.book
      def process_input(self, library):
            while True:
                  print("__________________________________")
                  print("|          Student MENU          |")
                  print("|________________________________|")
                  print("|1. Display all available books  |")     
                  print("|2. Request a book               |")
                  print("|3. Return a book                |")
                  print("|4. Exit                         |")
                  print("|________________________________|")
                        
                  choice=int(input("Enter Choice:"))
                  if choice==1:
                        library.display_availableBooks()
                  elif choice==2:
                        library.lendBook(self.requestBook())
                  elif choice==3:
                        library.addBook(self.returnBook())
                  elif choice==4:
                        return

class librarian:
      def addBook(self, library, name, isbn, author):
            library.availablebooks[name] =  Book(name, isbn, author)

      def removeBook(self, library, name):
            del library.availablebooks[name]

      def process_input(self, library):      
            while True:
                  print("____________________________________________")
                  print("|          LIBRARIAN MENU                  |")
                  print("|__________________________________________|")
                  print("|1. Display all available books            |")     
                  print("|2. Add a book to the library catalogue    |")
                  print("|3. Remove a book to the library catalogue |")
                  print("|4. Exit                                   |")
                  print("|__________________________________________|")
                        
                  choice=int(input("Enter Choice:"))
                  if choice==1:
                        library.display_availableBooks()
                  elif choice==2:
                        name = input("Enter book name: ")
                        isbn = input("Enter book isbn: ")
                        author = input("Enter book author: ")
                        self.addBook(library, name, isbn, author)
                        print(name + "has been added to the library.")
                  elif choice==3:
                        self.removeBook (library, input("Enter name of the book to remove: "))
                        print(name + "has been removed from the library.")
                  elif choice == 4:
                        return

def login():
      print("________________")
      print("| Login Portal |")
      print("|______________|")
      print("|1) Student    |")
      print("|2) Librarian  |")
      print("|______________|")

      choice=int(input("Enter Choice:"))
      if choice==1:
            stud_id = input("Enter Student Id: ")
            print("Welcome User, You are logged in.")

            return Student()
      elif choice==2:
            while True:
                  lib_id = input("Enter Id No.: ")
                  password = input("Enter Password: ")
                  if lib_id == "Sam@1234" and password == "1234":
                        print("Welcome, You are logged in as Sam.")
                        return librarian()
                        
                  else:
                        print("Incorrect Id or Password please try again.")  

def main():            
      library=Library()
      library.populate_books()
      student=login() 
      student.process_input(library)
      
            

                  
main()
