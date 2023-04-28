from view.menu_items.MenuMethod import MenuMethods


class Exit(MenuMethods):
    def description(self):
        return "Выход"

    def run(self):
        self.get_ui().exit()