import tkinter as tk
import tkinter.messagebox as messagebox
import unittest

from app import Application


class DummyMessageBox:  # Заглушка для messagebox
    """
    Класс-заглушка для переопределения методов tkinter.messagebox в тестах.
    """

    @staticmethod
    def showinfo(title, message):
        """
        Заглушка для метода showinfo.
        """
        pass

    @staticmethod
    def showerror(title, message):
        """
        Заглушка для метода showerror.
        """
        pass


class TestGui(unittest.TestCase):
    """
    Класс для тестирования GUI-приложения на основе unittest.

    Методы:
        setUp(): Выполняется перед каждым тестом, настраивает окружение.
        tearDown(): Выполняется после каждого теста, очищает ресурсы.
        assign_colors_for_test(): Помощник для назначения цветов объектам перед тестами.
        test_sort_colors_basic(): Проверяет базовый сценарий сортировки.
        test_sort_colors_empty_input(): Проверяет случай с пустым вводом.
        test_sort_colors_no_colors_assigned(): Проверяет случай, когда не всем объектам назначены цвета.
        test_sort_colors_partial_input(): Проверяет сортировку при частичном совпадении объектов.
        test_sort_colors_all_objects_same_color(): Проверяет сортировку, если все объекты одного цвета.
    """

    def setUp(self):
        """
        Настраивает окружение перед каждым тестом:
        - Заменяет messagebox на заглушку.
        - Инициализирует приложение и его GUI.
        """
        # Заменяем messagebox на заглушку перед тестами
        self.original_messagebox = messagebox
        messagebox.showinfo = DummyMessageBox.showinfo
        messagebox.showerror = DummyMessageBox.showerror

        # Инициализация приложения и GUI перед каждым тестом
        self.app = Application(master=tk.Tk())
        self.app.master.protocol("WM_DELETE_WINDOW", self.app.quit)
        self.app.pack()

    def tearDown(self):
        """
        Восстанавливает оригинальные настройки и освобождает ресурсы после каждого теста.
        """
        # Восстановление оригинального messagebox после тестов
        messagebox.showinfo = self.original_messagebox.showinfo
        messagebox.showerror = self.original_messagebox.showerror

        # Очистка ресурсов после каждого теста
        self.app.destroy()

    def assign_colors_for_test(self, green_objects, blue_objects, red_objects):
        """
        Назначает цвета объектам в приложении перед выполнением тестов.

        Аргументы:
            green_objects (list): Список объектов зеленого цвета.
            blue_objects (list): Список объектов синего цвета.
            red_objects (list): Список объектов красного цвета.
        """
        self.app.entry_green.delete(0, tk.END)
        self.app.entry_blue.delete(0, tk.END)
        self.app.entry_red.delete(0, tk.END)
        self.app.entry_objects.delete(0, tk.END)

        self.app.entry_green.insert(0, " ".join(green_objects))
        self.app.entry_blue.insert(0, " ".join(blue_objects))
        self.app.entry_red.insert(0, " ".join(red_objects))

        self.app.assign_colors()

    def test_sort_colors_basic(self):
        """
        Тестирует базовый сценарий:
        - Все объекты имеют назначенные цвета.
        - Проверяется правильность сортировки по цветам.
        """
        # Назначаем цвета для объектов
        self.assign_colors_for_test(
            green_objects=["A", "B"], blue_objects=["C", "D"], red_objects=["E", "F"]
        )

        # Вводим полный набор объектов для сортировки
        self.app.entry_objects.insert(0, "A B C D E F")

        # Тестируем сортировку
        self.app.sort_colors()

        # Получаем результат, удаляя строку заголовка
        displayed_objects = [
            widget.cget("text") for widget in self.app.result_frame.winfo_children()
        ]
        displayed_objects = displayed_objects[1:]  # Игнорируем заголовок

        # Ожидаемые отсортированные объекты
        sorted_objects = ["A", "B", "C", "D", "E", "F"]
        self.assertEqual(displayed_objects, sorted_objects)

    def test_sort_colors_empty_input(self):
        """
        Тестирует сценарий с пустым вводом:
        - Поле ввода объектов остается пустым.
        - Проверяется, что результат пустой.
        """
        self.app.entry_objects.insert(0, "")
        self.app.sort_colors()

        # Получаем результат
        displayed_objects = [
            widget.cget("text") for widget in self.app.result_frame.winfo_children()
        ]
        self.assertEqual(displayed_objects, [])

    def test_sort_colors_no_colors_assigned(self):
        """
        Тестирует сценарий, когда не всем объектам назначены цвета:
        - Проверяется возникновение ошибки KeyError.
        """
        # Назначаем цвета только для объектов "A" и "B"
        self.assign_colors_for_test(
            green_objects=["A", "B"], blue_objects=[], red_objects=[]
        )

        # Вводим полный набор объектов для сортировки
        self.app.entry_objects.insert(0, "A B C D E F")

        # Тестируем, что при отсутствии цвета для объектов C, D, E, F возникнет ошибка
        with self.assertRaises(KeyError):
            self.app.sort_colors()

    def test_sort_colors_partial_input(self):
        """
        Тестирует сценарий с частичным вводом:
        - Некоторые объекты имеют назначенные цвета, но полный ввод содержит дополнительные объекты.
        - Проверяется, что возникает ошибка KeyError.
        """
        # Назначаем цвета для некоторых объектов
        self.assign_colors_for_test(
            green_objects=["A", "B"], blue_objects=["C", "D"], red_objects=[]
        )

        # Вводим частичный набор объектов для сортировки
        self.app.entry_objects.insert(0, "A B C D E F")

        # Тестируем сортировку
        with self.assertRaises(KeyError):
            self.app.sort_colors()

    def test_sort_colors_all_objects_same_color(self):
        """
        Тестирует случай, когда все объекты одного цвета:
        - Проверяется, что порядок объектов не меняется.
        """
        # Назначаем цвета для всех объектов одного цвета
        self.assign_colors_for_test(
            green_objects=["A", "B", "C"], blue_objects=[], red_objects=[]
        )

        # Вводим объекты для сортировки
        self.app.entry_objects.insert(0, "A B C")

        # Тестируем сортировку
        self.app.sort_colors()

        # Получаем результат, удаляя строку заголовка
        displayed_objects = [
            widget.cget("text") for widget in self.app.result_frame.winfo_children()
        ]
        displayed_objects = displayed_objects[1:]  # Игнорируем заголовок

        # Ожидаемые отсортированные объекты (порядок не меняется, так как все одного цвета)
        sorted_objects = ["A", "B", "C"]
        self.assertEqual(displayed_objects, sorted_objects)


if __name__ == "__main__":
    unittest.main()
