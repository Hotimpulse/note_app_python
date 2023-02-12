import datetime
from tkinter import filedialog
import uuid
from note import Note
import csv, time, string
class Note_Controller:

    def __init__(self):
        self.notes = {};

    def generateId(self):
        note_id = str(uuid.uuid4());
        return note_id

    def add_note(self, note_id, note_head, note_text):
        note_edit = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        if note_id in self.notes:
            print("This note id already exists.")
        else:
            self.notes[note_id] = Note(note_id, note_head, note_text, note_edit)
            print(f"Note added successfully at {note_edit}!")
 
    def delete_note(self, note_id):
        note_id = input("Enter note id to remove it: ")
        if note_id in self.notes:
            del self.notes[note_id]
            print("Note deleted!")
        else:
            print("This id isn't in the note list.")
            True;

    def view_notes(self, note_id):

        user_pick = input("Enter 0 to show all notes, 1 to sort them by date: ")

        notes = [(note_id, note.note_head, note.note_text, note.note_edit) for note_id, note in self.notes.items()]
        if user_pick == '0':
            for note in notes:
                print(note[0], note[1], note[2], note[3])
        elif user_pick == '1':
            notes.sort(key=lambda x: x[3], reverse=True)
            for note in notes:
                print(note[0], note[1], note[2], note[3])
        elif self.notes == {}:
                print("Your notes list is empty. Try adding a note with #1.")
        else:
            print("Your note isn't here. Try a different ID.")

    def edit_note(self, note_id, note_head, note_text, note_edit):

        if note_id in self.notes:
            # if note_id == input:
            note_head = input("Edit title for the note: ")
            self.notes[note_id].note_head = note_head
            note_text = input("Edit text for the note: ")
            self.notes[note_id].note_text = note_text
            self.notes[note_id].note_edit = note_edit
            print("Note updated!")
        
    def export_note(self):

        file_path = './note_app_file'

        with open (file_path + ".csv", 'w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['id', 'title', 'body']) #, 'creation_date', 'creation_time', 'last_edit_date', 'last_edit_time'
            for note_id in self.notes:
                writer.writerow([note_id, self.notes[note_id].note_head, self.notes[note_id].note_text])

        print("Check the note_app_file in the app directory.")

    def import_notes(self):
        file_types = (("Comma Separated Values", "*.csv"), ("all files", "*.*"))
        file_path = filedialog.askopenfilename(initialdir='/', title='Select file', filetypes=file_types)
        if file_path == '':
            print("No file selected")
        else:
            with open(file_path, "r") as file:
                reader = csv.reader(file, delimiter=';')
                next(reader)  # skip the header row
                for row in reader:
                    note_id = row[0]
                    note_head = row[1]
                    note_text = row[2]
                    self.add_note(note_id, note_head, note_text)
                self.view_notes(note_id)
                
            print("Notes successfully imported from your csv file.")

    def run(self):
        while True:
            print();
            print("***Welcome to the Note-Taker 3000***");
            print();
            print("Choose your option by typing in a number:")
            print("1. Add a new note")
            print("2. Delete a note")
            print("3. Show all notes")
            print("4. Edit note")
            print("5. Export notes .csv")
            print("6. Import notes .csv")
            print("0. Type 0 or q to exit.")
            print();
            print("Input a number:");
            user_pick = input()

            if (user_pick == '1'):
                note_id = self.generateId();
                print("Your note's id is: ")
                print(note_id);
                note_head = input("Enter your note's title. Press enter when you're done: ")
                note_text = input("Enter your note's text. Press enter when you're done: ")
                self.add_note(note_id, note_head, note_text);
                continue

            elif (user_pick == '2'):
                if self.notes == {}:
                    print("There are no notes in your app yet! Create one with option #1")
                else:
                    self.delete_note(note_id)
                continue

            elif (user_pick == '3'):
                if self.notes == {}:
                    print("Add a note with option #1 first!")
                else:
                    self.view_notes(note_id)
                continue

            elif (user_pick == '4'):
                if self.notes == {}:
                    print("There are no notes in your app yet! Create one with option #1")
                else: 
                    note_id = input("Enter the ID of the note: ")
                    if note_id in self.notes:
                        note_edit = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                        self.edit_note(note_id, note_head, note_text, note_edit);
                    else:
                        print("Note id isn't in the list. Try again.")
                    continue

            elif (user_pick == '5'):
                if self.notes == {}:
                    print("There are no notes in your app yet! Create one with option #1")
                else:
                    self.export_note();
                    continue

            elif (user_pick == '6'):
                self.import_notes();
                continue

            elif (user_pick == ''):
                print("This isn't a choice from the menu. Select a different option.");
                continue

            elif (user_pick == '0' or 'q'):
                break