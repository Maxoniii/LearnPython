def palindrom(word):
    return word == word[::-1]

word = input()
if palindrom(word):
    print("Значится слово ПАЛИНДРОМ")
else:
    print("Ну получается слово не ПАЛИНДРОМ")
