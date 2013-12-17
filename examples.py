import os
import re
from os.path import isfile, join

langTable = {
            'c': '.c',
            'python': '.py',
            'haskell': '.hs',
            'clojure': '.clj',
            'regex': '.py',
            'ruby': '.rb',
            }

def getChapters(language):
    dir = os.path.join(os.getcwd(), 'code')
    file = os.path.join(dir, language)
    fhandle = open(file, 'r')
    line = fhandle.readline()
    chapters = []
    while line:
        if token(line) == Tokens.CHAPTER:
            chapters.append(chapter(line))
        line = fhandle.readline()
    return chapters

def getExercises(language, chapter):
    dir = os.path.join(os.getcwd(), 'languages')
    dir = os.path.join(dir, language)
    chapdir = os.path.join(dir, chapter)
    exercises = [ex for ex in os.listdir(chapdir) if ex.startswith('ex') and
            ex.endswith(langTable[language])]
    return sorted(exercises)

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

def exercise(language, chapter):
    exfiles = getExercises(language, chapter);
    value = []
    for ex in exfiles:
        dir = os.path.join(os.getcwd(), 'languages')
        dir = os.path.join(dir, language)
        chapdir = os.path.join(dir, chapter)
        file = os.path.join(chapdir, ex)

        outputfile = os.path.join(chapdir, ex.replace(langTable[language], ".out"))
        input = open(file, 'r')
        output = open(outputfile, 'r')
        value.append([input.read(), output.read()])
    return value
