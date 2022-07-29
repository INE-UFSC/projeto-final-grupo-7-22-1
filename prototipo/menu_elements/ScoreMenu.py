from menu_elements.TextBox import TextBox
from PathSingleton import path_single
from ConstantSingleton import const_single


class ScoreMenu:
    def __init__(self, height, width):
        self.height, self.width = height, width
        self.score_text_lines = [
            TextBox(
                path_single.scoreboard,
                (width / 2, 160),
                "SCOREBOARD",
                const_single.button_font,
                const_single.color_button_unselected,
            )
        ]

        self.scoreboard_text = TextBox(
            path_single.scoreboard,
            (width / 2, height / 2),
            "",
            const_single.text_font,
            const_single.color_button_unselected,
        )

    def update_score_text(self, score_dict):
        self.score_text_lines = self.score_text_lines[0:1]
        i = 0
        for score in score_dict:
            self.score_text_lines.append(
                TextBox(
                    path_single.button,
                    (self.width / 2, 200 + i),
                    score.string(),
                    const_single.text_font_small,
                    const_single.color_button_unselected,
                )
            )
            i += 30
