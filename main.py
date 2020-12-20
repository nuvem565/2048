
import random
import colorama

colorama.init()


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

    # flag for printing the message to winner
    @property
    def are_you_winning_son(self):
        return self.__are_you_winning_son

    @are_you_winning_son.setter
    def are_you_winning_son(self, state):
        self.__are_you_winning_son = state

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

    __colors_table = {
        # font, background colors
        "_": "\033[1;37;40m", # white, black
        "2": "\033[1;37;40m", # white, black
        "4": "\033[1;36;40m", # cyan, black
        "8": "\033[1;34;40m", # blue, black
        "16": "\033[1;32;40m", # green, black
        "32": "\033[1;35;40m", # purple, black
        "64": "\033[1;33;40m", # yellow, black
        "128": "\033[1;31;40m", # red, black
        "256": "\033[1;30;47m", # black, white
        "512": "\033[1;35;47m", # purple, white
        "1024": "\033[1;31;47m", # red, white
        "2048": "\033[1;30;41m", # black, red
        "no_match": "\033[1;33;41m" # yellow, red
    }

    def print_matrix(self):
        # shows the main matrix to the user
        for row in self.matrix:
            for cell in row:
                cell = str(cell)
                # replaces 0 by underscore in output
                cell = "_" if "0" == cell else cell
                # checks for appropriate font color in dict
                color = self.__colors_table.get(cell, "no_match")
                last_black_line = self.__colors_table.get("_")
                print(f"{color}{cell: >5s}{last_black_line}", end=" ")
            # line break after each row of matrix
            print()
        print()

    @property
    def score(self):
        # prints the total score (sum of the tiles values)
        total = 0
        for row in self.matrix:
            for cell in row:
                total += cell
        return total

    @property
    def no_possible_moves(self):
        # it's possible to move if there's at least one zero
        if self.__zeros != 0:
            return False
        else:
            # it can still move if there is no blank tile
            for i, row in enumerate(self.matrix):
                for j, cell in enumerate(row):
                    if any([
                            # check of inside values without first column and row
                            (0 < i and 0 < j) and (self.matrix[i][j] == self.matrix[i-1][j]
                                                   or self.matrix[i][j] == self.matrix[i][j-1]),
                            # first column check
                            0 < i and self.matrix[i][0] == self.matrix[i-1][0],
                            # first row check
                            0 < j and self.matrix[0][j] == self.matrix[0][j-1]]):
                        return False
            # no adjacent tile is the same
            return True

    def __inform_or_generate_new_tile(self, previous_matrix):
        # chooses appropriate action after the movement
        if self.no_possible_moves:
            print("You lose!")
        elif previous_matrix == self.matrix:
            # if there is no change after the movement, don't add any new tile
            self.matrix[:][:] = previous_matrix[:][:]
        else:
            # adds a new tile after checking for movement
            self.__generate_new_tile()

    # auxiliary methods for matrix manipulations
    def __rotate270(self):
        # rotates the main matrix by -90 degrees
        self.matrix = \
            [[self.matrix[j][i] for j in range(len(self.matrix))]
             for i in range(len(self.matrix[0])-1, -1, -1)]

    def __rotate90(self):
        self.matrix = \
            [[self.matrix[j][i] for j in range(len(self.matrix)-1, -1, -1)]
             for i in range(len(self.matrix))]

    def __rotate180(self):
        self.matrix = \
            [[self.matrix[i][j] for j in range(len(self.matrix[0])-1, -1, -1)]
             for i in range(len(self.matrix)-1, -1, -1)]

    def __move(self):
        # shift to the right
        # the universal type of movement
        # can be transformed into any other (to up, to bottom, to left) by matrix manipulations - rotate methods
        # loops from the left to the right, from the top to the bottom of the matrix
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0]) - 1):
                if self.matrix[i][j+1] == 0:
                    # shifts the previous cells to the direction of checking - to the right
                    # allows to add the tiles that aren't next ot each other
                    self.matrix[i][0:j+2] = [0] + self.matrix[i][0:j+1]
        # loops from right to left, from the top to the bottom of the matrix
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0]) - 1, 0, -1):
                if self.matrix[i][j] == self.matrix[i][j-1]:
                    # adds the tiles together
                    self.matrix[i][j] += self.matrix[i][j-1]
                    # and shifts the rest of the row
                    self.matrix[i][0:j] = [0] + self.matrix[i][0:j-1]
                elif self.matrix[i][j] == 0:
                    # if there is blank tile, shifts the slide of the rest of the row on the place of blank tile
                    self.matrix[i][0:j] = [0] + self.matrix[i][0:j-1]

    # public functions for realising appropriate movement of the main matrix and its consequences
    def to_down(self):
        # the actual = self.matrix[:][:] doesn't work because of shallow copy property
        # the actual var preserves the deepcopy of the main matrix before the movement
        actual = [ [cell for cell in row] for row in self.matrix ]
        # prints actual matrix shifted by some tabs (for debug purposes)
        # print("\n\t\t\t\t\t" + "\n\t\t\t\t\t".join(["{0}".format(row) for row in actual]))
        self.__rotate270()
        self.__move()
        self.__rotate90()
        self.__inform_or_generate_new_tile(actual)

    def to_up(self):
        actual = [ [cell for cell in row] for row in self.matrix ]
        self.__rotate90()
        self.__move()
        self.__rotate270()
        self.__inform_or_generate_new_tile(actual)

    def to_right(self):
        actual = [ [cell for cell in row] for row in self.matrix ]
        self.__move()
        self.__inform_or_generate_new_tile(actual)

    def to_left(self):
        actual = [ [cell for cell in row] for row in self.matrix ]
        self.__rotate180()
        self.__move()
        self.__rotate180()
        self.__inform_or_generate_new_tile(actual)


# The runtime of the game
arr = Array()
arr.print_matrix()
pressed_button = input().lower()

while not (pressed_button.startswith("exit", 0) or arr.no_possible_moves):
    # control flow
    if pressed_button == "w":
        arr.to_up()
        arr.print_matrix()
    elif pressed_button == "a":
        arr.to_left()
        arr.print_matrix()
    elif pressed_button == "d":
        arr.to_right()
        arr.print_matrix()
    elif pressed_button == "s":
        arr.to_down()
        arr.print_matrix()
    else:
        print()
        print("\033[1;33;40mTo manipulate the matrix, type w, s, a or d buttons. Type \"exit\" to end the game")
        print()
    pressed_button = input().lower()

print(f"Your score: {arr.score}")

# stops using colorama
colorama.deinit()

