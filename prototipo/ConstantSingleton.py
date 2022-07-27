

class ConstantSingleton:
    def __init__(self):
        #Screen size
        self.width = 800
        self.height = 600

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