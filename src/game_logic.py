from .ball import Ball
from .pole import Pole
from .stone import Stone
from .exceptions import MyCustomException
import time
import random


# Функция для начала игры
def start_game(canvas, score_label, root):
    playing = False  # Флаг, указывающий, идет ли игра
    paused_text = None  # Переменная для хранения текста "ПАУЗА"

    def handle_start_game():
        nonlocal playing
        playing = True  # Устанавливаем флаг в True, когда игра начинается

    root.bind_all("<Return>", lambda event: handle_start_game())  # Привязываем начало игры к клавише Enter

    if not playing:
        # playing = True
        score_label.configure(text="Score: 00")  # Устанавливаем начальный счет
        canvas.delete("all")  # Очищаем холст
        ball_colors = ["#789395", "#D0CAB2", "#BDCDD6"]
        stone_colors = ["#93BFCF", "#EEE9DA", "#94B49F", "#94B49F", "#E5E3C9", "#DED9C4",
                        "#96C7C1", "#89B5AF", "#FFF5E4", "#DFD3C3", "#D0B8A8", "#F5EFE6",
                        "#E8DFCA", "#AEBDCA", "#7895B2", "#FAEDCD", "#CCD5AE"]
        random.shuffle(ball_colors)  # Перемешиваем цвета для мяча
        pole = Pole(canvas, "#D0CAB2")  # Создаем палку с определенным цветом
        stones = []
        for i in range(0, 5):
            stone_line = []
            for j in range(0, 19):
                random.shuffle(stone_colors)  # Перемешиваем цвета для камней
                stone = Stone(canvas, stone_colors[0])  # Создаем камень
                stone_line.append(stone)
            stones.append(stone_line)

        for i in range(0, 5):
            for j in range(0, 19):
                canvas.move(stones[i][j].id, 25 * j, 25 * i)  # Расставляем камни на холсте

        ball = Ball(canvas, ball_colors[0], pole, stones, score_label)  # Создаем мяч
        root.update_idletasks()
        root.update()
        time.sleep(1)  # Задержка перед началом игры
        while True:
            if pole.pause_seconds != 1:
                try:
                    canvas.delete(paused_text)
                except MyCustomException:
                    pass
                if not ball.bottom_hit:
                    ball.draw()
                    pole.draw()
                    root.update_idletasks()
                    root.update()
                    time.sleep(0.01)
                    if ball.hit == 95:
                        canvas.create_text(250, 250, text="YOU WIN", fill="#FAEDCD", font="Calibri 24")
                        pole.set_game_over()
                        root.update_idletasks()
                        root.update()
                        break
                else:
                    canvas.create_text(250, 250, text="GAME OVER", fill="#B46060", font="Calibri 24")
                    pole.set_game_over()
                    root.update_idletasks()
                    root.update()
                    break
            else:
                try:
                    if paused_text is None:
                        pass
                except MyCustomException:
                    paused_text = canvas.create_text(250, 250, text="PAUSE", fill="#6096B4", font="Calibri 24")
                root.update_idletasks()
                root.update()


# Функция для рестарта игры
def restart_game(canvas, score_label, root):
    canvas.delete("all")  # Очищаем холст
    start_game(canvas, score_label, root)  # Запускаем новую игру


# Функция для отображения инструкций по управлению
def display_controls(canvas):
    control_text1 = "Press Space to pause, R to restart"
    control_text2 = "Use arrow keys (← and →) to control the platform"
    canvas.create_text(250, 30, text=control_text1, fill="white", font="Calibri 14 italic")
    canvas.create_text(250, 60, text=control_text2, fill="white", font="Calibri 14 italic")
    canvas.create_text(250, 250, text="Press Enter to start Game", fill="#FAEDCD", font="Calibri 18")
