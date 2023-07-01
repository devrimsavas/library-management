from sample_books import sample_books
import os
from datetime import datetime
import time
from menu_text import menu_text
from preload import preload

#BOOK CLASS
class Book:
    def  __init__(self,title,author,ISBN,amount):
        self.title=title
        self.author=author
        self.ISBN=ISBN
        self.amount=amount

    def  __str__(self):
        return f'{self.title} {self.author} {self.ISBN} {self.amount}\n\n'

#CLASS LIBRARY
class Library:
    def  __init__(self,library_name):
        self.library_name=library_name #library name
        self.list_books_in_library=[] #books in the library
        self.list_of_borrowed_books=[] #borrowed books 
        self.client_list=[] #clients 

    def display_books_in_library(self): #Display Books in the library
        now=datetime.now()
        formatted_datetime=now.strftime("%H:%M:%S  %d-%m-%Y")
        self.list_books_in_library.sort(key=lambda book:book.title) #sort the books alphabeticaly
        display_books_text=""
        counter=0
        for book in self.list_books_in_library:
            counter+=1
            display_books_text+=f'│{counter:3}│-{book.title:45}│{book.author:25}│{book.ISBN:20}│{book.amount:5}  │\n├---------------------------------------------------------------------------------------------------------┤\n'

        #Prepare Books List  
        display_books_text=display_books_text[:-1]
        title_text=f'\n             {self.library_name} AVAILABLE BOOKS: TIME & DATE :{formatted_datetime}'
        header_0="┌─────────────────────────────────────────────────────────────────────────────────────────────────────────┐"
        header="│No.|Book Name                                     │Author                   │ISBN                │AMOUNT │"
        between_text="├─────────────────────────────────────────────────────────────────────────────────────────────────────────┤"
        last_text="└─────────────────────────────────────────────────────────────────────────────────────────────────────────┘"

        #print Books
        print(title_text)
        print(header_0)
        print(header)
        print(between_text)
        print(display_books_text)
        print(last_text)

    def display_borrowed_books(self): #Display Borrowed Books
        display_borrowed_books_text=""
        counter=0
        for book in self.list_of_borrowed_books:
            counter+=1
            display_borrowed_books_text+=f'│{counter:3}│{book[0]:45}│{book[1]:21}│{book[2]:5}          │\n├───────────────────────────────────────────────────────────────────────────────────────┤\n'
        header_0="┌───────────────────────────────────────────────────────────────────────────────────────┐"  
            
        header="│No.│Book Name                                    │Client Name          │Duration (days)│"

        between_text="├───────────────────────────────────────────────────────────────────────────────────────┤"
        last_text="└───────────────────────────────────────────────────────────────────────────────────────┘"
        #Display Borrowed Books
        display_borrowed_books_text=display_borrowed_books_text[:-1]
        print(header_0)
        print(header)
        print(between_text)
        print(display_borrowed_books_text)
        print(last_text)

    def add_new_book_to_library(self,book):
        for existing_book in self.list_books_in_library:
            if existing_book.title==book.title and existing_book.author==book.author and existing_book.ISBN==book.ISBN:
                print(f'This Book {book.title} by {book.author} is already in the library')
                existing_book.amount+=1
                print(f'The amount of the book {book.title}: {existing_book.amount}')
                return
        self.list_books_in_library.append(book)
        print(f'The Book "{book.title}" by {book.author} has been added to the library')

    def remove_a_book_from_library(self,book):
        if book not in self.list_books_in_library:
            print('this book does not in the library')
            return
        else:
            self.list_books_in_library.remove(book)
            print(f'the book : {book.title} removed from library')

    def borrow_a_book(self,book,client_borrowed,borrow_duration):
        if book not in self.list_books_in_library:
            print('This book is not in the library')
            return 
        elif book.amount==0:
            print ('All copies of this books borrowed')
            return
        else:
            book.amount-=1
            self.list_of_borrowed_books.append((book.title,client_borrowed,borrow_duration))
            #self.list_books_in_library.remove(book)

    def return_book_to_library(self,duration_passed=0):
        books_to_return=[]
        updated_borrowed_books=[]

        for book_tuple in self.list_of_borrowed_books:
            book,client_borrowed,borrow_duration=book_tuple
            borrow_duration-=duration_passed
            if borrow_duration<=0:
                print(f' {book} duration is over')
                books_to_return.append(book_tuple)
            #Find the book object in the list_books_in_library
                for book_obj in self.list_books_in_library:
                    if book_obj.title==book:
                        book_obj.amount+=1
                        break
            else:
                updated_borrowed_books.append((book,client_borrowed,borrow_duration))

        for book_tuple in books_to_return:
            self.list_of_borrowed_books.remove(book_tuple)
        self.list_of_borrowed_books=updated_borrowed_books

    def client_add(self,date,client_borrowed,client_borrowed_book,client_email,client_tel):
        client_data=[date,client_borrowed,client_borrowed_book,client_email,client_tel]
        self.client_list.append((client_data))

    def show_clients_info(self):
        text_client=""
        counter=0
        for client in self.client_list:
            counter+=1
            text_client+=f'│{counter:3}│{client[0]:16}│{client[1]:43}│{client[2]:45}│{client[3]:25}│{client[4]:17}│\n├──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤\n'

        header_0="┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐"
        
        header="│No.│DATE            │CLIENT NAME                                │BORROWED BOOK                                │CLIENT EMAIL             │CLIENT TEL       │"
        
        last_text="└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘"
        between_text="├──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤"

        text_client=text_client[:-1]
        print(header_0)
        print(header)
        print(between_text)
        print(text_client)
        print(last_text)
        
