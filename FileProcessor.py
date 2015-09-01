__author__ = 'akhil'

import re

class FileProcessor:

    def setFileName(self, filename):
        self.filename = filename

    def setFilePath(self, filepath):
        self.filepath = filepath

    def setFile(self):
        self.file = self.filepath + '/' + self.filename

    def __init__(self, filepath, filename):
        self.setFilePath(filepath)
        self.setFileName(filename)
        self.setFile()

    def getFileName(self):
        return self.filename

    def getFilePath(self):
        return self.filepath

    def getFile(self):
        return self.file

    def _getFileContent(self):
        if hasattr(self, '_filecontent'):
            return self._filecontent
        fileptr = open(self.getFile(), 'r', encoding='utf-8')
        self._filecontent = fileptr.read()
        fileptr.close()
        return self._filecontent

    def checkForContent(self, patternList):
        if not hasattr(self, '_filecontent'):
            self._getFileContent()
        for pattern in patternList:
            if re.search(pattern, self._filecontent, flags=re.I|re.M) is None:
                return False

        return True


