
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

