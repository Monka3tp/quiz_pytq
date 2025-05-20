from statistics import correlation


class Question:
    def __init__(self, path):
        try:
            with open(path, 'r') as file:
                data = file.read()
            data = data.split('\n')
            self.text = data[0]
            self.answers = [data[1][3:], data[2][3:], data[3][3:], data[4][3:]]
            correct = data[5][-1]
            #wersja Roch i wibtu
            #self.correct = ord(correct) - ord('A')
            match correct:
                case 'A':
                    self.correct = 0
                case 'B':
                    self.correct = 1
                case 'C':
                    self.correct = 2
                case 'D':
                    self.correct = 3
        except Exception as exception:
            raise ValueError(f'Błędny format pliku: {path}')