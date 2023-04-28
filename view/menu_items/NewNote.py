from view.menu_items.MenuMethod import MenuMethods


class AddNote(MenuMethods):
    def description(self):
        return "+ запись"

    def run(self):
        self.get_ui().add_note()