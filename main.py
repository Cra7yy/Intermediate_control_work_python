import json
import os
from datetime import datetime

class Note:
    def __init__(self, id, title, message, timestamp):
        self.id = id
        self.title = title
        self.message = message
        self.timestamp = timestamp

class NoteApp:
    def __init__(self):
        self.notes = []
        self.file_path = "notes.json"
        self.load_notes()

    def load_notes(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                notes_data = json.load(file)
                self.notes = [Note(note['id'], note['title'], note['message'], note['timestamp']) for note in notes_data]

    def save_notes(self):
        notes_data = [{'id': note.id, 'title': note.title, 'message': note.message, 'timestamp': note.timestamp} for note in self.notes]
        with open(self.file_path, 'w') as file:
            json.dump(notes_data, file)

    def list_notes(self):
        for note in self.notes:
            print(f"{note.id}: {note.title} - {note.timestamp}")

    def add_note(self, title, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        note_id = len(self.notes) + 1
        new_note = Note(note_id, title, message, timestamp)
        self.notes.append(new_note)
        self.save_notes()
        print("Заметка успешно сохранена")

    def edit_note(self, note_id, title, message):
        for note in self.notes:
            if note.id == note_id:
                note.title = title
                note.message = message
                note.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_notes()
                print("Заметка успешно отредактирована")
                return
        print("Заметка с указанным ID не найдена")

    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note.id != note_id]
        self.save_notes()
        print("Заметка успешно удалена")

if __name__ == "__main__":
    app = NoteApp()

    while True:
        print("\nВыберите команду:")
        print("1. Показать все заметки")
        print("2. Добавить новую заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("0. Выйти")

        choice = input()

        if choice == "1":
            app.list_notes()
        elif choice == "2":
            title = input("Введите заголовок заметки: ")
            message = input("Введите тело заметки: ")
            app.add_note(title, message)
        elif choice == "3":
            note_id = int(input("Введите ID заметки для редактирования: "))
            title = input("Введите новый заголовок заметки: ")
            message = input("Введите новое тело заметки: ")
            app.edit_note(note_id, title, message)
        elif choice == "4":
            note_id = int(input("Введите ID заметки для удаления: "))
            app.delete_note(note_id)
        elif choice == "0":
            break
        else:
            print("Некорректная команда. Пожалуйста, введите снова.")
