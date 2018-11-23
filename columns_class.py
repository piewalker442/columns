# NATHANIEL LOUIS   TISUELA    30957483
# GAME MECHANICS



class Field:
    def __init__(self, rows: int, columns: int, ):
        self.rows = rows
        self.columns = columns

        '''Defining variables in advance to prevent NameAttribute errors'''

        self.field_list = []
        self.faller = []
        self.true_match = set()
        self.faller_index = []
        self.faller_object = None

        for row in range(self.rows + 5):
            '''Created game board with FIVE EXTRA rows on top
            These extra rows is where new fallers are born and 
            also serves to prevent matching and falling errors w
            when dealing with jewels outside the DISPLAYED field'''
            row_list = []
            for column in range(self.columns):
                row_list.append(' ')
            self.field_list.append(row_list)

    def input_field(self, manual_field: list):  # use BEFORE constructing faller
        '''Inputs CONTENTS for user-inputted field'''
        del self.field_list[5:]
        self.field_list.extend(manual_field)

    def return_faller(self):
        '''Returns faller as recorded in FIELD class'''
        return self.faller

    def return_field(self):
        '''Returns field 2D list'''
        return (self.field_list)


    ##### executes action if allowed by state #####


    def construct_faller(self, faller: list, faller_column: int):  # Construct AFTER field has no falling jewels
        '''Creates Faller object and inserts it into the field'''
        if self.faller_index == []:  # remove this
            self.faller_object = Faller(self.field_list, faller, faller_column)  # refers to class object itself

            self.faller = faller

            faller_jewel_index = 0
            for row in self.field_list[:3]:
                row[faller_column] = faller[faller_jewel_index]
                faller_jewel_index += 1

            self.falling_faller()
            self.falling_faller()


    def falling_jewel(self):  # prevent out of range errors
        '''Makes all jewels fall to the point where they can no longer fall'''

        row_index = -1
        for row in self.field_list:
            row_index += 1
            column_index = -1
            for element in row:
                column_index += 1
                try:
                    above_element = self.field_list[(row_index - 1)][column_index]

                    if len(above_element.strip()) == 1 and row_index != 0 and \
                            element == ' ': #index not 0 to prevent errors
                        '''if the above element is a jewel and the current element is an empty space'''

                        for index in range(row_index)[1:]:
                            '''makes above element – the jewel – fall'''
                            above = self.field_list[(row_index - index)][column_index]
                            self.field_list[(row_index) + (1 - index)][column_index] = above

                except IndexError:  # do nothing if index is out of range – jewel stays frozen
                    '''My game mechanics work so that an index error means that
                    the jewel in concern can no longer fall anyway'''
                    pass



    def matched_jewel(self):
        '''Returns matched jewels'''
        self.true_match = Jewel(self.field_list).match_made()
        return self.true_match



    def remove_match(self):
        '''Removes matches from list'''
        for jewel_index in self.true_match:
            self.field_list[jewel_index[0]][jewel_index[1]] = ' '
        self.true_match = set()


    def rotate_faller(self):
        '''Rotates faller in the FIELD'''
        if len(self.faller_object.return_faller()) != 0:  # to ensure that faller exists
            faller_index = self.faller_object.return_faller_index()
            self.faller_object.rotate_faller()

            self.field_list[faller_index[0][0]][faller_index[0][1]] = self.faller[0]
            self.field_list[faller_index[1][0]][faller_index[1][1]] = self.faller[1]
            self.field_list[faller_index[2][0]][faller_index[2][1]] = self.faller[2]

    def move_faller_left(self):
        '''Moves faller left'''
        faller_index = self.faller_object.return_faller_index()
        if self.faller_object.can_faller_move_left():
            ### insert faller to the left ###
            self.field_list[faller_index[0][0]][(faller_index[0][1] - 1)] = self.faller[0]
            self.field_list[faller_index[1][0]][(faller_index[1][1] - 1)] = self.faller[1]
            self.field_list[faller_index[2][0]][(faller_index[2][1] - 1)] = self.faller[2]

            ### replace faller with ' ' in original column ###
            self.field_list[faller_index[0][0]][(faller_index[0][1])] = ' '
            self.field_list[faller_index[1][0]][(faller_index[1][1])] = ' '
            self.field_list[faller_index[2][0]][(faller_index[2][1])] = ' '

            self.faller_object.left_index_update()

    def move_faller_right(self):
        '''Moves faller right'''
        faller_index = self.faller_object.return_faller_index()
        if self.faller_object.can_faller_move_right():
            ### insert faller to the right ###
            self.field_list[faller_index[0][0]][(faller_index[0][1] + 1)] = self.faller[0]
            self.field_list[faller_index[1][0]][(faller_index[1][1] + 1)] = self.faller[1]
            self.field_list[faller_index[2][0]][(faller_index[2][1] + 1)] = self.faller[2]

            ### replace faller with ' ' in original column ###
            self.field_list[faller_index[0][0]][(faller_index[0][1])] = ' '
            self.field_list[faller_index[1][0]][(faller_index[1][1])] = ' '
            self.field_list[faller_index[2][0]][(faller_index[2][1])] = ' '

            self.faller_object.right_index_update()

    def falling_faller(self):
        '''Allows faller to fall'''
        faller_index = self.faller_object.return_faller_index()
        if self.faller_object.can_faller_fall():
            self.field_list[faller_index[0][0]][faller_index[0][1]] = ' '  # changes top faller to empty string
            self.field_list[faller_index[1][0]][faller_index[1][1]] = self.faller[
                0]  # changes middle faller to top faller
            self.field_list[faller_index[2][0]][faller_index[2][1]] = self.faller[
                1]  # changes bottom faller to middle faller
            self.field_list[(faller_index[2][0] + 1)][faller_index[1][1]] = self.faller[
                2]  # changes column of row below bottom faller to bottom faller

            self.faller_object.falling_index_update()

    def return_faller_object(self):
        '''Returns the faller object that was created (or None if the object has not been created yet'''
        return self.faller_object

    def check_game_over(self):
        '''If there is no more matching jewels and the faller is frozen (to be more sure
        I check if the faller list is empty), this will check
        for jewels on top of the displayed field. If there are jewels, it will end
        the game'''
        if len(self.matched_jewel()) == 0 and self.faller_object.faller == []:
            for element in self.field_list[4]:
                if element != ' ':
                    return True

        return False


