import uuid
from note import Note
import csv, json, time, random, string
class Note_Controller:

    #instantiating the class with this method

    def __init__(self):
        self.notes = {};

    # id generator based on random 
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
            del self.notes[note_id];
        else:
            print("This id isn't in the note list.")
            True;

    def show_notes(self):
        print(list(str(self.notes)))

    def edit_note(self):
        pass;

    def export_note(self):
        pass;

    def run(self):
        while True:

            print("***Welcome to the Note-Taker 3000***");
            print();
            print("Choose your option by typing in a number:")
            print("1. Create a new note")
            print("2. Delete a note")
            print("3. Show all notes")
            print("4. Edit note")
            print("5. Export notes via csv/json")
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
                True;

            elif (user_pick == '2'):
                self.delete_note(note_id);

            elif (user_pick == '3'):
                self.show_notes();

            elif (user_pick == '4'):
                self.edit_note();

            elif (user_pick == '5'):
                self.export_note;

            elif (user_pick == '0'):
                break;

            else:
                print("This isn't a choice from the menu. Select a different option.");
                True;