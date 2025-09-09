# Импортируем необходимые модули для создания GUI
import tkinter as tk
from tkinter import ttk

class ColorButton:
    def __init__(self):
        # Создаем главное окно приложения
        self.root = tk.Tk()
        self.root.title("Color Button")  # Заголовок окна
        self.root.geometry("350x250")  # Увеличиваем размер окна для второй кнопки
        self.root.resizable(False, False)  # Запрещаем изменение размера окна
        
        # Устанавливаем начальный цвет фона окна
        self.root.configure(bg="white")
        
        # Настраиваем главный фрейм для размещения элементов (используем tk.Frame вместо ttk.Frame)
        main_frame = tk.Frame(self.root, bg="white")
        main_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        # Создаем первую кнопку для изменения цвета самой кнопки
        self.button = tk.Button(
            main_frame,
            text="Цвет кнопки!",  # Изменяем текст на русский
            width=15,
            height=2,
            font=("Arial", 12, "bold"),
            bg="lightgray",
            relief="raised",
            borderwidth=3
        )
        self.button.pack(pady=10)
        
        # Создаем вторую кнопку для изменения цвета фона окна
        self.bg_button = tk.Button(
            main_frame,
            text="Цвет фона!",
            width=15,
            height=2,
            font=("Arial", 12, "bold"),
            bg="lightblue",
            relief="raised",
            borderwidth=3
        )
        self.bg_button.pack(pady=10)
        
        # Привязываем события к первой кнопке (изменение цвета кнопки)
        self.button.bind("<Button-1>", self.on_single_click)
        self.button.bind("<Double-Button-1>", self.on_double_click)
        
        # Привязываем события ко второй кнопке (изменение цвета фона)
        self.bg_button.bind("<Button-1>", self.on_bg_single_click)
        self.bg_button.bind("<Double-Button-1>", self.on_bg_double_click)
        
        # Добавляем инструкции для пользователя
        instructions = tk.Label(
            main_frame,
            text="Кнопка 'Цвет кнопки': 1 клик = Зеленая, 2 клика = Красная\nКнопка 'Цвет фона': 1 клик = Голубой фон, 2 клика = Желтый фон",
            font=("Arial", 9),
            justify=tk.CENTER,
            wraplength=300  # Перенос текста
        )
        instructions.pack(pady=10)
        
        # Сохраняем ссылку на главный фрейм для изменения его цвета
        self.main_frame = main_frame
    
    def on_single_click(self, event):
        """Обработка одиночного клика - изменяем кнопку на зеленую"""
        self.button.config(bg="green", activebackground="darkgreen")
        self.button.config(text="Зеленая!")
    
    def on_double_click(self, event):
        """Обработка двойного клика - изменяем кнопку на красную"""
        self.button.config(bg="red", activebackground="darkred")
        self.button.config(text="Красная!")
    
    def on_bg_single_click(self, event):
        """Обработка одиночного клика по кнопке фона - меняем фон на голубой"""
        self.root.configure(bg="lightblue")
        self.main_frame.configure(bg="lightblue")  # Также меняем цвет фрейма
        self.bg_button.config(text="Голубой фон!")
    
    def on_bg_double_click(self, event):
        """Обработка двойного клика по кнопке фона - меняем фон на желтый"""
        self.root.configure(bg="lightyellow")
        self.main_frame.configure(bg="lightyellow")  # Также меняем цвет фрейма
        self.bg_button.config(text="Желтый фон!")
    
    def run(self):
        """Запускаем GUI приложение"""
        self.root.mainloop()

# Запускаем приложение, если файл выполняется напрямую
if __name__ == "__main__":
    app = ColorButton()  # Создаем экземпляр приложения
    app.run()  # Запускаем главный цикл приложения