from Actor import Actor


class Character(Actor):
    def __init__(self, pos: tuple, size: tuple, img_path: str):
        super().__init__(pos, size, img_path)

        self.__hasCollided = False
        self.__gravity = 0.5
        self.__jump_force = 0.0

    @property
    def gravity(self):
        return self.__gravity

    @gravity.setter
    def gravity(self, gravity):
        self.__gravity = gravity

    @property
    def hasCollided(self):
        return self.__hasCollided

    @hasCollided.setter
    def hasCollided(self, cond):
        self.__hasCollided = cond

    # Atualiza vetor x do char dependendo da direcao parada 
    def update_movement(self, dir: str):
        if dir == "r":
            self.vx = 10
        elif dir == "l":
            self.vx = -10
        elif dir == "s":
            self.vx = 0
        else:
            print("Direction parameter must be 'r', 'l' or 's'")

    # Nao inplementado
    def increase_jump_force(self):
        if self.__jump_force < 1:
            self.__jump_force += 0.01

    # Aumenta vetor y do char
    def jump(self):
        if self.hasCollided:
            self.vy -= 50 * 0.3

    # Atualiza velocidade de queda
    def fall(self):
        self.vy += self.gravity

    # Movimento interno do char
    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.rect.move_ip(self.vx, self.vy)

    # Movimento externo do char, acessivel pela classe world
    def set_pos(self, vx, vy):
        self.x += vx
        self.y += vy
        self.rect.move_ip(vx, vy)
