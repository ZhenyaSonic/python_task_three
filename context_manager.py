"""Модуль управления контекстным менеджером."""


class FileManager:
    """Менеджер контекста для безопасной работы с файлами."""
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        """Вызывается при входе в контекст."""
        try:
            self.file = open(self.filename, self.mode)
            return self.file
        except Exception as e:
            print(f"Ошибка при открытия файла {self.filename}: {e}")
            raise

    def __exit__(self, exc_type, exc_value, traceback):
        """Вызывается при выходе из контекста."""
        if self.file:
            self.file.close()
            print(f"Файл {self.filename}, закрыт")

        if exc_type is not None:
            print(f"Произошла ошибка: {exc_type.__name__}: {exc_value}")
            return False
        return True


if __name__ == '__main__':
    with FileManager("example.txt", "w") as file:
        file.write("Hello, world!")
