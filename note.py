class Note:
    def __init__(self, note_id, note_text):
     self.id = note_id;
     self.text = note_text;

    def __str__(self):
       return self.text;
