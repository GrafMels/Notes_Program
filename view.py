import os
import shutil
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
        function_selection = input("Выберете команду и введите соответсвующую цифру:\n1. Добавить новую книгу заметок\n2. Сохранить всё\n3. Открыть книгу\n4. Удалить книгу\n0. Выход\n")
        return function_selection
    
    def function_selection_in_book():
        os.system('CLS')
        function_selection = input("Выберете команду и введите соответсвующую цифру:\n1. Добавить заметку\n2. Сохранить всё\n3. Открыть заметку\n4. Отедактировать заметку\n6. Переименовать заметку\n5. Удалить заметку\n0. Выход\n")
        return str(function_selection)
     
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
                    new_note = open("notes_books/{0}/{1}.json".format(book[0], note.get_name()), "w", encoding='utf-8')
                    new_note.write(note.toString())
                    new_note.close()
    
    def note_builder_add():
        list_answer = []
        os.system('CLS')
        list_answer.append(input("Придумайте имя записки: "))
        list_answer.append(input("Придумайте оглавление записки: "))
        list_answer.append(input("Введите текст записки: "))
        return list_answer
    
    def choice_book(book_list, bool):
        output_list = []
        os.system('CLS')
        if bool == True:
            print("Выберете книгу и введите соответсвующую цифру:")
        elif bool == False:
            print("ВНИМАНИЕ!!! Книга удаляется вместе с заметками!\nВыберете книгу и введите соответсвующую цифру:")
        i=0
        list = []
        for book in book_list:
            list.append(i)
            i += 1
            print("{0}. {1}".format(i, book[0]))
        list.append(i)
        print("0. Назад")
        book_selection = input(": ")
        if bool == True:
            output_list.append(list)
            output_list.append(book_selection)
            output_list.append(i)
        elif bool == False:
            shutil.rmtree("notes_books/{0}".format(book_list[int(book_selection)-1][0]))
        return output_list
    
    def choice_note(book):
        output_list = []
        os.system('CLS')
        print("Выберете записку и введите соответсвующую цифру:")
        i=0
        list = []
        for note in book.get_all_notes():
            list.append(i)
            i += 1
            print("{0}. {1}".format(i, note.get_name()))
        list.append(i)
        print("0. Назад")
        note_selection = input()
        output_list.append(list)
        output_list.append(note_selection)
        output_list.append(i)
        return output_list

    def show_note(note):
        os.system('CLS')
        print(str(note))
        print()
        wait = input("Введите любой символ для продолжения: ")
        
    def edit_note(note):
        list_answer = []
        os.system('CLS')
        list_answer.append("\"{0}\"".format(input("Придумайте новое оглавление записки: ")))
        list_answer.append("\"{0}\"".format(input("Введите новый текст записки: ")))
        note_builder = Note_builder()
        note_builder.edit_note(note, list_answer[0], list_answer[1])
        return note
        
            
    
