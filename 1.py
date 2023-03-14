a="muhammed rafid"
b={}
for letter in a:
    if letter in b:
        b[letter]=b[letter]+1
    else:
        b[letter]=1
print(b)

maxcountsofar =0
mostoccuring=""
for letter in b :
    if b[letter]>maxcountsofar:
        maxcountsofar=b[letter]
        mostoccuring=letter
print("Most occuring letter is ",mostoccuring)

