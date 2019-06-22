'''
Bestseller Utility - compatible with Python3.x
To get it work with Python2.7.x input() needs to be changed with raw_input().
This programe expects to have a file named as "bestsellers.txt" in current directory. 
And each line in this file must be formatted as
title <tab> author <tab> publisher <tab> date <tab> category
'''
FILE_TO_LOAD="bestsellers.txt"
'''
Print a book
'''
def print_book(book):
    print("{} by {} ({})".format(book[0],book[1],book[3]))
'''
Print a book list
'''
def print_book_list(book_list):
    if(len(book_list)==0):
        print("No seach result! better luck next time.")
    for book in book_list:
        print_book(book)
'''
Serach book list based on author & return list of books matches by author
'''
def search_author(book_list, author_search_key):
    search_result = []
    for book in book_list:
        author = book[1]
        #print("Matching key {} with {}".format(author_search_key,author))
        if(author_search_key.upper() in author.upper()):
            search_result.append(book)
    return search_result

'''
Serach book list based on title & return list of books matches by title
'''
def search_title(book_list, title_search_key):
    search_result = []
    for book in book_list:
        title = book[0]
        #print("Matching key {} with {}".format(title_search_key,title))
        if(title_search_key.upper() in title.upper()):
            search_result.append(book)
    return search_result

'''
Load data set into a book list 
'''
def load_books_data():
    book_list = []
    try:
        with open(FILE_TO_LOAD) as fp: 
            line = fp.readline()
            line_number = 1
            while line:
                book = line.strip().split('\t')
                #print("Line {}: {} Book Array {}".format(line_number, len(book), book))
                #Each line must be formatted as title <tab> author <tab> publisher <tab> date <tab> category
                if(len(book) !=5):
                    print("Improper data set at line {}".format(line_number))
                    exit(1)
                book_list.append(book)
                line = fp.readline()
                line_number += 1
    except IOError:
        print ("Opps!, unable to load data set from {}".format(FILE_TO_LOAD))
        exit(1)
    print("Data set loaded successfully, total no of books {}.".format(len(book_list)))
    return book_list

'''
Print menu options
'''
def print_menu_options():
    print("\nWhat wouuld you like to do?")
    print("1 : Look up year range")
    print("2 : Look up month/year")
    print("3 : Search for author")
    print("4 : Search for title")
    print("Q : Quit")

'''
Main program starts here
'''
book_list = load_books_data()
while True:
    print_menu_options()
    option = str ( input (">") )
    if (option.upper() == "Q"):
        print("Thank you, have a nice day!")
        break
    elif (int(option) == 1):
        print("Sorry, feature not implemented yet!")
    elif (int(option) == 2):
        print("Sorry, feature not implemented yet!")
    elif (int(option) == 3):
        author_search_key = input ("Enter an author's name (or part of a name):")
        print_book_list(search_author(book_list,author_search_key))
    elif (int(option) == 4):
        title_search_key = input ("Enter a title (or part of title):")
        print_book_list(search_title(book_list,title_search_key))