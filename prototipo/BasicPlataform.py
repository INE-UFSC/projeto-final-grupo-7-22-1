


from Plataform import Plataform, PLATAFORM_TYPE


class BasicPlataform(Plataform):
    def __init__(self, pos: tuple, size: tuple, type: PLATAFORM_TYPE, img_path: str):
        super().__init__(pos, size, type, img_path)

    def update_movement(self, vx, vy):
        self.vx = vx
        self.vy = vy
        
    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.rect.move_ip(self.vx, self.vy)