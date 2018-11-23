# NATHANIEL LOUIS   TISUELA    30957483


import output
import sys


class Invalid_Jewel(Exception):
    '''Raises when invalid jewel is input'''
    pass

class columns_ui:

    def __init__(self):
        try:
            content = []
            self.rows = int(input())
            self.columns = int(input())
            command = input()
            if command == 'CONTENTS':
                content = self.content_list()
            elif command == 'EMPTY':
                pass
            else:
                print('INVALID INPUT')
                sys.exit()
            self.game = output.Columns_game(self.rows, self.columns, command, content)
        except:
            print('INPUT ERROR')
            sys.exit()


    def content_list(self):
        '''Gets content from user, creates it into list'''
        content_list = []
        for row in range(self.rows):
            row_input = input()
            row_list = []
            for element in row_input:
                row_list.append(element)
            content_list.append(row_list)

        return content_list

    def run_game(self):
        '''Runs commands in a loop'''
        while True:
            self.action()


    def action(self):
        '''Checks for commands'''
        user_input = input().split()
        try:
            if len(user_input) > 0:
                command = user_input[0]
            else:
                command = ''

            if command == 'F':
                self.faller_check(user_input[2:])
                self.construct_faller(user_input[1:])
                #self.game.passage_of_time()
            elif command == '>':
                self.game.move_faller_right()
            elif command == '<':
                self.game.move_faller_left()
            elif command == 'R':
                self.game.rotate_faller()
            elif command == '':
                self.game.passage_of_time()
            elif command == 'Q':
                sys.exit()
            else:
                print('INVALID COMMAND')
        except Invalid_Jewel:
            print('Invalid Jewel input, try again')
        except:
            print('Columns Error')
            sys.exit()


    def construct_faller(self, faller_info):
        '''Constructs faller'''
        column = int(faller_info[0]) - 1
        faller = []
        for jewel in faller_info[1:]:
            faller.append(jewel)
        self.game.create_faller(faller, column)


    def faller_check(self, faller_jewels):
        jewels = 'STVWXYZ'
        for jewel in faller_jewels:
            if jewel not in jewels:
                raise Invalid_Jewel

if __name__ == '__main__':
    columns_ui().run_game()