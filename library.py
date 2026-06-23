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


def return_book(book_id):
    if book_id not in loans:
        print("Book is not on loan")
        return False

    reader_id = loans[book_id]["reader_id"]

    books[book_id]["available"] = True
    readers[reader_id]["books_borrowed"].remove(book_id)
    del loans[book_id]

    print("Book returned successfully")
    return True


def extend_loan(book_id, days):
    if book_id not in loans:
        print("Book is not on loan")
        return False

    current_due = datetime.strptime(loans[book_id]["due_date"], "%Y-%m-%d")
    new_due = current_due + timedelta(days=days)
    loans[book_id]["due_date"] = new_due.strftime("%Y-%m-%d")

    print(f"Loan extended. New due date: {loans[book_id]['due_date']}")
    return True


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
    print("=== Library System Test ===\n")

    print("Available books:")
    for book in get_available_books():
        print(f" - {book['title']}")

    print("\nSearching for 'Harry':")
    for book in search_book("Harry"):
        print(f"  - {book['title']}")

    print("\nBorrowing Harry Potter for Noam:")
    borrow_book("B001", "R003")

    print("\nAvailable books now:")
    for book in get_available_books():
                print(f"  - {book['title']}")

    print("\nReturning Harry Potter:")
    return_book("B001")

    print("\nOverdue loans:")
    for loan in get_overdue_loans():
        print(f"  - {loan['book_title']} (was due: {loan['due_date']})")