#----------END OF CLASS DEFINITION---------------

def add_start_books(library): #Library opened and has some books in the inventory
    for book in sample_books:
        library.add_new_book_to_library(Book(*book))

def add_new_book(library):  #Library add new books to inventory
    new_book_title=input('Book Title ? : ')
    new_book_writer=input('The Author ? :')
    new_book_ISBN=input('ISBN Number ? :')
    new_book_amount=int(input('How many copies ?: '))

    new_book_text=f"""┌─────────────────────────────────────────────────┐
│Book Title:{new_book_title:35}   │
│Book Writer:{new_book_writer:25}            │
│Book ISBN:{new_book_ISBN:25}              │
│Book Amount: {new_book_amount:25}           │
└─────────────────────────────────────────────────┘"""
    print(new_book_text)
    new_book_entry_confirmation=input('do you want to register this book ? (y/n')
    if new_book_entry_confirmation=='y':
        new_book=Book(new_book_title,new_book_writer,new_book_ISBN,new_book_amount)
        if new_book.title in library.list_books_in_library: # this line need to change later
            print('this book already in the library')
            return
        else:
            library.add_new_book_to_library(new_book)
            print(f' {new_book_title} is registered to the library')
            time.sleep(2)
            clear_screen()
            return
    elif new_book_entry_confirmation=='n':
        return

def remove_a_book_from_library(library):
    library.display_books_in_library()
    book_to_remove_index=int(input('Which book to remove ? 0 for main menu'))
    if book_to_remove_index==0:
        return
    library.remove_a_book_from_library(library.list_books_in_library[book_to_remove_index-1])

def borrow_a_book(library):
    library.display_books_in_library()
    now=datetime.now()
    formatted_time=now.strftime("%H:%M:%S")
    formatted_date=now.strftime("%d-%m-%Y")
    while True:
        try:
            index_book_to_borrow=int(input('Book number ?:  '))
            if index_book_to_borrow<1 or index_book_to_borrow>len(library.list_books_in_library):
                raise ValueError
            break
        except ValueError:
            print('invalid selection integer between 1-{len(library.list_book_in_library}')
    who_want_to_borrow=input('Client Name     ')
    borrow_duration=int(input('Duration ?   '))
    client_email=input('Clients Email ? ')
    client_tel=input('Client Tel' )

    library.client_add(formatted_date,who_want_to_borrow,library.list_books_in_library[index_book_to_borrow-1].title,client_email,client_tel)
    library.borrow_a_book(library.list_books_in_library[index_book_to_borrow-1],who_want_to_borrow,borrow_duration)

def display_borrowed_books(library):
    library.display_borrowed_books()

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')
    return 
    
def save_books_to_file(library):
    file_name=input('Enter a file name 0 for cancel')
    if file_name=='0':
        return
    file_name=file_name+'.txt'
    with open(file_name, 'w', encoding='utf-8') as save_file:
        library.list_books_in_library.sort(key=lambda book: book.title)
        for book in library.list_books_in_library:
            save_file.write(f'{book.title}|{book.author}|{book.ISBN}|{book.amount}|\n')
            print(str(book))
    save_file.close()

