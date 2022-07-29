from entities.Actor import Actor
from ConstantSingleton import const_single
from PathSingleton import path_single

# Implementa especialização do ator para um personagem 
class Character(Actor):
    def __init__(self, pos: tuple, img):
        super().__init__(pos, img)

        # Atributos
        self.__hasCollided = False # Verdade quando jogador colidiu com outro ator
        self.__running = False
        self.__preparing_jump = False
        self.__jump_strengh = 0.0 # Porcentagem da força total do pulo

    #Getters e Setters
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

    # Atualiza vetor x dependenfo da direção informado e constante de "fricção" 
    def update_movement(self, dir: str, friction = const_single.friction_const):
        if dir == "r":
            self.vx = const_single.char_movement
            self.__running = True
        elif dir == "l":
            self.__running = True
            self.vx = -const_single.char_movement
        elif dir == "s":
            self.__running = False
            if self.vx > friction:
                self.vx -= friction
            elif self.vx < -friction:
                self.vx += friction
            else:
                self.vx = 0
        else:
            print("Direction parameter must be 'r', 'l' or 's'")

    # Aumento força do pulo
    def increase_jump_force(self):
        if self.hasCollided:
            if self.jump_strengh == 0:
                self.jump_strengh = const_single.jump_strengh_minimum
            if self.jump_strengh < const_single.jump_strengh_limit:
                self.jump_strengh += const_single.jump_strengh_increase
            self.__preparing_jump = True

    # Aumenta vetor y de acordo com a força do pulo
    def jump(self):
        if self.hasCollided:
            self.vy -= const_single.jump_speed * self.jump_strengh
            self.jump_strengh = 0
            self.__preparing_jump = False

    # Atualiza velocidade de queda
    def fall(self):
        self.vy += const_single.gravity

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
    
    def update_sprite(self):
        if self.__preparing_jump:
            self.image = path_single.character_preparing_jump
        elif self.vy < 0:
            if self.vx > 0:
                self.image = path_single.character_jump
            else:
                self.image = path_single.character_jump2
        elif self.vy > 0:
            if self.vx > 0:
                self.image = path_single.character_fall
            else:
                self.image = path_single.character_fall2
        elif self.__running:
            if self.vx > 0:
                self.image = path_single.character_run
            else:
                self.image = path_single.character_run2
        else:
            self.image = path_single.character_idle
