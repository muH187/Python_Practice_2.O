words = "Hello World I'm Muhammad Ali is"
print(words)

myWords = words.split(" ")
newWords = []
for word in myWords:
    if len(word) >= 3:

        r1 = "kdr"
        r2 = "cpr"

        stringNew = r1 + word[1:] + word[0] + r2
        newWords.append(stringNew)
    else:
        newWords.append(word[::-1])
print(" ".join(newWords))


