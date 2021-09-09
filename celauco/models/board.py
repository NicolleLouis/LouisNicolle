class Board:
    length = 9
    width = 9

    def print(self):
        for i in range(self.length):
            line = ""
            for j in range(self.width):
                line += "0"
            print(line)
