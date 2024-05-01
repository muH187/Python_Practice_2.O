words = input("Enter your message: ")
coding = input("Enter 1 for coding and 0 for decoding: ")
coding = True if coding == "1" else False

myWords = words.split(" ")
newWords = []

if coding:
    for word in myWords:
        if len(word) >= 3:

            r1 = "kdr"
            r2 = "cpr"

            stringNew = r1 + word[1:] + word[0] + r2
            newWords.append(stringNew)
        else:
            newWords.append(word[::-1])
    print(" ".join(newWords))
else:
    for word in myWords:
        if len(word) >= 3:
            stringNew = word[3:-3]
            stringNew = stringNew[-1] + stringNew[:-1]
            newWords.append(stringNew)
        else:
            newWords.append(word[::-1])
    print(" ".join(newWords))

