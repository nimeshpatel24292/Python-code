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
"""
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

s= "Hi nimesh patel you doing coding".split()
print(s)
print(s[1:4])