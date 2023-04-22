print("opening file")
f=open("C:\\Users\\jokku\\filec.txt")
s=f.read()
s=str(s)
lc=0
uc=0
spc=0
sc=0
tc=0
dc=0
wc=1
for i in s:
    tc+=1
    if i.isalpha():
        if i.islower():
            lc+=1
        else:
            uc+=1
    elif i==".":
        sc+=1
    elif i==" " or i=="\n":
        wc+=1
    elif i.isdigit():
        dc+=1
    else:
        spc+=1
spc=spc-s.count("\n")
print("contents\n",s)
print("\nno of lowercase letters: ",lc)
print("no of uppercase letters: ",uc)
print("no of special characters: ",spc)
print("no of words: ",wc+1)
if sc==0:
    print("no of sentences: ",1)
else:
    print("no of sentences: ",sc)
