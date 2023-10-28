from tkinter import *
from src.game_logic import start_game, restart_game, display_controls


# Функция для обработки нажатия клавиши R для рестарта
def handle_restart_key(event):
    if event.char in restart_keys:
        restart_game(canvas, score_label, root)


# Создаем главное окно
root = Tk()
root.title("")  # Устанавливаем заголовок окна
root.geometry("500x570")  # Устанавливаем размер окна
root.resizable(False, False)  # Запрещаем изменение размера окна
root.wm_attributes("-topmost", 1)  # Окно всегда поверх остальных окон

# Создаем холст для рисования
canvas = Canvas(root, width=500, height=500, bd=0, highlightthickness=0, highlightbackground="#93BFCF", bg="#404258")
canvas.pack(padx=10, pady=10)  # Устанавливаем положение холста и отступы

# Создаем метку для отображения счета
score_label = Label(height=50, width=80, text="Score: 00", font="Calibri 14")
score_label.pack(side="left")  # Устанавливаем положение метки

# Привязываем обработчик начала игры к клавише Enter
root.bind_all("<Return>", lambda event: start_game(canvas, score_label, root))

# Отображаем инструкции по управлению
display_controls(canvas)

# Задаем клавиши для рестарта игры
restart_keys = ["R", "r", "к", "К"]
root.bind_all("<Key>", lambda event: handle_restart_key(event))

# Запускаем главный цикл
root.mainloop()
