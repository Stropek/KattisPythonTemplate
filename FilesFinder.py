import os


class FilesFinder:

    def find_test_files(self):
        files = []

        for file in os.listdir("TestFiles"):
            if file.endswith(".in"):
                files.append(file)

        return files