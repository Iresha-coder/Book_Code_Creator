cho = input("""How are you getting the names of the books?
By:
\t1.Typing in the books names manually
\t\t  or
\t2.Reading from a file
:""")

if cho == "1":
    number_of_books = int(
        input("Enter the number of books' names you want to type: "))
    for i in range(1, number_of_books + 1):
        book_name = input("Enter the book name: ")
        print(book_name[0] + str(len(book_name) - 1))
    print("Ended operation...")
elif cho == "2":
    file_name = input("Enter the name of the file with the path: ")
    file = open(file_name, "r")
    for i in file.readlines():
        code = i[0] + str(len(i) - 1)
        print(code)
    print("Ended operation...")
