words = "Hello World, I'm Muhammad Ali"
print(words)

words.split(" ")

newWords = []
r1 = "kdr"
r2 = "cpr"

stringNew = r1 + words[0:] + r2
newWords.append(stringNew)

codedString = " ".join(newWords)
print(codedString)

stringNew2 = codedString[3:-3]
print(stringNew2)