from mvc.model import Model
from mvc.view import View


class Controller:
    def start():
        note_book = View.start_loading()
        bool_exit = False
        model = Model()
        model.load_books(note_book)

        while bool_exit == False:
            bool_exit = model.repeating_books_function()
