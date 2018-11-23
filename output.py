# NATHANIEL LOUIS   TISUELA    30957483


import columns_class
import sys

def print_game(field):

    for row in field:
        print(row)
    print()


class Columns_game:
    def __init__(self, rows, columns, command, contents):
        self.field = columns_class.Field(rows, columns)

        self.columns = columns
        self.faller_object = 'does not exist'
        self.get_field()

        if command == 'EMPTY':
            self.print_field()
            pass
        elif command == 'CONTENTS':
            self.field.input_field(contents)
            self.field.falling_jewel()
            self.get_field()
            self.format_matching_jewels()
            #print_game(self.field.field_list)



    def create_faller(self, faller, column):
        '''Creates faller'''
        if self.faller_object == 'does not exist' or len(self.faller_object.faller) == 0:
            self.field.construct_faller(faller, column)
            self.faller_object = self.field.return_faller_object()
            self.passage_of_time()

        else: #consider moving these checks to mechanics
            self.print_field()

    def passage_of_time(self):
        '''Passage of time'''
        if self.faller_object != 'does not exist':


            if self.faller_object.faller != []:
                self.field.falling_faller()

            self.format_jewels()

            if self.field.check_game_over():
                print('GAME OVER')
                sys.exit()


        else:
            self.format_matching_jewels()

    def move_faller_left(self):
        '''Moves faller left'''
        self.field.move_faller_left()
        self.format_jewels()

    def move_faller_right(self):
        '''Moves faller right'''
        self.field.move_faller_right()
        self.format_jewels()


    def rotate_faller(self):
        '''rotates faller'''
        self.field.rotate_faller()
        self.format_jewels()


    def get_field(self):
        '''creates copy of field_list to be formatted'''
        self.format_list = []
        for row in self.field.field_list:
            row_list = []
            for element in row:
                row_list.append(element)
            self.format_list.append(row_list)


    def format_jewels(self):
        '''Formats all jewels, prints result'''
        self.get_field()

        faller_index = self.faller_object.return_faller_index()

        faller_state = self.faller_object.is_faller_static()

        if faller_state['can_fall'] or faller_state['landed']:
            self.format_falling_faller(faller_index, faller_state)
            self.print_field()

        else:
            self.format_matching_jewels()


    def format_falling_faller(self, faller_index, faller_state):
        '''Adds appropriate characters around faller'''

        if faller_state['can_fall']:
            wrap1 = '['
            wrap2 = ']'

        elif faller_state['landed']:
            wrap1 = '|'
            wrap2 = '|'

        else:
            wrap1 = ' '
            wrap2 = ' '

        self.format_list[faller_index[0][0]][(faller_index[0][1])] = wrap1 + self.field.faller[0] + wrap2
        self.format_list[faller_index[1][0]][(faller_index[1][1])] = wrap1 + self.field.faller[1] + wrap2
        self.format_list[faller_index[2][0]][(faller_index[2][1])] = wrap1 + self.field.faller[2] + wrap2


    def format_matching_jewels(self):
        '''Formats matching jewes'''
        if len(self.field.matched_jewel()) > 0:
            for jewel_index in self.field.matched_jewel():
               self.format_list[jewel_index[0]][jewel_index[1]] = (
                   '*' + self.format_list[jewel_index[0]][jewel_index[1]] + '*') #adds asterics to matched jewels

        self.print_field()

        self.field.remove_match() #remove matches
        self.field.falling_jewel()  # makes jewels fall
        self.get_field() #prepares for printing


    def print_field(self):
        '''Prints field_list'''
        for row in self.format_list[5:]:
            print_row = '|'
            for element in row:
                if len(element) == 1:
                    element = ' ' + element + ' '
                print_row += (element)
            print_row += '|'
            print(print_row)

        print(' '+ ('---' * self.columns) + ' ')
        #print()