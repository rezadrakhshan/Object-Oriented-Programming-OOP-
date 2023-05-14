from note import note

class Notebook:
    note_list =[]

    def __init__(self):
        pass

    def create_note(self,memo,tags=""):
            self.note_list.append(note(memo,tags))

    def read_note(self,tag):
        for i in self.note_list:
            if i.tag == tag:
                return True
        else:
            return False
        
    def update_note(self,current_memo,new_memo):
        for i in self.note_list:
            if i.memo == current_memo:
                i.memo = new_memo
                return i.memo
        else:
            return "its not found."
        

    def delete_note(self,memo):
        for i in self.note_list:
            if i.memo == memo:
                self.note_list.remove(i)
                return True
            else:
                return False

              

Notebook = Notebook()
Notebook.create_note("snowy night","winter")
print(Notebook.delete_note("snowy night"))
print(Notebook.note_list)