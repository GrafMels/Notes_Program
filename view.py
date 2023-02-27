import os
import time
from note_book_buider import Note_book_builder
from note_book import Note_book
from note_builder import Note_builder
from note import Note


class View:
    def start_loading():
        list_note_books = []
        i = 0
        for fouldername in os.listdir("notes_books"):
            new_build = Note_book_builder(fouldername)
            for filename in os.listdir(str("notes_books/{0}".format(fouldername))):
                with open(os.path.join(str("notes_books/{0}".format(fouldername)), filename), 'r', encoding='utf-8') as f:
                    new_build.add_new_note(
                        Note_builder.read_str_to_note(f.read(), filename))
            list_note_books.append(new_build.build_note_book())
            i += 1
        return list_note_books
    
    def function_selection():
        os.system('CLS')
        function_selection = input("Выберете команду и введите соответсвующую цифру:\n1. Добавить новую книгу заметок\n2. Сохранить всё\n3. Открыть книгу\n0. Выход\n")
        return function_selection
     
    def wrong_input(string):
        os.system('CLS')
        print(f"!!!\nНекорректный ввод. Введите цифры представленные ниже.\n{string}\n!!!!\n")
        time.sleep(3)
        
    def choice_book_name():
        os.system('CLS')
        function_selection = input("Придумайте имя книги: ")
        return function_selection
    
    def save_all(book_list):
        for book in book_list:
            if not os.path.exists("notes_books/{0}".format(book[0])):
                os.mkdir("notes_books/{0}".format(book[0]))
            for note in book[1].get_all_notes():
                if not os.path.exists("notes_books/{0}/{1}.json".format(book[0], note.get_name())):
                    new_note = open("notes_books/{0}/{1}.json".format(book[0], note.get_name()), "w")
                    new_note.write(str(note))
                    new_note.close()