from note_object.note import Note


class Note_builder:

    def build_new_note(self, name, head, body, book_name):
        new_note = Note()
        new_note.set_new_note(name, head, body, book_name)
        return new_note

    def edit_note(self, note, head, body):
        note.set_head_without(head)
        note.set_body_without(body)
        return note

    def read_str_to_note(string, filename):
        info_list = []
        text = string[2:-2]
        i = 0

        for splited in text.split("\n"):

            if i < 7:
                max_splited = splited[:-1].split(": ")
                i += 1

            else:
                max_splited = splited.split(": ")

            info_list.append(max_splited[1])
        new_note = Note()
        new_note.set_old_note(filename[:-5], info_list[0], info_list[1], info_list[2],
                              info_list[3], info_list[4], info_list[5], info_list[6], info_list[7])
        return new_note
