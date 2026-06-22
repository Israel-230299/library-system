from datetime import datetime, timedelta

# ========== DATA ==========
books = {
    "B001": {"title": "Harry Potter", "author": "J.K. Rowling", "available": True},
    "B002": {"title": "The Hobbit", "author": "J.R.R. Tolkien", "available": False},
    "B003": {"title": "1984", "author": "George Orwell", "available": True},
    "B004": {"title": "The Little Prince", "author": "Antoine de Saint", "available": True},
    "B005": {"title": "Pride and Prejudice", "author": "Jane Austen", "available": False}
}

readers = {
    "R001": {"name": "David", "books_borrowed": ["B002"]},
    "R002": {"name": "Yael", "books_borrowed": ["B005"]},
    "R003": {"name": "Noam", "books_borrowed": []},
    "R004": {"name": "Shira", "books_borrowed": []}
}

loans = {
    "B002": {"reader_id": "R001", "due_date": "2024-02-15"},
    "B005": {"reader_id": "R002", "due_date": "2024-02-10"}
}

# ========== LOAN FUNCTIONS ==========
# TODO: borrow_book(book_id, reader_id)
# TODO: return_book(book_id)
# TODO: extend_loan(book_id, days)

# ========== REPORT FUNCTIONS ==========
# TODO: search_book(title)
# TODO: get_available_books()
# TODO: get_overdue_loans()

# ========== MAIN ==========
if __name__ == "__main__":
    print("Library System Ready")
