from note_book import Note_book
note_book = Note_book("404")

class Note_book_builder:
    def __init__(self, name):
        self.note_book = Note_book(name)
        self.name = name
    
    def add_new_note(self, note):
        note.set_book_name(self.name)
        note.set_id(str(self.note_book.get_id()))
        self.note_book.new_notes(note)
        self.note_book.plus_id()
    
    def build_note_book(self):
        return self.note_book
    
    def change_book(self, book):
        self.note_book = book
        
        