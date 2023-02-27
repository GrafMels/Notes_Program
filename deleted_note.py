from note import Note

class Deleted_note(Note):
    __id = "404"
    __body = "404"
    __head = "404"
    __creation_Date = "404"
    __creation_Time = "404"
    __changed_Date = "404"
    __changed_Time = "404"
    __book_name = "404"
    
    def __init__(self, unnecessary_note):
        full_note = unnecessary_note.return_deleted()
        splited_note = full_note.split()
        self.__id = splited_note[0]
        self.__body = splited_note[1]
        self.__head = splited_note[2]
        self.__creation_Date = splited_note[3]
        self.__creation_Time = splited_note[4]
        self.__changed_Date = splited_note[5]
        self.__changed_Time = splited_note[6]
        self.__book_name = splited_note[7]

    
    def restore_note():
        pass
    
    def complete_removal():
        pass
    
    def __str__(self):
        return str("{{\n\"id\": {0},\n\"body\": {1},\n\"head\": {2},\n\"date of creation\": {3},\n\"time of creation\": {4},\n\"date of change\": {5},\n\"time of change\": {6},\n\"book name\": {7}\n}}".format(self.__id, self.__body, self.__head, self.__creation_Date, self.__creation_Time, self.__changed_Date, self.__changed_Time, self.__book_name))
    