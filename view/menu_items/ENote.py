from view.menu_items.MenuMethod import MenuMethods


class EditNote(MenuMethods):
    def description(self):
        return "Редактировать заметку"

    def run(self):
        self.get_ui().edit_note()