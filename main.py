
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

    def __generate_new_tile(self):
        # between 0 and 15 (inclusive)
        random_number = self.__rand(self.__zeros - 1)
        # increment after finding the zero or after replacing the zero when hits the random number
        number_of_zero = 0
        for i, row in enumerate(self.matrix):
            for j, cell in enumerate(self.matrix[i]):
                if cell == 0 and number_of_zero == random_number:
                    # 15% chances for 4, otherwise 2 to be placed as new random tile
                    self.matrix[i][j] = 2 if random.random() < 0.85 else 4
                    number_of_zero += 1
                elif cell == 0:
                    number_of_zero += 1

