from database import init
from dao import BookDAO


def add_book(book: BookDAO) -> None:
    try:
        title, author, year = input('Введите название, автора и год через точку с запятой\n').split(';')
        book.add_book(title, author, int(year))
        print('Книга добавлена')
    except ValueError:
        print("Ошибка ввода. Убедитесь, что вы ввели название, автора и год через точку с запятой.")
    except Exception as e:
        print(f"Ошибка: {e}")


def delete_book(book: BookDAO) -> None:
    try:
        book_id = input('Введите id книги: ')
        book.delete_book(book_id)
        print('Книга удалена')
    except Exception as e:
        print(f"Ошибка: {e}")


def search_books(book: BookDAO) -> None:
    try:
        title = input('Введите название книги (или оставьте пустым): ')
        author = input('Введите автора книги (или оставьте пустым): ')
        year_input = input('Введите год книги (или оставьте пустым): ')
        year = int(year_input) if year_input else None
        results = book.search_books(title=title or None, author=author or None, year=year)
        if results:
            for result in results:
                print(result)
        else:
            print('Книги не найдены')
    except ValueError:
        print("Ошибка ввода. Убедитесь, что год введен корректно.")
    except Exception as e:
        print(f"Ошибка: {e}")


def show_all_books(book: BookDAO) -> None:
    books = book.display_all_books()
    for book in books:
        print(book)


def update_book_status(book: BookDAO) -> None:
    try:
        book_id, new_status = map(int, input('Введите id книги и статус через пробел.\n'
                                             'Статус 1 аналогичен статусу "в наличии"\n'
                                             'Статус 0 аналогичен статусу "выдана"\n').split())
        print(book.update_book_status(book_id, new_status))
    except ValueError:
        print("Ошибка ввода. Убедитесь, что вы ввели id и статус как целые числа.")
    except Exception as e:
        print(f"Ошибка: {e}")


def print_help() -> None:
    print('Список команд:\n exit - Выход\n add - добавить книгу\n delete - удалить книгу по id\n'
          ' search - поиск книг\n show all - показать все книги\n status - обновить статус книги\n')


def main() -> None:
    init()
    book = BookDAO()
    commands = {
        'add': add_book,
        'delete': delete_book,
        'search': search_books,
        'show all': show_all_books,
        'status': update_book_status,
        'help': print_help
    }

    while True:
        user_input = input('Введите действие\nВведите "help" для вызова справки\n')
        if user_input == 'exit':
            break
        if user_input == 'help':
            print_help()
        else:
            command = commands.get(user_input)
            if command:
                command(book)
            else:
                print("Неизвестная команда. Введите 'help' для списка команд.")


if __name__ == '__main__':
    main()
