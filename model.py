import cmd
import os
import sys
import time
from note_book_buider import Note_book_builder
from note_builder import Note_builder
from view import View


class Model:
    book_list = []
    bool_choice = []

    def load_books(self, note_books):
        for book in note_books:
            self.book_list.append([book.get_name(), book])

    def repeating_books_function(self):
        function_selection = View.function_selection()

        if function_selection == "1":
            book_name = View.choice_book_name()
            new_builder = Note_book_builder(book_name)
            self.book_list.append([book_name, new_builder.build_note_book()])
            View.save_all(self.book_list)
            return False

        elif function_selection == "2":
            View.save_all(self.book_list)
            return False

        elif function_selection == "3":
            bool_choice = False
            while bool_choice == False:
                bool_choice = self.repeating_books_choice()
            return False

        elif function_selection == "4":
            print("ВНИМАНИЕ")
            input_list = View.choice_book(self.book_list, False)
            del self.book_list[[int(input_list[1])-1][0]]
            return False

        elif function_selection == "0":
            return True

        else:
            View.wrong_input("[0, 1, 2, 3, 4]")
            return False

    def repeating_books_choice(self):
        input_list = View.choice_book(self.book_list, True)
        try:

            if int(input_list[1]) < input_list[2]+1 and int(input_list[1]) > 0:
                bool_choice = False
                while bool_choice == False:
                    bool_choice = self.repeating_in_book(
                        self.book_list[int(input_list[1])-1][1], int(input_list[1])-1)
                return True

            elif int(input_list[1]) == 0:
                return True

            else:
                View.wrong_input(input_list[0])
                return False

        except:
            return False

    def repeating_in_book(self, book, book_selection):
        function_selection = View.function_selection_in_book()
        note_builder = Note_builder()
        book_builder = Note_book_builder("404")
        book_builder.change_book(book)

        if function_selection == "1":
            list_answer = View.note_builder_add()
            note = note_builder.build_new_note(
                list_answer[0], list_answer[1], list_answer[2], self.book_list[book_selection][0])
            book_builder.add_new_note(note)
            self.book_list[book_selection][1] = book_builder.build_note_book()
            book = book_builder.build_note_book()
            View.save_all(self.book_list)
            return False

        elif function_selection == "2":
            View.save_all(self.book_list)
            return False

        elif function_selection == "3":
            bool_choice = False
            while bool_choice == False:
                bool_choice = self.repeating_note_choice(
                    book, 0, book_selection)
            return False

        elif function_selection == "4":
            bool_choice = False
            while bool_choice == False:
                bool_choice = self.repeating_note_choice(
                    book, 1, book_selection)
            return False

        elif function_selection == "5":
            bool_choice = False
            while bool_choice == False:
                bool_choice = self.repeating_note_choice(
                    book, 2, book_selection)
            return False

        elif function_selection == "6":
            bool_choice = False
            while bool_choice == False:
                bool_choice = self.repeating_note_choice(
                    book, 3, book_selection)
            return False

        elif function_selection == "0":
            return True

        else:
            View.wrong_input("[0, 1, 2, 3, 4, 5, 6]")
            return False

    def repeating_note_choice(self, book, func_id, book_selection):
        input_list = View.choice_note(book)

        try:
            note = book.get_note(int(input_list[1])-1)

            if int(input_list[1]) < input_list[2]+1 and int(input_list[1]) > 0:
                if func_id == 0:
                    View.show_note(note)

                elif func_id == 1:
                    self.book_list[book_selection][1].set_note(
                        int(input_list[1]), View.edit_note(note))

                elif func_id == 2:
                    old_name = self.book_list[book_selection][1].get_note(
                        int(input_list[1])-1).get_name()
                    self.book_list[book_selection][1].get_note(
                        int(input_list[1])-1).set_name(View.set_name())
                    View.delete_note(
                        self.book_list[book_selection][0], old_name)
                    View.save_all(self.book_list)

                elif func_id == 3:
                    View.delete_note(self.book_list[book_selection][0], self.book_list[book_selection][1].get_note(
                        int(input_list[1])-1).get_name())
                    book.delete_note(int(input_list[1])-1)

            elif int(input_list[1]) == 0:
                return True

            else:
                View.wrong_input(input_list[0])

        except:
            View.wrong_input(input_list[0])
