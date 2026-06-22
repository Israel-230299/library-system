from datetime import datetime, timedelta

# ========== DATA ==========
books = {}
readers = {}
loans = {}

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

# ========== MAIN ==========
if __name__ == "__main__":
    print("Library System Ready")
