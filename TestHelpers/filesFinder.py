import os


class FilesFinder:

    def findTestFiles(self):
        files = []

        for file in os.listdir("../TestFiles"):
            if file.endswith(".in"):
                files.append(file)

        return files

FilesFinder().findTestFiles()