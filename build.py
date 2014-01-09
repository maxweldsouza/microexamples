#TODO Active highlight navigation bar
#TODO C compilation
#TODO Permalinks
#TODO Add search feature
#TODO Social bookmarking
#TODO Goto next chapter
#TODO Improve performance
#TODO Add google analytics
#TODO Change title based on page
#TODO Reformat code
#TODO Changeable Color Themes
#TODO Add permalinks

import re
import os

#This is the list of languages supported
langTable = {
            'c': '.c',
            'python': '.py',
            'haskell': '.hs',
            'clojure': '.clj',
            'regex': '.py',
            'ruby': '.rb',
            'clisp': '.lisp'
            }
langList = ['c','python','haskell','clisp', 'regex']
langNames = {'c': 'C', 'python': 'Python', 'haskell': 'Haskell', 'clisp': 'Common Lisp', 'regex': 'Regex'}
hlName = {'c': 'c', 'python': 'python', 'haskell': 'haskell', 'clisp': 'lisp', 'regex': 'python'}

class Tokens:
    CHAPTER, EXERCISE, CODE = range(3)

def token(line):
    e = re.match(r'<!--Chapter=[a-zA-Z].*-->', line)
    if e:
        return Tokens.CHAPTER
    e = re.match(r'<!--Exercise-->', line)
    if e:
        return Tokens.EXERCISE
    return Tokens.CODE

def chapter(line):
    line = re.sub(r'^<!--Chapter=', '', line)
    line = re.sub(r'-->\n$', '', line)
    print line
    return line

def exercise():
    return

ex = 1
for language in langTable:
    f = open(os.path.join('code', language), 'r')
    line = f.readline()

    while line:
        print line,

        linetoken = token(line)
        if linetoken == Tokens.CHAPTER:
            ex = 1
            directory = os.path.join('.', 'languages', language, chapter(line))
            if not os.path.exists(directory):
                os.makedirs(directory)

        if linetoken == Tokens.EXERCISE:
            exstring = '%03d' % ex
            exercise = 'ex' + exstring + langTable[language]
            exercise = os.path.join(directory, exercise)
            w = open(exercise, 'w+')
            #TODO close file?
            ex += 1

        if linetoken == Tokens.CODE:
            w.write(line)

        line = f.readline()
