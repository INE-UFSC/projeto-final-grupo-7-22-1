

class Button:
    def __init__(self, image, image2, pos, text_input, font, base_color, hovering_color):
        self.__image = image
        self.__image1 = image
        self.__image2 = image2
        self.__x_pos = pos[0]
        self.__y_pos = pos[1]
        self.__font = font
        self.__base_color, self.__hovering_color = base_color, hovering_color
        self.__text_input = text_input
        self.__text = self.__font.render(self.__text_input, True, self.__base_color)
        if self.__image is None:
            self.__image = self.__text
        self.__rect = self.__image.get_rect(center=(self.__x_pos, self.__y_pos))
        self.__text_rect = self.__text.get_rect(center=(self.__x_pos, self.__y_pos))

    @property
    def image(self):
        return self.__image

    @property
    def rect(self):
        return self.__rect

    @property
    def text(self):
        return self.__text

    @property
    def text_rect(self):
        return self.__text_rect

    def check_For_Input(self, position):
        if position[0] in range(self.__rect.left, self.__rect.right) and position[
            1
        ] in range(self.__rect.top, self.__rect.bottom):
            return True
        return False

    def change_Color(self):
        self.__image = self.__image2
        self.__text = self.__font.render(self.__text_input, True, self.__hovering_color)

    
    def og_Color(self):
        self.__image = self.__image1
        self.__text = self.__font.render(self.__text_input, True, self.__base_color)
    
#def menu_Button_Style(self):