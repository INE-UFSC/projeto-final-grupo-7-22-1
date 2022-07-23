from Actor import Actor


# Class Character implements especialization from actor to a character controlled by the player 
class Character(Actor):
    def __init__(self, pos: tuple, img):
        super().__init__(pos, img)

        #Attributes
        self.__hasCollided = False # True if character has collided with any other object
        self.__gravity = 0.5 # Gravity acceleration
        self.__jump_strengh = 0.0 # Percentage of total jump strengh

    #Getters and Setters
    @property
    def gravity(self):
        return self.__gravity

    @gravity.setter
    def gravity(self, gravity):
        self.__gravity = gravity

    @property
    def jump_strengh(self):
        return self.__jump_strengh

    @jump_strengh.setter
    def jump_strengh(self, jump_strengh):
        self.__jump_strengh = jump_strengh

    @property
    def hasCollided(self):
        return self.__hasCollided

    @hasCollided.setter
    def hasCollided(self, cond):
        self.__hasCollided = cond

    # Updates vector x depending on given direction 
    def update_movement(self, dir: str):
        if dir == "r":
            self.vx = 10
        elif dir == "l":
            self.vx = -10
        elif dir == "s":
            self.vx = 0
        else:
            print("Direction parameter must be 'r', 'l' or 's'")

    # Increase strengh of jump
    def increase_jump_force(self):
        if self.hasCollided:
            if self.jump_strengh == 0:
                self.jump_strengh = 0.2
            if self.jump_strengh < 0.4:
                self.jump_strengh += 0.005

    # Increases vector y according to jump strengh
    def jump(self):
        if self.hasCollided:
            self.vy -= 50 * self.jump_strengh
            self.jump_strengh = 0

    # Updates fall speed
    def fall(self):
        self.vy += self.gravity

    # Moves character position using internal vectors
    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.rect.update(self.x, self.y, self.width, self.height)

    # Moves character position using given vectors
    # Used to offset character in collisions
    def set_pos(self, vx, vy):
        self.x += vx
        self.y += vy
        self.rect.update(self.x, self.y, self.width, self.height)
