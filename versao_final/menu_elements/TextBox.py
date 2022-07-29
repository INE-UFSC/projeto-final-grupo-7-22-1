

class TextBox:
    def __init__(self, image, pos, text_input, font, base_color):
        self.__image = image
        self.__x_pos = pos[0]
        self.__y_pos = pos[1]
        self.__font = font
        self.__base_color = base_color
        self.change_text(text_input)
        if self.__image is None:
            self.__image = self.__text
        self.__rect = self.__image.get_rect(center=(self.__x_pos, self.__y_pos))

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

    @property
    def text_input(self):
        return self.__text_input

    def change_text(self, text_input):
        self.__text_input = text_input
        self.__text = self.__font.render(self.__text_input, True, self.__base_color)
        self.__text_rect = self.__text.get_rect(center=(self.__x_pos, self.__y_pos))
