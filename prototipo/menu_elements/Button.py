

class Button:
    def __init__(self, image, image2, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.image1 = image
        self.image2 = image2
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))


    def check_For_Input(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[
            1
        ] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def change_Color(self):
        self.image = self.image2
        self.text = self.font.render(self.text_input, True, self.hovering_color)

    
    def og_Color(self):
        self.image = self.image1
        self.text = self.font.render(self.text_input, True, self.base_color)
    
#def menu_Button_Style(self):