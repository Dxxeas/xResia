import tkinter as tk
import random

# Функция для создания случайного цвета
def random_color():
    return f'#{random.randint(0, 0xFFFFFF):06x}'

# Функция для создания визуального эффекта
def create_visual_effect():
    for _ in range(100):  # Увеличено количество фигур
        x = random.randint(0, root.winfo_screenwidth())
        y = random.randint(0, root.winfo_screenheight())
        size = random.randint(30, 150)  # Немного уменьшен размер фигур
        color = random_color()
        shape = random.choice(['circle', 'rect'])

        if shape == 'circle':
            canvas.create_oval(x, y, x + size, y + size, fill=color, outline="")
        elif shape == 'rect':
            canvas.create_rectangle(x, y, x + size, y + size, fill=color, outline="")

    # Очищаем экран и создаем новый эффект через 50 мс
    root.after(50, clear_and_redraw)  # Уменьшено время задержки для более быстрых эффектов

# Функция для очистки экрана и перерисовки
def clear_and_redraw():
    canvas.delete("all")
    create_visual_effect()

# Инициализация окна tkinter
root = tk.Tk()
root.attributes('-fullscreen', True)
root.attributes('-topmost', True)
root.attributes('-transparentcolor', 'black')

# Создаем холст для рисования
canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg='black', highlightthickness=0)
canvas.pack()

# Запуск визуального эффекта
create_visual_effect()

# Запуск главного цикла tkinter
root.mainloop()
