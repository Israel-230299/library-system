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

def	search_book(title):
    results	= []
    for	book_id, book in books.items():
        if title.lower() in book["title"].lower():
            results.append({"id": book_id, **book})
    return	results

# TODO: get_available_books()
def get_available_books():
    available = []
    for book_id, book in books.items():
        if book["available"]:
            available.append({"id": book_id, **book})
    return available

# TODO: get_overdue_loans()
def get_overdue_loans():
    overdue = []
    today = datetime.now().strftime("%Y-%m-%d")

    for book_id, loan in loans.items():
        if loan["due_date"] < today:
            overdue.append({
                "book_id": book_id,
                "book_title": books[book_id]["title"],
                "reader_name": readers[loan["reader_id"]]["name"],
                "due_date": loan["due_date"]
            })
    return overdue

# ========== MAIN ==========
if __name__ == "__main__":
    print("Library System Ready")
    print("Data loaded: 5 books, 4 readers")
