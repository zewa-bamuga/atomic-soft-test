import tkinter as tk  # Стандартная библиотека для создания GUI
from tkinter import messagebox


class Application(tk.Frame):
    """
    Класс для создания графического интерфейса приложения, которое позволяет назначать цвета объектам и сортировать их по цвету.

    Атрибуты:
        master (tk.Tk): Основное окно приложения.
        color_mapping (dict): Словарь для сопоставления объектов и их цветов.
    """

    def __init__(self, master=None):
        """
        Инициализирует приложение.

        Аргументы:
            master (tk.Tk, optional): Основное окно приложения. По умолчанию None.
        """
        super().__init__(master)
        self.master = master
        self.master.title('Тестовое задание АО "АтомикСофт"')
        self.master.geometry("600x400")
        self.color_mapping = {}  # Словарь для сопоставления объектов и их цветов
        self.create_widgets()

    def create_widgets(self):
        """
        Создает и размещает все виджеты (элементы интерфейса), включая поля ввода и кнопки.
        """
        # Поле для ввода объектов зеленого цвета
        self.label_green = tk.Label(
            self, text="Введите объекты зеленого цвета (З):", fg="green"
        )
        self.label_green.pack(pady=5)
        self.entry_green = tk.Entry(self, width=50)
        self.entry_green.pack()

        # Поле для ввода объектов синего цвета
        self.label_blue = tk.Label(
            self, text="Введите объекты синего цвета (С):", fg="blue"
        )
        self.label_blue.pack(pady=5)
        self.entry_blue = tk.Entry(self, width=50)
        self.entry_blue.pack()

        # Поле для ввода объектов красного цвета
        self.label_red = tk.Label(
            self, text="Введите объекты красного цвета (К):", fg="red"
        )
        self.label_red.pack(pady=5)
        self.entry_red = tk.Entry(self, width=50)
        self.entry_red.pack()

        # Кнопка для назначения цветов
        self.assign_button = tk.Button(
            self, text="Назначить цвета", command=self.assign_colors
        )
        self.assign_button.pack(pady=10)

        # Поле для ввода полного набора объектов
        self.label_objects = tk.Label(
            self, text="Введите весь набор объектов (например, A B C D):"
        )
        self.label_objects.pack(pady=10)
        self.entry_objects = tk.Entry(self, width=50)
        self.entry_objects.pack()

        # Кнопка сортировки
        self.sort_button = tk.Button(self, text="Сортировать", command=self.sort_colors)
        self.sort_button.pack(pady=10)

        # Рамка для вывода результатов
        self.result_frame = tk.Frame(self)
        self.result_frame.pack(pady=10)

    def assign_colors(self):
        """
        Назначает цвета объектам на основе ввода пользователя и заполняет словарь color_mapping.
        """
        self.color_mapping.clear()
        # Получаем объекты из полей для каждого цвета
        green_objects = self.entry_green.get().strip().split()
        blue_objects = self.entry_blue.get().strip().split()
        red_objects = self.entry_red.get().strip().split()

        # Заполняем словарь сопоставления цветов
        for obj in green_objects:
            self.color_mapping[obj] = "З"
        for obj in blue_objects:
            self.color_mapping[obj] = "С"
        for obj in red_objects:
            self.color_mapping[obj] = "К"

        messagebox.showinfo("Успех", "Цвета успешно назначены объектам.")

    def sort_colors(self):
        """
        Сортирует введенные объекты по их цветам и отображает результат.

        Проверяет, что все объекты имеют назначенный цвет, и выводит отсортированные объекты на экран.
        """
        # Получаем полный набор объектов
        objects = self.entry_objects.get().strip().split()

        if not objects:
            messagebox.showerror(
                "Ошибка ввода", "Поле ввода объектов должно быть заполнено."
            )
            return

        try:
            # Проверяем, что все объекты имеют назначенный цвет
            for obj in objects:
                if obj not in self.color_mapping:
                    raise KeyError(f"Объект '{obj}' не имеет назначенного цвета.")

            # Если все объекты имеют цвет, выполняем сортировку
            sorted_objects = self.sort_by_color_order(objects)

            # Очищаем контейнер для меток перед выводом нового результата
            for widget in self.result_frame.winfo_children():
                widget.destroy()

            # Добавляем надпись перед отсортированными объектами
            header_label = tk.Label(
                self.result_frame, text="Отсортированные объекты:", font=("Arial", 8)
            )
            header_label.pack(pady=10)

            # Создаем метки для каждого объекта с нужным цветом
            for obj in sorted_objects:
                color = self.color_mapping[obj]
                label = tk.Label(self.result_frame, text=obj, font=("Arial", 12))
                if color == "З":
                    label.config(fg="green")
                elif color == "С":
                    label.config(fg="blue")
                elif color == "К":
                    label.config(fg="red")
                label.pack(side=tk.LEFT, padx=2)

        except KeyError as e:
            messagebox.showerror("Ошибка", str(e))
            raise  # Перебрасываем исключение, чтобы оно могло быть проверено в тестах

    def sort_by_color_order(self, objects, color_order=["З", "С", "К"]):
        """
        Сортирует список объектов по их цветам на основе заданного порядка цветов.

        Аргументы:
            objects (list): Список объектов для сортировки.
            color_order (list): Список порядка цветов, где первый элемент имеет высший приоритет.

        Возвращает:
            list: Отсортированный список объектов по цвету.
        """
        # Создаем отображение цвета в его приоритет для быстрого доступа
        color_priority = {color: index for index, color in enumerate(color_order)}

        # Проверяем, что все объекты имеют определенный цвет
        try:
            objects_with_colors = [(obj, self.color_mapping[obj]) for obj in objects]
        except KeyError:
            raise KeyError("Некоторые объекты не имеют назначенного цвета.")

        # Сортируем объекты по приоритету цвета
        sorted_objects = sorted(objects_with_colors, key=lambda x: color_priority[x[1]])

        return [obj for obj, _ in sorted_objects]


def start_application():
    """
    Запускает приложение, создавая окно и экземпляр класса Application.

    Возвращает:
        Application: Экземпляр класса Application.
    """
    root = tk.Tk()
    icon = tk.PhotoImage(file="icon.png")
    root.iconphoto(True, icon)
    app = Application(master=root)
    app.master.protocol(
        "WM_DELETE_WINDOW", app.quit
    )  # Чтобы приложение корректно закрывалось
    app.pack()
    return app


if __name__ == "__main__":
    start_application().mainloop()
