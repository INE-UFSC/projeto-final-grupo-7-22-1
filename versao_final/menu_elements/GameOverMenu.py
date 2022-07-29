

from menu_elements.TextBox import TextBox
from menu_elements.AbstractMenu import AbstractMenu
from PathSingleton import path_single
from ConstantSingleton import const_single

class GameOverMenu(AbstractMenu):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.__text_lines = [
            TextBox(
            path_single.scoreboard,
            (width / 2, (height / 2) - 40),
            "Player name:",
            const_single.button_font,
            const_single.color_button_unselected
            ),
            TextBox(
            path_single.button,
            (width / 2, height / 2),
            "",
            const_single.text_font,
            const_single.color_button_unselected
            )
        ]
    
    def input_text(self):
        return self.__text_lines[1].text_input
        
    def change_text(self, char):
        if char == 'del':
            text = self.__text_lines[1].text_input[:-1]
        else:
            text = self.__text_lines[1].text_input + char
        self.__text_lines[1].change_text(text)
    
    def draw(self, screen):
        screen.blit(path_single.background, screen.get_rect())
        for text_box in self.__text_lines:
            screen.blit(text_box.text, text_box.text_rect)