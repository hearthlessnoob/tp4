import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = [arcade.color.RED, arcade.color.BLUE, arcade.color.GREEN, arcade.color.YELLOW, arcade.color.ORANGE, arcade.color.PURPLE, arcade.color.PINK]


class Balle:
    def __init__(self, x, y, change_x, change_y, rayon, color):
        self.x = x
        self.y = y
        self.change_x = change_x
        self.change_y = change_y
        self.rayon = rayon
        self.color = color

    def update(self):
        self.x += self.change_x
        self.y += self.change_y

        # Valider que la balle ne sorte pas de l'écran
        if self.x < self.rayon:
            self.x = self.rayon
            self.change_x *= -1
        elif self.x > SCREEN_WIDTH - self.rayon:
            self.x = SCREEN_WIDTH - self.rayon
            self.change_x *= -1
        if self.y < self.rayon:
            self.y = self.rayon
            self.change_y *= -1
        elif self.y > SCREEN_HEIGHT - self.rayon:
            self.y = SCREEN_HEIGHT - self.rayon
            self.change_y *= -1

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color)


class Rectangle:
    def __init__(self, x, y, change_x, change_y, width, height, color, angle):
        self.x = x
        self.y = y
        self.change_x = change_x
        self.change_y = change_y
        self.width = width
        self.height = height
        self.color = color
        self.angle = angle

    def update(self):
        self.x += self.change_x
        self.y += self.change_y

        # Valider que le rectangle ne sorte pas de l'écran
        if self.x < 0:
            self.x = 0
            self.change_x *= -1
        elif self.x > SCREEN_WIDTH - self.width:
            self.x = SCREEN_WIDTH - self.width
            self.change_x *= -1
        if self.y < 0:
            self.y = 0
            self.change_y *= -1
        elif self.y > SCREEN_HEIGHT - self.height:
            self.y = SCREEN_HEIGHT - self.height
            self.change_y *= -1

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color, self.angle)


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.balles = []
        self.rectangles = []

    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()
        for balle in self.balles:
            balle.draw()
        for rectangle in self.rectangles:
            rectangle.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            balle = Balle(x, y, random.uniform(-5, 5), random.uniform(-5, 5), random.randint(10, 30), random.choice(COLORS))
            self.balles.append(balle)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            rectangle = Rectangle(x, y, random.uniform(-5, 5), random.uniform(-5, 5), random.randint(10, 100), random.randint(10, 100), random.choice(COLORS), 0)
            self.rectangles.append(rectangle)


def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()


if __name__ == "__main__":
    main()
