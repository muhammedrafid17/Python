file=open("r.txt",'r')
contents=file.readlines()
for x in contents :
    if int(x.strip()) %2==0 :
        print(x.strip())


