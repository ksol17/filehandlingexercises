def read_books(filename):
    try:
        with open(filename, 'r') as file:
            books = {}
            for line in file:
                title, author, copies = line.strip().split(',')
                books[title] = {'author': author, 'copies': int(copies)}
            return books
    except FileNotFoundError:
        return {}
    

def add_book(books):
    title = input("Enter book title: ")
    if title in books:
        print("Book already exists.")
    else:
        author = input("Enter author's name: ")
        copies = int(input("Enter number of copies: "))
        books[title] = {'author': author, 'copies': copies}

def update_books(books):
    title = input("Enter book title: ")
    if title not in books:
        print("Book not found.")
    else:
        copies = int(input("Enter new number of copies: "))
        books[title]['copies'] = copies

def display_books(books):
   for title, info in books.items():
       print(f"Title: {title}, Author: {info['author']}, Copies: {info['copies']}")

def check_availability(books):
    title = input("Enter book title to check: ")
    if title in books:
        info = books[title]
        print(f"Title: {title}, Author: {info['author']}, Copies: {info['copies']}")
    else:
        print("Book not found.")



def write_books(filename, books):
    with open(filename, 'w') as file:
        for title, info in books.items():
            file.write(f"{title}, {info['author']}, {info['copies']}\n")




def main():
    books = read_books('library_books.txt')

    while True:
        print("\n1. Add a Book\n2. Update a Book\n3. Display Books\n4. Check Book Availability\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book(books)
        elif choice == '2':
            update_books(books)
        elif choice == '3':
            display_books(books)
        elif choice == '4':
            check_availability(books)
        elif choice == '5':
            break
        else:
            print("Invalid choice.")
        
        write_books('library_books.txt', books)


if __name__ == "__main__":
    main()