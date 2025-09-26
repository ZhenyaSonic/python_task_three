"""Модуль библиотеки для управление коллекцией книг."""
from typing import List, Optional


class Book:
    """Класс, для представления книги."""
    def __init__(
            self,
            title: str,
            author: str,
            year: int,
            genre: str,
            pages: int
            ):
        self._validate_data(title, author, year, genre, pages)
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.pages = pages

    def _validate_data(
            self,
            title: str,
            author: str,
            year: int,
            genre: str,
            pages: int
            ):
        """Проверка корректности входных данных."""
        validations = [
            (
                title,
                "название книги должно быть непустой строкой",
                str,
                lambda x: bool(x.strip())
                ),
            (
                author,
                "автор",
                str,
                lambda x: bool(x.strip())
                ),
            (
                year,
                "Год не может быть пустым",
                int,
                lambda x: x > 0
                ),
            (
                genre,
                "Жанр не может быть пустым",
                str,
                lambda x: bool(x.strip())
                ),
            (
                pages,
                "Кол-во страниц должно быть больше 0",
                int,
                lambda x: x > 0
            )
        ]

        for value, error_message, expected_type, validator in validations:
            if not isinstance(value, expected_type) or not validator(value):
                raise ValueError(error_message)

    def __repr__(self):
        return (
            f"""Book('{self.title}', '{self.author}', '{self.year}', '{self.genre}', '{self.pages}')"""
        )

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return (self.title.lower(), self.author.lower(), self.year,
                self.genre.lower(), self.pages) == (
                    other.title.lower(), other.author.lower(), other.year,
                    other.genre.lower(), other.pages)


class Library:
    """Класс библиотеки для управления коллекцией книг."""
    def __init__(self):
        self._books: List[Book] = []

    def add_book(self, book: Book) -> None:
        """Добавление книги в библиотеку."""
        if book in self._books:
            raise ValueError(
                f"Книга '{book.title}' уже существует в библиотеке"
            )
        self._books.append(book)

    def search_by_title(self, title: str) -> Optional[Book]:
        """Поиск книги по точному названию."""

        for book in self._books:
            if book.title.lower() == title.lower():
                return book
        return None

    def get_books_by_author(self, author: str) -> List[Book]:
        """Получение всех книг указанного автора."""
        return [book for book in self._books
                if book.author.lower() == author.lower()]

    def get_books_sorted_by_year(self) -> List[Book]:
        """Получение всех книг по году."""
        return sorted(self._books, key=lambda book: book.year)

    def __repr__(self):
        return f"Library({len(self._books)} books)"


if __name__ == "__main__":
    library = Library()
    book1 = Book("Название1", "Автор1", 2001, "Жанр1", 300)
    book2 = Book("Название2", "Автор2", 1999, "Жанр2", 150)
    library.add_book(book1)
    library.add_book(book2)
    print(library.search_by_title("Название1"))
    print(library.get_books_by_author("Автор1"))
    print(library.get_books_sorted_by_year())
