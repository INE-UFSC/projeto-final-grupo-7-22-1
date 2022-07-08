from World import World


class Draw():
    def __init__(self,object):
        self.__object_to_drawn = object
        

    def draw(self):
        if isinstance(self.__object_to_drawn, World):
            self.__object_to_drawn.screen.fill('white')
            for region in self.__object_to_drawn.regions:
                for step in region.plataforms:
                    for plataform in step:
                        self.__object_to_drawn.screen.blit(plataform.image, plataform.rect)
            self.__object_to_drawn.screen.blit(self.__object_to_drawn.player.image, self.__object_to_drawn.player.rect)

    def draw_menu(self):
        if isinstance(self.__object_to_drawn, World):
            self.__object_to_drawn.screen.fill('white')