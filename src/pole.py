class Pole:
    def __init__(self, canvas, color):
        self.paused_text = None
        self.canvas = canvas
        self.game_over = False  # Флаг, указывающий, завершилась ли игра
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color, outline="#404258")
        self.canvas.move(self.id, 200, 485)  # Устанавливаем начальное положение палки
        self.speed_x = 0  # Скорость движения палки по горизонтали
        self.pause_seconds = 0  # Счетчик секунд паузы
        self.canvas_width = canvas.winfo_width()  # Ширина холста
        self.canvas.bind_all("<Left>", self.turn_left)  # Привязываем левое движение палки к клавише Left
        self.canvas.bind_all("<Right>", self.turn_right)  # Привязываем правое движение палки к клавише Right
        self.canvas.bind_all("<space>", self.pause)  # Привязываем паузу к клавише Space

    # Метод для отрисовки палки и ее движения
    def draw(self):
        pole_coordinates = self.canvas.coords(self.id)
        if pole_coordinates[0] + self.speed_x <= 0:
            self.speed_x = 0
        if pole_coordinates[2] + self.speed_x >= self.canvas_width:
            self.speed_x = 0
        self.canvas.move(self.id, self.speed_x, 0)

    # Метод для поворота палки влево
    def turn_left(self, event):
        self.speed_x = -3.5

    # Метод для поворота палки вправо
    def turn_right(self, event):
        self.speed_x = 3.5

    # Метод для проверки окончания игры
    def game_over(self):
        return self.game_over

    # Метод для управления паузой
    def pause(self, event):
        if self.game_over:
            return

        self.pause_seconds += 1
        if self.pause_seconds == 1:
            self.paused_text = self.canvas.create_text(250, 250, text="PAUSE", fill="#6096B4", font="Calibri 24")
        elif self.pause_seconds == 2:
            self.canvas.delete(self.paused_text)
            self.paused_text = None
            self.pause_seconds = 0

    # Метод для установки флага окончания игры
    def set_game_over(self):
        self.game_over = True
