import sys
from urllib.request import urlopen


def fatch_word(url):
    """
    fetch_word is used for fatching the data from any URL

    Arguments: here it used the url data convert into utf-8

    return: in the readable format
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
        return story_words

"""

def printing(words):               
    for word in words:
        print(word)


def main(url): 
    #url = sys.argv[1]
    print(__name__)
    # if __name__ == "__main__":
    newdata = fatch_word(url)
    printing(newdata)


if __name__ == '__main__':
    main(sys.argv[1])


def check(n):
    if n % 2 == 0:
        print('even')
        return
    print('odd')
check(14)
check(5)


def adding(menu = None):
    if menu is None:
        menu = []
    menu.append('add')
    print(menu)
    return menu

lunch = ['Egg','Milk']
b= ['abc','def']
adding(lunch)
adding(b)
"""


#List Techniques
"""
s= "Hi nimesh patel you doing coding".split()
t="i a a ds fg dg df dsfg d"
print(s)
print(s[1:4])

q= "ok kjd jhfdkj sfhasjkf sdhjfha ksjh dfhakdkj sh  skjjfh dfsfh af nnnn".split()
print(q.index('sh'))
print(q.count('nnnn'))
print('nnnn' in ['sfds','sdfd','fgds','dvs','nnnn'])
z=q.remove('ok') # remove perticular name from list
print(q)
del q[1] # delete the perticular index in list//
print(q)
o = "i have some problems".split()
o.insert(2,'not')
print(' '.join(o))
"""

#combine lists and reverse and sort it
"""
a=[4,1,2,3,0,11,8]
b=[4,5]
print(a+b)
a.extend([6,7])
print(a)
a.reverse() # or use reversed(a)
print(a)
a.sort() # or use sorted(a)
print(a)
"""

# dictonary
"""
nap= [('nim',123466),('sag',54688),('aaa',789654)]
b= dict(nap)
print(b)
# update dictonary
b.update({'ccc': 456789})
print(b)
for key, value in b.items():  # this is for printing dictonary using for loop 
    print("{key} => {value}".format(key=key, value=value))
"""

#copy lists
"""
u=s.copy()
print(u)
u=s
v= list(t)
print(v)
print(u)
ssequencecopy=s[1:4]
scopy=s[:] # full slice techniques
print(ssequencecopy)
print(scopy)

d=[[1,2],[2,3]]
d[1].append(4)
print(d[1])

#repetation list
e=[1,2]
f= e * 4
print(f)
"""

# range with for loop
"""
a= range(4)
b= list(range(3,8))
print(a)
print(b)
c= list(range(0,8,2))
print(c)
for d in c:
    print(d)
for i in range(3):
    print(i)
"""

# while loop
"""
a= 5
while a!=0:
    print(a)
    a-=1

while True:
    print("Enter integer number")
    respond= input()
    if int(respond) % 2 == 0:
        break
"""

# Tuple
"""
a= ('nimesh', 1.1, 0, (1,2))
print(a)
for i in a:
    print(i)
print(len(a)) 
a = a + ("patel", 2) # add tuple
print(a)
a = a * 3 # multiply tuple
print(a)

def minmax(items):
    return min(items), max(items)
c = minmax([23,56,2,-4,45,66])
lower , upper = minmax([23,56,2,-4,45,66])
print(c)
print(lower) 
print(upper)
"""

#string
"""
a = "i" + "am" + "patel"
print(a)
b= ' '.join(['I','am','good']) # if you use empty string then it is joining it like ''.join(['nim','e','sh']) -> nimesh
#print(b)
print(b.split(' '))
print("the age of {0} ia {1}. {0}'s birthday is on {2}".format('Nimesh',26,'february'))
"""

# exceptions
"""
def excprogram():    
    try:
        while True:
            print("Enter integer number")
            x= input()
            if int(x) % 2 == 0:
                print("even number")
                return
            else:
                excprogram()
    except (ValueError, TypeError):
        print("wrong integer or string")
        excprogram()
       #pass 
    
        #x for x in range(20) if excprogram():
        #print(y)
if __name__ == '__main__':
    excprogram()
"""

#file
#file: file path is required otherwise it gaves exception error
# mode: read/write/append  text/binary always required to mentioned it\
# encoding: text encoding
import sys
f= open('new.txt', mode='wt', encoding='utf-8') # write
f.write("Hello this is first file!\n")
f.write("Please write the file please")
f= open('new.txt', mode='rt', encoding='utf-8') # read
#print(f.read(32))
print(f.readline())
f.seek(0) # goes back to firstline of the file
print(f.readline())
f= open('new.txt', mode='at', encoding='utf-8') #append
f.writelines(
    ['this is me\n,'
    'i am stranger to the dark,\n'
    'Hard a way this is want to broken parts'])
f.close()

def main(filename):
    #f= open('new.txt', mode='rt', encoding='utf-8')
    with open('new.txt', mode='rt', encoding='utf-8') as f:
        for line in f:
        #  print(line)
            sys.stdout.write(line)
    

if __name__=='__main__':
    main(sys.argv[0])