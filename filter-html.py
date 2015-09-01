__author__ = 'akhil'

import re
import argparse
import os
from os import walk
from FileProcessor import FileProcessor

BASE_DIR = os.getcwd() + '/../crawls/'

# initialize argument parser
parser = argparse.ArgumentParser()
parser.add_argument('--crawlname', '--cn', help='name of the crawl')
args = parser.parse_args()

FILE_PATH = BASE_DIR + args.crawlname + '/filedump'
FILTER_PATH = BASE_DIR + args.crawlname + '/filtered-files/'
FAILED_PATH = BASE_DIR + args.crawlname + '/failed-files/'

def moveToTarget(file, target):
    file = re.sub('\(', '\\(', file)
    file = re.sub('\)', '\\)', file)
    os.system('cp ' + FILE_PATH + '/' + file + ' ' + target)

def getAllFiles():
    files = []
    for (dirpath, dirnames, filenames) in walk(FILE_PATH):
        files.extend(filenames)
        break

    files = filter(lambda x: not x.startswith('.'), files)

    return files

def main():

    titlePattern    = "(.)*<div\sid=\"title\">(\s)*game(.+)of(.+)thrones(.*)"
    categoryPattern = "<dt>type:</dt>(\s*)<dd><a href=(.+)Video(.*)TV(.*)shows</a></dd>"
    patternList  = [titlePattern, categoryPattern]

    count = 0
    files = getAllFiles()
    for file in files:
        fileProcessor = FileProcessor(FILE_PATH, file)

        if fileProcessor.checkForContent(patternList):
            moveToTarget(file, FILTER_PATH)
            count += 1
        else:
            moveToTarget(file, FAILED_PATH)
        print('done')
    print(count)

main()