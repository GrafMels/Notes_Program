import os
from note_book_buider import Note_book_builder
from note_builder import Note_builder


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
