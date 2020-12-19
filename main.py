
class Array:
    def __init__(self):
        self.are_you_winning_son = False
        self.matrix = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        # chooses two random blank fields and sets them to a value of 2
        self.__generate_new_tile()
        self.__generate_new_tile()


    def __str__(self):
        return "\n".join(["{0}".format(row) for row in self.matrix])

    def __repr__(self):
        return "\n".join(["{0}".format(row) for row in self.matrix])