class Jewel:
    '''Keeps track of jewels in the field'''
    def __init__(self, field_list):
        self.field_list = field_list
        self.true_match = set()
        self.jewel_index = []
        self.match_list = []

        row_index = -1
        for row in self.field_list:
            '''Records index for every Jewel'''
            row_index += 1
            column_index = -1
            for column in row:
                column_index += 1
                if len(column.strip()) == 1:
                    self.jewel_index.append((row_index, column_index))

    def return_jewel_index(self):
        return self.jewel_index


    ##### matchmaker <3 #####


    def match_find(self):
        '''Finds every matching pair and puts its color, locations, and deltas into a tuple which then
        goes into a list'''
        self.match_list = []  # more like pair list

        for jewel in self.jewel_index:
            jewel_row = jewel[0]
            jewel_column = jewel[1]
            start_jewel_value = self.field_list[jewel[0]][jewel[1]]

            for potential_match in self.jewel_index:
                '''Looks for potential matches'''
                potential_match_row = potential_match[0]
                potential_match_column = potential_match[1]
                potential_match_value = self.field_list[potential_match[0]][
                    potential_match[1]]  # gets match value/colour
                row_delta = (jewel_row - potential_match_row)
                column_delta = (jewel_column - potential_match_column)

                if (-1 <= row_delta <= 1) and (-1 <= column_delta <= 1) and potential_match != jewel and (
                        potential_match_value == start_jewel_value):
                    '''Checks if the potential match is a match, and is not itself'''

                    match = potential_match

                    self.match_list.append((start_jewel_value, jewel, match, row_delta, column_delta))

        return self.match_list

    def match_made(self):
        '''From the pairs of matches we got in the previous function, match_find, we now look for legitimate
        matches, that is, matches that contain more than 3 jewels with the same delta values'''
        self.true_match = set() #using a set will get rid of duplicates

        for pair in self.match_find():
            '''Extracts tuples returned from match_find'''
            index1 = pair[1]
            index2 = pair[2]
            row_delta = pair[3]
            column_delta = pair[4]

            for other_pair in self.match_list:
                '''If another pair matches with the former pair, we know that these series of jewels are a legitimate
                match and we will record their indexes... It should be noted that one of the indexes from each pair
                should reference the same Jewel'''
                other_index1 = other_pair[1]
                other_index2 = other_pair[2]
                other_row_delta = other_pair[3]
                other_column_delta = other_pair[4]
                if (index1 == other_index2 or index2 == other_index1) and \
                        (row_delta == other_row_delta and column_delta == other_column_delta) and \
                        (pair[0] == other_pair[0]):
                    self.true_match.update({index1, index2, other_index1, other_index2})

        return self.true_match


