

from menu_elements.TextBox import TextBox
from PathSingleton import path_single
from ConstantSingleton import const_single

class GameOverMenu:
    def __init__(self, height, width):
        self.height, self.width = height, width
        self.text_lines = [
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
        
    def change_text(self, char):
        if char == 'del':
            text = self.text_lines[1].text_input[:-1]
        else:
            text = self.text_lines[1].text_input + char
        self.text_lines[1].change_text(text)