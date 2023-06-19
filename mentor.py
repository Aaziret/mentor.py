import math


def triangle_area(x1, y1, x2, y2, x3, y3):
    a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    b = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    c = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)

    p = (a + b + c) / 2

    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return s


def is_right_triangle(x1, y1, x2, y2, x3, y3):
    a2 = (x2 - x1) ** 2 + (y2 - y1) ** 2
    b2 = (x3 - x2) ** 2 + (y3 - y2) ** 2
    c2 = (x1 - x3) ** 2 + (y1 - y3) ** 2

    if a2 + b2 == c2 or a2 + c2 == b2 or b2 + c2 == a2:
        return True
    else:
        return False


x1, y1 = 0, 0
x2, y2 = 3, 4
x3, y3 = 5, 2

area = triangle_area(x1, y1, x2, y2, x3, y3).__round__()
is_right = is_right_triangle(x1, y1, x2, y2, x3, y3)

with open("area.txt", "w") as f:
    f.write(str(area))
with open("truefalse.txt", "w") as f:
    f.write(str(is_right))

sentence = input("Введите предложение: ")
words = sentence.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

most_common_word = max(word_count, key=word_count.get)
print("Самое часто встречающееся слово: " + most_common_word)

moments = [(10, 30, 45), (8, 15, 20), (12, 0, 0)]

sorted_moments = sorted(moments, key=lambda x: (x[0], x[1], x[2]))

print(sorted_moments)
