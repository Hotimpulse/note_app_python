import datetime
from tkinter import filedialog
import uuid
from note import Note
import csv, json, time, random, string
class Note_Controller:

    def __init__(self):
        self.notes = {};

    def generateId(self):
        rand_id = str(uuid.uuid4());
        return rand_id;

    def add_note(self, note_id, note_head, note_text):
        if note_id in self.notes:
            print("This note id already exists.")
        else:
            self.notes[note_id] = Note(note_id, note_head, note_text);
            print("Note added successfully!");
 
    def delete_note(self, note_id):
        note_id = input("Enter note id to remove it: ")
        if note_id in self.notes:
            del self.notes[note_id]
            print("Note deleted!")
        else:
            print("This id isn't in the note list.")
            True;

    def view_notes(self, note_id, note_head):
        if note_id in self.notes:
            for note_id in self.notes:
                print(str(note_id), self.notes[note_id].note_head, self.notes[note_id].note_text)
        elif self.notes == {}:
            print("Your notes list is empty. Try adding a note with #1.")
        else:
            print("Your note isn't here. Try a different ID.")

    def edit_note(self, note_id, note_head, note_text):
        if note_id in self.notes:
            # if note_id == input:
            note_head = input("Edit title for the note: ")
            self.notes[note_id].note_head = note_head
            note_text = input("Edit text for the note: ")
            self.notes[note_id].note_text = note_text
            print("Note updated!")
        
    def export_note(self, note_id, note_head, note_text):
        file_path = './note_app_file'
        format = input("Pick your format by typing `json` or `csv` in this field: ")
        if format == 'csv':
            with open (file_path + ".csv", 'a', newline='') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(['id', 'title', 'body']) #, 'creation_date', 'creation_time', 'last_edit_date', 'last_edit_time'
                for note_id in self.notes:
                    writer.writerow([str(note_id), self.notes[note_id].note_head, self.notes[note_id].note_text]) #, note.creation_date, note.creation_time, note.last_edit_date, note.last_edit_time
            print("Check the note_app_file in the app directory.")
        elif format == 'json':
            notes_list = [note.__dict__ for note in self.notes.items()]
            with open(file_path + ".json", 'w') as file2:
                json.dump(notes_list, file2)
            print("Check the note_app_file in the app directory.")
        else:
            print("This isn't the right format. Try again.")

    def import_notes(self):
        file_format = input("Enter file format (csv/json): ")
        if file_format == 'csv':
            file_types = (("Comma Separated Values", "*.csv"), ("all files", "*.*"))
        elif file_format == 'json':
            file_types = (("JSON", "*.json"), ("all files", "*.*"))
        else:
            print("Invalid file format")

        file_path = filedialog.askopenfilename(initialdir='/', title='Select file', filetypes=file_types)
        if file_path == '':
            print("No file selected")

        if file_format == 'csv':
            with open(file_path, "r") as file:
                reader = csv.reader(file, delimiter=';')
                next(reader)  # skip the header row
                # self.notes = [{"id": row[0], "title": row[1], "body": row[2]} for row in reader]
                with open(file_path, 'a') as file:
                    writer = csv.writer(file, delimiter=';')
                    for note_id in list(self.notes):
                        writer.writerow([str(note_id), self.notes[note_id].note_head, self.notes[note_id].note_text]) #, note.creation_date, note.creation_time, note.last_edit_date, note.last_edit_time

            print("Notes successfully imported from your csv file.")
        elif file_format == 'json':
            self.import_notes_from_json(file_path)

        else:
            print("Invalid file format")


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
            print("5. Export notes via csv/json")
            print("6. Import notes with csv/json files")
            print("0. To exit.")
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
                    self.view_notes(note_id, note_head)
                continue

            elif (user_pick == '4'):
                if self.notes == {}:
                    print("There are no notes in your app yet! Create one with option #1")
                else: 
                    note_id = input("Enter the ID of the note: ")
                    if note_id in self.notes:
                        self.edit_note(note_id, note_head, note_text);
                    else:
                        print("Note id isn't in the list. Try again.")
                    continue

            elif (user_pick == '5'):
                if self.notes == {}:
                    print("There are no notes in your app yet! Create one with option #1")
                else:
                    self.export_note(note_id, note_head, note_text);
                    continue

            elif (user_pick == '6'):
                self.import_notes();
                continue

            elif (user_pick == '0' or 'q'):
                break

            else:
                print("This isn't a choice from the menu. Select a different option.");
                continue