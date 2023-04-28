from abc import ABC, abstractmethod


class View(ABC):
    @abstractmethod
    def __init__(self):
        self.__presenter = None

    @abstractmethod
    def set_presenter(self, presenter):
        """презентер"""

    @abstractmethod
    def start(self):
        """Запуск"""

    @abstractmethod
    def message(self, text):
        """Вывод сообщения"""

    @abstractmethod
    def show_notes(self):
        """записи"""

    @abstractmethod
    def add_note(self):
        """+ запись"""

    @abstractmethod
    def exit(self):
        """Выход"""

    @abstractmethod
    def edit_note(self):
        """редактирование заметки"""

    @abstractmethod
    def delete_note(self):
        """Удаление"""

    @abstractmethod
    def save_notes(self):
        """Сохранить"""

    @abstractmethod
    def date_selection(self):
        """заметки по дате"""

    @abstractmethod
    def show_note(self):
        """заметку по номеру"""