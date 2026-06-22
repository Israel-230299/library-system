from datetime import datetime, timedelta

# ========== DATA ==========
books = {}
readers = {}
loans = {}

# ========== LOAN FUNCTIONS ==========
def borrow_book(book_id, reader_id):
    if book_id not in books:
        print("Book	not	found")
        return False
    if not books[book_id]["available"]:
        print("Book	not	available")
        return False
    books[book_id]["available"] = False
    readers[reader_id]["books_borrowed"].append(book_id)
    due_date = datetime.now() + timedelta(days=14)
    loans[book_id] = {
        "reader_id":	reader_id,
        "due_date":	due_date.strftime("%Y-%m-%d")
    }
    print(f"Book	borrowed	successfully.	Due	date:	{loans[book_id]['due_date']}")
    return True
# TODO: return_book(book_id)
# TODO: extend_loan(book_id, days)

# ========== REPORT FUNCTIONS ==========
# TODO: search_book(title)
# TODO: get_available_books()
# TODO: get_overdue_loans()

# ========== MAIN ==========
if __name__ == "__main__":
    print("Library System Ready")
