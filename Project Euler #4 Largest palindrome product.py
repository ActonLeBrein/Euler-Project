def palindrome(l):
    largest = None
    for i in range(999, 0, -1):
        if i * 999 < largest:
            break 
        for j in range(999, i-1, -1):
            product = i*j
            s = str(product)
            if s == s[::-1]:
                if product > largest and product < l:
                    largest = product
    return largest

T = int(raw_input())
for _ in range(T):
    print palindrome(int(raw_input()))