
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

    @property
    def __zeros(self):
        # calculates the number of blank tiles with value of 0
        zeros = 0
        for row in self.matrix:
            zeros += row.count(0)
        return zeros

    def __rand(self, upper_limit):
        '''Returns random integer number between zero (inclusive) and the input integer (also inclusive) - the upper_limit.

    In case of the input is less than 0, it returns -1.'''
        if upper_limit < 0:
            return -1
        else:
            return random.randint(0, upper_limit)

