from view.menu_items.MenuMethod import MenuMethods


class FindDate(MenuMethods):
    def description(self):
        return "Выбор заметок по дате"

    def run(self):
        self.get_ui().date_selection()