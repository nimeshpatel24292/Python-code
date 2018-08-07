from urllib.request import urlopen

"""with urlopen('http://sixty-north.com/c/t.txt') as story:
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    story_words       
    for word in story_words:
    print(word)
"""

def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

banner("Hello world")

def adding(menu = None):
    if menu is None:
        menu = []
    menu.append('add')
    #print(menu)
    return menu

lunch = ['Egg','Milk']

adding(lunch)
print(lunch)


def check(n):
    if n % 2 == 0:
        print('even')
        return
    print('odd')

check(14)
check(5)