import random


class Ball:
    def __init__(self, canvas, color, pole, stones, score_label):
        self.stones = stones  # Список камней на экране
        self.canvas = canvas
        self.pole = pole  # Объект палки
        self.score_label = score_label
        self.bottom_hit = False  # Флаг, указывающий, что мяч коснулся нижней границы
        self.hit = 0
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color, width=1, outline="#404258")
        self.canvas.move(self.id, 230, 461)  # Устанавливаем начальное положение мяча
        start_speeds = [4, 3.8, 3.6, 3.4, 3.2, 3, 2.8, 2.6]
        random.shuffle(start_speeds)
        self.speed_x = start_speeds[0]  # Начальная скорость по горизонтали
        self.speed_y = -start_speeds[0]  # Начальная скорость по вертикали
        self.canvas_height = canvas.winfo_height()  # Высота холста
        self.canvas_width = canvas.winfo_width()  # Ширина холста

    # Метод для проверки столкновения с камнями
    def stone_strike(self, ball_coordinates):
        for stone_line in self.stones:
            for stone in stone_line:
                stone_coordinates = self.canvas.coords(stone.id)
                try:
                    if ball_coordinates[2] >= stone_coordinates[0] and ball_coordinates[0] <= stone_coordinates[2]:
                        if ball_coordinates[3] >= stone_coordinates[1] and ball_coordinates[1] <= stone_coordinates[3]:
                            self.canvas.bell()  # Воспроизводим звук при столкновении
                            self.hit += 1  # Увеличиваем счетчик ударов
                            self.score_label.configure(text="Score: " + str(self.hit))  # Обновляем счет
                            self.canvas.delete(stone.id)  # Удаляем камень
                            return True
                except IndexError:
                    continue
        return False

    # Метод для проверки столкновения с палкой
    def pole_strike(self, ball_coordinates):
        pole_coordinates = self.canvas.coords(self.pole.id)
        if ball_coordinates[2] >= pole_coordinates[0] and ball_coordinates[0] <= pole_coordinates[2]:
            if ball_coordinates[3] >= pole_coordinates[1] and ball_coordinates[1] <= pole_coordinates[3]:
                return True
            return False

    # Метод для отрисовки мяча и его движения
    def draw(self):
        self.canvas.move(self.id, self.speed_x, self.speed_y)
        ball_coordinates = self.canvas.coords(self.id)
        start_speeds = [4, 3.8, 3.6, 3.4, 3.2, 3, 2.8, 2.6]
        random.shuffle(start_speeds)
        if self.stone_strike(ball_coordinates):
            self.speed_y = start_speeds[0]
        if ball_coordinates[1] <= 0:
            self.speed_y = start_speeds[0]
        if ball_coordinates[3] >= self.canvas_height:
            self.bottom_hit = True
        if ball_coordinates[0] <= 0:
            self.speed_x = start_speeds[0]
        if ball_coordinates[2] >= self.canvas_width:
            self.speed_x = -start_speeds[0]
        if self.pole_strike(ball_coordinates):
            self.speed_y = -start_speeds[0]
