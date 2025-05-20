import os

from logic.question import Question


class Quiz:
    def __init__(self, directory):
        #biblioteka os
        paths = os.listdir(directory) #lista ze sciezkami do calej zawartosci katalogu
        self.questions = [Question(path) for path in paths]

