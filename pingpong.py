import arcade #библиотека аркад

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Pong Game'

class Ball(arcade.Sprite): #задаем мяч
    def __init__(self):
        super().__init__('ball.png', 1.0)
        self.change_x = 3 #скорость движения мяча горизонтальная
        self.change_y = 3 #вертикальная

    def update (self): #ф-я движения мяча
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right <= SCREEN_WIDTH: #чтобы мяч не уходил за экран
            self.change_x = -self.change_x
        if self.left <= 0:
            self.change_x = -self.change_x
        if self.change_y <= SCREEN_HEIGHT:
            self.change_y = -self.change_y
        if self.change_y <= 0:
            self.change_y = -self.change_y

class Bar(arcade.Sprite): #задаем ракетку
    def __init__(self):
        super().__init__('bar.png', 0.2)
    def update(self):
        self.center_x += self.change_x
        if self.right >= SCREEN_WIDTH:# чтобы ракетка не уходила за край экрана
            self.right = SCREEN_WIDTH
        if self.left <= 0:
            self.left = 0

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bar = Bar()
        self.ball = Ball()
        self.setup()

    def setup(self):
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 5 #положение ракетки
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 2  # положение мяча


    def on_draw(self):
        self.clear((255,255,255)) #белый фон окна
        self.bar.draw_hit_box() #отрисовка ракетки
        self.ball.draw_hit_box() #отрисовка мяча

    def update(self, delta):
        if arcade.check_for_collision(self.bar, self.ball):
            self.ball.change_y = -self.ball.change_y
        self.ball.update()
        self.bar.update()

    def on_key_press(self, key, modifiers): # ф-я движения ракетки
        if key == arcade.key.RIGHT:
            self.bar.change_x = 5
        if key == arcade.key.LEFT:
            self.bar.change_x = -5

    def on_key_release(self, key, modifiers): #ф-я остановки ракетки
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.bar.change_x = 0

if __name__ == '__main__':
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE) #окно
    arcade.run()