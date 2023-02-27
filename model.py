import os
from note_book_buider import Note_book_builder
from view import View
from note_book import Note_book 

class Model:
    book_list = []
    
    def load_books(self, note_books):
        for book in note_books:
            self.book_list.append([book.get_name(), book])
    
    def repeating_books_function(self):
        function_selection = View.function_selection()
        if function_selection == "1":
            book_name = View.choice_book_name()
            new_builder = Note_book_builder(book_name)
            self.book_list.append([book_name, new_builder.build_note_book()])
            return False
        
        elif function_selection == "2":
            
            View.save_all(self.book_list)
            return False
        
        elif function_selection == "3":
            self.repeating_books_choice()
            return False
        
        elif function_selection == "0":
            return True
        
        else:
            View.wrong_input("1,2,3,0")
            return False
    
    def repeating_books_choice(self):
        bool_choice = False
        while bool_choice == False:
            os.system('CLS')
            print("Выберете книгу и введите соответсвующую цифру:")
            i=0
            list = []
            for book in self.book_list:
                list.append(i)
                i += 1
                print("{0}. {1}".format(i, book[0]))
            print("0. Назад")
            book_selection = input()
            print(self.book_list[int(book_selection)-1][1])
            try:
                if int(book_selection) < i+1 and int(book_selection) > 0:
                    self.repeating_in_book(self.book_list[int(book_selection)-1][1])
                    bool_choice = True
                elif int(book_selection) == 0:
                    bool_choice = True
                else:          
                    View.wrong_input(list)
            except:
                bool_choice = False
    
    def repeating_in_book(self, book):
        bool_choice = False
        while bool_choice == False:
            function_selection = View.function_selection_in_book()
            if function_selection == "1":

                bool_choice = False
                
            elif function_selection == "2":
                View.save_all(self.book_list)
                bool_choice = False
            
            elif function_selection == "3":
                bool_choice = False
            
            elif function_selection == "4":
                bool_choice = False
            
            elif function_selection == "5":
                bool_choice = False
            
            elif function_selection == "0":
                bool_choice = True
            
            else:
                View.wrong_input("1,2,3,0")
                bool_choice = False