import time_manager


class Note:
    __name = "404"
    __id = "404"
    __body = "404"
    __head = "404"
    __creation_Date = "404"
    __creation_Time = "404"
    __changed_Date = "404"
    __changed_Time = "404"
    __book_name = "404"

    def set_old_note(self, name, id, body, head, creation_Date, creation_Time, changed_Date, changed_Time, book_name):
        self.__name = name
        self.__id = id
        self.__body = body
        self.__head = head
        self.__changed_Date = changed_Date
        self.__changed_Time = changed_Time
        self.__creation_Date = creation_Date
        self.__creation_Time = creation_Time
        self.__book_name = book_name

    def set_new_note(self, name, id, body, head, book_name):
        self.__name = name
        self.__id = id
        self.__body = body
        self.__head = head
        self.__creation_Time = time_manager.get_now_time()
        self.__creation_Date = time_manager.get_now_date()
        self.__changed_Date = "Не_изменялся"
        self.__changed_Time = "Не_изменялся"
        self.__book_name = book_name
        
    def set_name(self, name):
        self.__changed_Time = time_manager.get_now_time()
        self.__changed_Date = time_manager.get_now_date()
        self.__name = name

    def get_name(self):
        return self.__name
     
    def set_id(self, id):
        self.__changed_Time = time_manager.get_now_time()
        self.__changed_Date = time_manager.get_now_date()
        self.__id = id

    def get_id(self):
        return self.__id

    def set_body(self, body):
        self.__changed_Time = time_manager.get_now_time()
        self.__changed_Date = time_manager.get_now_date()
        self.__body = body

    def get_body(self):
        return self.__body

    def set_head(self, head):
        self.__changed_Time = time_manager.get_now_time()
        self.__changed_Date = time_manager.get_now_date()
        self.__head = head

    def get_head(self):
        return self.__head
    
    def set_book_name(self, book_name):
        self.__changed_Time = time_manager.get_now_time()
        self.__changed_Date = time_manager.get_now_date()
        self.__book_name = book_name

    def get_book_name(self):
        return self.__book_name

    def __str__(self):
        return str("{{\n\"id\": {0},\n\"body\": {1},\n\"head\": {2},\n\"date of creation\": {3},\n\"time of creation\": {4},\n\"date of change\": {5},\n\"time of change\": {6},\n\"book name\": {7}\n}}".format(self.__id, self.__body, self.__head, self.__creation_Date, self.__creation_Time, self.__changed_Date, self.__changed_Time, self.__book_name))
    
    def return_deleted(self):
        return str("{0} {1} {2} {3} {4} {5} {6} {7}".format(self.__id, self.__body, self.__head, self.__creation_Date, self.__creation_Time, self.__changed_Date, self.__changed_Time, self.__book_name))