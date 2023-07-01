


preload=f"""\n

┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                   Library Management Program                                                                        │
│    this is library management program                                                                               │
│    that is updated version of first library management program.                                                     │
│    Updates: Sqlite3 database is removed, so user should not need to install sqlite3.                                │
│    Instead, user can save books and clients in seperate files and call them.                                        │
│                                                                                                                     │
│    Structure: "Library_Management_July" runs the main program. sample_books.py loads sample book list.              │
│    client.txt is sample list of clients.                                                                            │
│    books.txt can be used to save books or you can choose any file name.                                             │
│    Menu text contains menu text. This is written seperately to                                                      │
│   make main code easier to read. And this is preload text of program.                                               │
│                                                                                                                     │
│    how program works: when program starts, it wants you load books.txt (or your file name contains books).          │
│    After you load it,                                                                                               │
│    library will ask you load clients records. so as long as you save file ,                                         │
│    you will not lose previous records. After you load client                                                        │
│    list you will see the main menu. you can borrow book, see client records,                                        │
│    save and load options. Pass day is quite special function                                                        │
│    which brings the books library automatically at the end of the borrow time.                                      │
│    You can quit program by using menu.                                                                              │
│                                                                                                                     │
│    Issues: Program is still in developing process and have issues:                                                  │
│    At the beginning if user choose clienlist instead of books, program will                                         │  
│    crash, so need to add error handling. If user runs program in python IDE, interface should be extended.          │
│    There is not such problem if user                                                                                │  
│    run programs at console. Program uses modified console if user wants to see old time terminal effect,            │
│    he/she can play with terminal properities.                                                                       │
│    Further ideas and plan: Program simulates old time terminals. However it is possible to use colorama or other    │ 
│    console modules to provide with better                                                                           │
│    console experience.                                                                                              │
│    A tkinter GUI can be added to program. (next version of this program will come with tkinter GUI).                │
│    Further ideas will be updated.                                                                                   │  
│                                                                                                                     │ 
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
    you want to run the program ?(y/n) 
"""