class Faller:

    def __init__(self, field_list, faller: list, faller_column):
        '''list of index tuples for each jewel of the faller, ordered from top to bottom
        Each tuple is ordered (row index, column index)
        Each faller jewel should have the same column index
        '''
        self.faller_index = []
        self.field_list = field_list
        self.faller = faller
        self.under_faller_row = []

        self.can_fall = None

        self.faller_index = []
        self.faller = faller
        row_index = 0

        for row in self.field_list[:3]:
            self.faller_index.append((row_index, faller_column))
            row_index += 1

    def return_faller(self):
        '''Returns faller. This is the Source of Truth when dealing with the faller list values'''
        return self.faller

    def return_faller_index(self):
        '''Returns the index of each jewel in the faller in order'''
        return self.faller_index


    ####### obtain what is around the faller (if there is a faller) ########


    def get_under_faller_row(self):  # change to check around faller
        '''gets row under faller'''
        try:
            if self.faller_index != []:
                bottom_faller_jewel = self.faller_index[-1]
                faller_row = bottom_faller_jewel[0]
                faller_column = bottom_faller_jewel[1]  # do I really need this??
                self.under_faller_row = self.field_list[(faller_row + 1)]
            else:
                self.under_faller_row = []
        except IndexError:
            self.under_faller_row = []


    def get_column_left(self):
        '''gets column element to the left of the bottom faller jewel, and the element under the former element as well'''
        try:
            if self.faller_index != [] and self.under_faller_row != []:
                bottom_faller_jewel = self.faller_index[-1]
                self.left_faller_element = self.field_list[bottom_faller_jewel[0]][(bottom_faller_jewel[1] - 1)]
                self.under_left_faller_element = self.under_faller_row[(bottom_faller_jewel[1] - 1)]

                if self.faller_index[-1][1] == 0:  # review this
                    self.left_faller_element = ''
                    self.under_left_faller_element = ''

            else:
                self.left_faller_element = ''
                self.under_left_faller_element = ''

        except IndexError:
            self.left_faller_element = ''
            self.under_left_faller_element = ''


    def get_column_right(self):
        '''gets column element to the right of the bottom faller jewel, and the element under the former element as well'''
        try:
            if self.faller_index != [] and self.under_faller_row != []:
                bottom_faller_jewel = self.faller_index[-1]
                self.right_faller_element = self.field_list[bottom_faller_jewel[0]][(bottom_faller_jewel[1] + 1)]
                self.under_right_faller_element = self.under_faller_row[(bottom_faller_jewel[1] + 1)]

            else:
                self.right_faller_element = ''
                self.under_right_faller_element = ''

        except IndexError:
            self.right_faller_element = ''
            self.under_right_faller_element = ''

    ###### Assign state to what is around faller ######


    def under_faller_element_check(self):
        if len(self.under_faller_row) != 0 and len(self.faller_index) != 0:
            '''If under_faller_row list contains something, get the
            element under the faller'''
            bottom_faller_jewel_column = self.faller_index[-1][1]
            under_faller_element = self.under_faller_row[bottom_faller_jewel_column]

        else:
            '''If there's nothing in the under_faller_row list, then
            the element under the faller is also nothing (prevents 
            index error)'''
            under_faller_element = ''

        return under_faller_element


    def is_faller_static(self):  # consider changing the name
        '''Determines if faller is falling, landed or frozen'''
        self.get_under_faller_row()

        under_faller_element = self.under_faller_element_check()

        if under_faller_element != ' ' and self.can_fall:
            '''if the previous state of the faller was falling
            and the element underneath is not empty, then the faller
            has landed'''
            self.landed = True
            self.can_fall = False
            self.frozen = False

        elif under_faller_element == ' ':
            '''if the element underneath is empty then the faller
            can fall'''
            self.can_fall = True
            self.landed = False
            self.frozen = False

        else:
            '''In any other case, the faller is frozen'''
            self.can_fall = False
            self.landed = False
            self.frozen = True

        self.frozen_check()

        bool_dict = {'can_fall': self.can_fall, 'landed': self.landed,
                     'frozen': self.frozen}

        '''Returning a dict helps me check the the state of the faller outside of this class without having
        to run the method again'''

        return bool_dict


    def can_faller_fall(self):
        '''returns bool if the faller can fall'''
        self.is_faller_static()
        return self.can_fall


    def falling_index_update(self):
        '''Updates faller index whenever it falls'''

        index_count = 0

        for index in self.faller_index:
            column_index = index[1]
            row_index = index[0] + 1
            self.faller_index[index_count] = (row_index, column_index)
            index_count += 1


    def frozen_check(self):
        '''If faller is frozen, reset faller_index and faller lists'''
        if self.frozen:
            self.faller_index = []
            self.faller = []


    def can_faller_land(self):
        '''Returns bool if faller can land'''
        self.is_faller_static()
        return self.landed


    def can_faller_move_left(self):
        self.get_column_left()
        '''Determines if faller can move left'''
        if self.left_faller_element == '':
            self.can_move_left = False
            return self.can_move_left

        elif self.under_left_faller_element == ' ' and self.landed:
            self.can_move_left = True
            return self.can_move_left

        elif self.left_faller_element == ' ' and self.can_fall:
            self.can_move_left = True
            return self.can_move_left

        else:
            self.can_move_left = False
            return self.can_move_left


    def left_index_update(self):
        '''updates index when faller moves left'''
        index_count = 0

        for index in self.faller_index:
            column_index = index[1] - 1
            row_index = index[0]
            self.faller_index[index_count] = (row_index, column_index)
            index_count += 1


    def can_faller_move_right(self):
        self.get_column_right()
        '''Determines if faller can move right'''
        if self.right_faller_element == '':
            self.can_move_right = False
            return self.can_move_right

        elif self.under_right_faller_element == ' ' and self.landed:
            self.can_move_right = True
            return self.can_move_right

        elif self.right_faller_element == ' ' and self.can_fall:
            self.can_move_right = True
            return self.can_move_right

        else:
            self.can_move_right = False
            return self.can_move_right


    def right_index_update(self):
        '''updates index when faller moves right'''
        index_count = 0

        for index in self.faller_index:
            column_index = index[1] + 1
            row_index = index[0]
            self.faller_index[index_count] = (row_index, column_index)
            index_count += 1


    def rotate_faller(self):
        '''moves faller right'''
        faller1 = self.faller[0]
        faller2 = self.faller[1]
        faller3 = self.faller[2]

        self.faller[0] = faller3
        self.faller[1] = faller1
        self.faller[2] = faller2