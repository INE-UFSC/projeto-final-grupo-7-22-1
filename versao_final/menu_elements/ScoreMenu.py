from menu_elements.TextBox import TextBox
from menu_elements.AbstractMenu import AbstractMenu
from PathSingleton import path_single
from ConstantSingleton import const_single

class ScoreMenu(AbstractMenu):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.__score_text_lines = [
            TextBox(
            path_single.scoreboard,
            (width / 2, 160),
            "SCOREBOARD",
            const_single.button_font,
            const_single.color_button_unselected
        )]
        
        self.__scoreboard = TextBox(
            path_single.scoreboard,
            (width / 2, height / 2),
            "",
            const_single.text_font,
            const_single.color_button_unselected
        )

    def update_score_text(self, score_dict):
        self.__score_text_lines = self.__score_text_lines[0:1]
        i = 0
        scores = []
        for s in score_dict:
            scores.append((s.points, s))
        for score in sorted(scores, reverse=True, key= lambda i: i[0])[0:9]:
            self.__score_text_lines.append(
                TextBox(
                    path_single.button,
                    (self.width / 2, 200 + i),
                    score[1].string(),
                    const_single.text_font_small,
                    const_single.color_button_unselected
            ))
            i += 30
    
    def draw(self, screen):
        screen.blit(path_single.background, screen.get_rect())
        screen.blit(self.__scoreboard.image , self.__scoreboard.rect)
        for text_box in self.__score_text_lines:
            screen.blit(text_box.text, text_box.text_rect)
