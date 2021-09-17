# ["119", "97674223", "1195524421"]	false

def solution(book):
    book.sort()

    for i in range(len(book)-1):
        if book[i+1].startswith(book[i]):
            return False

    return True
