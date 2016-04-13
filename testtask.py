"""
Определить 2 наибольших числа произвольного списка
с неуникальными элементами
"""

l = [8, 8, 3, 4, 2, 6, 7, 7, 3]
Big1 = 0
Big2 = 0

for i in l:
    if Big1 < i:
        Big2 = Big1
        Big1 = i

if Big2 == Big1:
    Big2 = 0

if Big2 == 0:
    for i in l:
        if Big2 < i and i != Big1:
            Big2 = i

print(Big1, Big2)