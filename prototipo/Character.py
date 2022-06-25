from Actor import Actor


class Character(Actor):
    def __init__(self, pos: tuple, size: tuple, img_path: str):
        super().__init__(pos, size, img_path)

        self.__gravity = 0.5
        self.__jump_force = 0.0

    @property
    def gravity(self):
        return self.__gravity

    @gravity.setter
    def gravity(self, gravity):
        self.__gravity = gravity

    def update_movement(self, dir: str):
        if dir == "r":
            self.vx = 20
        elif dir == "l":
            self.vx = -20
        elif dir == "s":
            self.vx = 0
        else:
            print("Direction parameter must be 'r', 'l' or 's'")

    def jump(self):
        self.vy -= 5

    def fall(self):
        self.vy += self.gravity

    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.rect.move_ip(self.vx, self.vy)

    def stop(self):
        self.vx = 0
        self.vy = 0
