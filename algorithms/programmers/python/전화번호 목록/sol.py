def solution(phone_book):
    phone_book.sort()
    for i in range(0, len(phone_book)-1):
        tmp = phone_book[i]
        end = len(tmp)
        if tmp == phone_book[i+1][0:end]:
            return False
    return True