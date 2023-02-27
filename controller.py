import array
import os
from model import Model

from view import View

class Controller:
    def start():
        note_book  = View.start_loading()
        bool_exit = False
        while bool_exit == False:
            bool_exit = Model.repeating_function()
        # list = []
        # list = note_book[0].get_all_notes()
        # print(list[0])