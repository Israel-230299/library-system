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