def save_clients_to_file(library):
    file_name=input('Enter a file name 0 for cancel')
    if file_name=='0':
        return
    with open(file_name,'w', encoding='utf-8') as save_client_file:
        #library.client_list.sort(key=lambda client:client.name)
        for client in library.client_list:
            save_client_file.write(f'{client[0]:16}│{client[1]:43}│{client[2]:45}│{client[3]:25}│{client[4]:17}│\n')
            print(str(client))
    save_client_file.close()
        #date,client_borrowed,client_borrowed_book,client_email,client_tel

def load_books_from_file(library):
    del library.list_books_in_library
    library.list_books_in_library=[]
    directory = os.getcwd()
    
    txt_files = [file for file in os.listdir(directory) if file.endswith('.txt')]
    print('Available Files:\n')
    for i, file_name in enumerate(txt_files):
        print(f'    {i+1}. {file_name}\n')
    file_index=int(input('Enter the Index of the file to load:  '))

    if file_index==0:
        return
    file_name =txt_files[file_index-1]

    with open(file_name, 'r', encoding='utf-8') as load_file:
        for line in load_file:
            # Remove any trailing '|' characters from the line
            line = line.rstrip('|')
            # Split the line into fields using the '|' character as the delimiter
            fields = line.split('|')
            # Create a new Book object and add it to the list_books_in_library list
            book = Book(fields[0], fields[1], fields[2], int(fields[3]))
            library.list_books_in_library.append(book)
    load_file.close()
    library.display_books_in_library()
    
def load_clients_from_file(library):
    del library.client_list
    library.client_list=[]
    directory = os.getcwd()
    
    txt_files = [file for file in os.listdir(directory) if file.endswith('.txt')]
    print(f'Available Files:')
    for i, file_name in enumerate(txt_files):
        print(f'{i+1}. {file_name}')
    file_index=int(input(f' Enter the Index of the file to load:  '))

    if file_index==0:
        return
    file_name =txt_files[file_index-1]
    
    if file_name=='0':
        return
    with open(file_name, 'r', encoding='utf-8') as load_file:
        for line in load_file:
            line=line.rstrip('│')
            fields=line.split('│')
            library.client_list.append(fields)

    load_file.close()
    
    library.show_clients_info()
    
def show_client_record(library):
    library.show_clients_info()

def quit_program():
    clear_screen()
    ask_to_quit=input("""
┌──────────────────────────────────┐
│    Are you sure to Quit ? (y/n)  │ 
├──────────────────────────────────┤
└──────────────────────────────────┘""")
    if ask_to_quit=='y':
        return True 

    elif ask_to_quit=='n':
        return False 
    else:
        print('invalid option just y or no')
        return False  
        
#------------END ROUTINES------------------

#------------LIBRARY INIT------------------

#load intro and explanation

intro=input(preload).strip()
if intro=='y':
    clear_screen()
    pass
elif intro=='n':
    raise SystemExit
else:
    print("invalid selection just y or n")
    
    


my_library=Library('Fantasy Library') #library name
duration=0  #set duration

print(f'\t\t LOADING BOOKS') 
load_books_from_file(my_library)
print('\t\tLOADING CLIENT LIST')
load_clients_from_file(my_library)
clear_screen()



menu=menu_text

#---------MAIN LOOP-----------------------------
while True:
    print(menu)
    user_choice = input('selection: ').strip()
    
    if user_choice=='1':

        clear_screen()
        my_library.display_books_in_library()
    
    elif user_choice=='2':
        clear_screen()
        add_new_book(my_library)

    elif user_choice=='3':
        clear_screen()
        remove_a_book_from_library(my_library)
        clear_screen()

    elif user_choice=='4':
        clear_screen()
        borrow_a_book(my_library)

    elif user_choice=='5':
        clear_screen()
        my_library.display_borrowed_books()

    elif user_choice=='6':
        clear_screen()
        my_library.display_books_in_library()
        my_library.display_borrowed_books()
        duration+=1
        my_library.return_book_to_library(1)

    elif user_choice=='7':
        save_books_to_file(my_library)

    elif user_choice=='8':
        clear_screen()
        show_client_record(my_library)

    elif user_choice=='9':
        clear_screen()

    elif user_choice=='10':
        if quit_program():
            break
        else:
            clear_screen()


    elif user_choice=='11':
        add_start_books(my_library)

    elif user_choice=='12':
        load_books_from_file(my_library)

    elif user_choice=='13':
        save_clients_to_file(my_library)

    elif user_choice=='14':
        load_clients_from_file(my_library)
 
    else:
        print ('Invalid Selection')

#END OF MAIN LOOP

    
    
        
        

            
        

    
        


        
