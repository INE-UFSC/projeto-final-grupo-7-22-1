from PathSingleton import path_single


class Renderer:
    def __init__(self, object_world, main_menu, object_screen, score_menu, textbox):
        self.__object_world = object_world
        self.__screen = object_screen
        self.__main_menu = main_menu
        self.__score_menu = score_menu
        self.__text_menu = textbox
        ### object_menu

    def draw_game(self):
        self.__screen.blit(path_single.background, self.__screen.get_rect())

        for region in self.__object_world.regions:
            for step in region.objects:
                for actor in step:
                    self.__screen.blit(actor.image, actor.rect)
        self.__screen.blit(
            self.__object_world.player.image, self.__object_world.player.rect
        )
        self.__screen.blit(
            self.__object_world.score_text.text,
            self.__object_world.score_text.text_rect,
        )

    def draw_pre_menu(self):
        self.__screen.blit(path_single.background, self.__screen.get_rect())
        self.__screen.blit()
        self.__screen.blit(self.__text_menu.Draw[0], self.__text_menu.Draw[1])

    def draw_main_menu(self):
        self.__screen.blit(path_single.background, self.__screen.get_rect())
        self.draw_button(self.__main_menu.start_button)
        self.draw_button(self.__main_menu.score_button)
        self.draw_button(self.__main_menu.quit_button)

    def draw_score_menu(self):
        self.__screen.blit(path_single.background, self.__screen.get_rect())
        self.__screen.blit(
            self.__score_menu.scoreboard_text.image,
            self.__score_menu.scoreboard_text.rect,
        )
        for score_text_line in self.__score_menu.score_text_lines:
            self.__screen.blit(score_text_line.text, score_text_line.text_rect)

    def draw_button(self, button):
        self.__screen.blit(button.image, button.rect)
        self.__screen.blit(button.text, button.text_rect)
