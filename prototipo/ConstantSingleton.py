from pygame import font, Color


class ConstantSingleton:
    def __init__(self):
        #Screen size
        self.width = 800
        self.height = 600

        #Colors
        self.color_button_unselected = Color(222, 222, 222)
        self.color_button_selected = Color(122, 122, 122)

        #Fonts
        font.init()
        self.button_font_size = 40
        self.text_font_size = 30
        self.text_font_size_small = 20
        self.button_font = font.Font(font.get_default_font(), self.button_font_size)
        self.text_font = font.Font(font.get_default_font(), self.text_font_size)
        self.text_font_small = font.Font(font.get_default_font(), self.text_font_size_small)

        #World properties
        self.world_vel = 2
        self.wall_bound = 30
        self.defeat_condition_multiplier = 1.5
        self.upper_limit = 50
        self.preset_amount = 4

        #Region Properties
        self.yoffset = 150

        #Plataform properties
        self.friction_const = 2

        #Character properties
        self.char_movement = 5
        self.gravity = 0.5
        self.jump_strengh_minimum = 0.2
        self.jump_strengh_increase = 0.005
        self.jump_strengh_limit = 0.4
        self.jump_speed = 50


const_single = ConstantSingleton()