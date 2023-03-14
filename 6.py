file=open("r.txt",'r')
contents=file.read()
contents=contents.split(',')
#for x in contents :
  #  if int(x)%2==0:
       # print(x)
filetowrite=open("evens.txt",'a')
for x in contents:
    if int(x)%2==0:
        filetowrite.write(x)
        filetowrite.write("\n")
        print(x)
with open("evens.txt",'r') as file2:
    print(file2.read())
