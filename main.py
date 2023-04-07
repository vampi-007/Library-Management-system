#Add function this will add a book.
def add():
          _add = int(input("Enter isbn to add: "))
          bookName = input("Enter book name: ")
          price = int(input("Enter price of book: "))
          books[_add] = [bookName, price]
#Update function this will update a book info.
def update():
          _update = int(input("Enter isbn to update: "))
          bookName = input("Enter book name: ")
          price = int(input("Enter price of book: "))
          books[_update] = [bookName, price]
#Remove function this is used to remove the book from the library.      
def remove():
          _remove = int(input("Enter isbn to remove: "))
          books.pop(_remove)
          books
#Search fuction will search in the whole library for a book.
def search():
          search = int(input("enter the isbn to find the book: "))
          print(books[search])
#this fuction will print out the whole data of books.
def printAll():
          for _books in books:
            print("isbn: ", _books)
            print("book: " ,(books[_books])[0])
            print("price: " ,(books[_books])[1])
          
# books available...
books = {1234567890321 : ["English", 100],
         1234567890654 : ["Programming fundamental", 990],
         1234567890098 : ["Urdu", 780],
         1234567890123 : ["Physics", 650]}
userCommand = 0
# menu driven program...
while userCommand != "EXIT":
  userCommand = input("""Enter the following to perform actions:
                    1) Enter 'add' to add a book: 
                    2) Enter 'update' for update in books: 
                    3) Enter 'remove' to remove a book: 
                    4) Enter 'search' for searching a book: 
                    6) Enter 'print' to print all books in library: 
                    7) Enter 'exit' to exit the program: """).upper()
  if userCommand == "ADD":
          add()
  elif userCommand == "UPDATE":
          update()
  elif userCommand == "REMOVE":
          remove()
  elif userCommand == "SEARCH":
          search()
  elif userCommand == "PRINT":
          printAll()
  elif userCommand == "exit":
          break
  else:
          print("Invalid command!!")
      
