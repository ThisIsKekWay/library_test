import sqlite3
from typing import Optional, List, Tuple, Any


class BookDAO:
    def __init__(self, db_path: str = 'library.db') -> None:
        self.db_path = db_path

    def _connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.db_path)

    def _execute_query(self, query: str, params: Tuple = ()) -> List[Tuple]:
        with self._connect() as connection:
            cursor = connection.cursor()
            cursor.execute(query, params)
            results = cursor.fetchall()
        return results

    def add_book(self, title: str, author: str, year: int) -> None:
        query = '''
            INSERT INTO books (title, author, year, status)
            VALUES (?, ?, ?, ?)
        '''
        self._execute_query(query, (title, author, year, 1))

    def delete_book(self, book_id: str) -> None:
        query = 'DELETE FROM books WHERE id = ?'
        self._execute_query(query, (book_id,))

    def search_books(self, title: Optional[str] = None, author: Optional[str] = None, year: Optional[int] = None) -> \
    List[Tuple]:
        query = 'SELECT * FROM books WHERE 1=1'
        params: List[Any] = []
        if title:
            query += ' AND title LIKE ?'
            params.append(f'%{title}%')
        if author:
            query += ' AND author LIKE ?'
            params.append(f'%{author}%')
        if year:
            query += ' AND year = ?'
            params.append(year)
        return self._execute_query(query, tuple(params))

    def display_all_books(self) -> List[Tuple]:
        query = 'SELECT * FROM books'
        return self._execute_query(query)

    def update_book_status(self, book_id: int, new_status: int) -> str:
        query = 'UPDATE books SET status = ? WHERE id = ?'
        self._execute_query(query, (new_status, book_id))
        return "OK"
