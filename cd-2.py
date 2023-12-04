import random
lis = ['alb','ald','lec','obz','sod','bod','woe','bfl','agv','lxj','alk',' lxl','owe','qzn','iso','vmp']
random = random.choice(lis)

st = input("Enter your message: ")
words = st.split(" ")
coding = input("Type 1 for coding and 0 for decoding: ")
coding = True if coding == "1" else False
print(coding)
if(coding):
    nwords = []
    for word in words:
        if len(word)>=3:
            r1 = random
            r2 = random
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords = []
    for word in words:
        if len(word)>=3:
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
