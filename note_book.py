import numpy as np

class Note_book:
    __notes = dict(name = '404')
    __id_number = 0
    
    def __init__(self, new_name):
        self.__notes = dict(name = '{0}'.format(new_name))
        
    def get_id(self):
        return int(self.__id_number)
    
    def get_note(self, id):
        return self.__notes.get(id)
    
    def get_name(self):
        return self.__notes.get('name')
    
    def plus_id(self):
        self.__id_number += 1
    
    def new_notes(self, note):
        self.__notes[self.__id_number] = note
        
    def get_all_notes(self):
        list_note = []
        for i in range(len(self.__notes)-1):
            list_note.append(self.__notes.get(i))
        return list_note
        
    def __str__(self):
        strings = []
        for key,item in self.__notes.items():
            strings.append("\n{}: {}\n".format(key, item))
        result = "\n".join(strings)
        return result