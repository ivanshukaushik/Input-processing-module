
compulsory = ["DIA", "LENGTH", "NODE", "NAME"]


class Rules:
    def __init__(self, content):
        self.content = content

    def compulsory(self):
        for part in self.content:
            if part not in compulsory:
                print("The Compulsory fields have not been entered \n")
                break

    def single(self):
        for part in self.content:
            number_of_occurances = self.content.count(part)
            if number_of_occurances > 1:
                print("The Single fields have been entered more than once")
