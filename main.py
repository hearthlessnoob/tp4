import arcade
import random

SCREEN_WIDTH = 1900
SCREEN_HEIGHT = 1000

COLORS = [arcade.color.RED, arcade.color.BLUE, arcade.color.GREEN, arcade.color.YELLOW, arcade.color.ORANGE,
          arcade.color.PURPLE, arcade.color.PINK]


class Balle:
    #initiate la classe balle
    def __init__(self, x, y, rayon, color):
        self.x = x
        self.y = y
        self.change_x = 10
        self.change_y = 10
        self.rayon = rayon
        self.color = color
    #faire la balle bouger
    def update(self):
        self.x += self.change_x
        self.y += self.change_y

        if self.x < self.rayon:
            self.change_x *= -1
        elif self.x > SCREEN_WIDTH - self.rayon:
            self.change_x *= -1
        if self.y < self.rayon:
            self.change_y *= -1
        elif self.y > SCREEN_HEIGHT - self.rayon:
            self.change_y *= -1
    #dessiner la balle
    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color)


class Rectangle:
    #initiate la classe rectangle
    def __init__(self, x, y, width, height, color, angle):
        self.x = x
        self.y = y
        self.change_x = 10
        self.change_y = 10
        self.width = width
        self.height = height
        self.color = color
        self.angle = angle
    #faire bouger le rectangle
    def update(self):
        self.x += self.change_x
        self.y += self.change_y

        if self.x < self.width/2:
            self.change_x *= -1
        elif self.x > SCREEN_WIDTH - self.width/2:
            self.change_x *= -1
        if self.y < self.height/2:
            self.change_y *= -1
        elif self.y > SCREEN_HEIGHT - self.height/2:
            self.change_y *= -1
    #dessiner le rectangle
    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color, self.angle)


class MyGame(arcade.Window):
    #ouvrir la fenetre
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.balles = []
        self.rectangles = []
    #changer le background color
    def setup(self):
        arcade.set_background_color(arcade.color.BLACK)
    #dessiner les formes
    def on_draw(self):
        arcade.start_render()
        for balle in self.balles:
            balle.draw()
        for rectangle in self.rectangles:
            rectangle.draw()
    #faire bouger les formes
    def on_update(self, delta_time):
        for balle in self.balles:
            balle.update()
        for rectangle in self.rectangles:
            rectangle.update()
    #savoir si on doit creer un cercle ou un rectangle
    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            balle = Balle(x, y, 30, random.choice(COLORS))
            self.balles.append(balle)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            rectangle = Rectangle(x, y, 50, 50, random.choice(COLORS), 0)
            self.rectangles.append(rectangle)


def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()


if __name__ == "__main__":
    main()
