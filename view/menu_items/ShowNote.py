from view.menu_items.MenuMethod import MenuMethods


class ShowNote(MenuMethods):
    def description(self):
        return "Показать заметку"

    def run(self):
        self.get_ui().show_note()