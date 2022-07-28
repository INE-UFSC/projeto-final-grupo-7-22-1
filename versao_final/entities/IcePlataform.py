


from entities.Plataform import Plataform, PLATAFORM_TYPE


class IcePlataform(Plataform):
    def __init__(self, pos: tuple, type: PLATAFORM_TYPE, img):
        super().__init__(pos, type, img)

    def update_movement(self, vx, vy):
        self.vx = vx
        self.vy = vy
        
    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.rect.move_ip(self.vx, self.vy)
    
    def player_collision(self, player):
        player.update_movement('s', 0.25)
        player.vy = 0