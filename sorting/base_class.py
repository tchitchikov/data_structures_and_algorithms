# Abstract Base Class from which other classes will inherit. Handles input
from abc import abstractmethod
import abc


class Sort:
    def main(self):
        """
        handles the main logic

        :return:
        """
        input_array = self.handle_input()
        print(self.sorting_process(input_array))

    def handle_input(self):
        '''
        This method takes the user input and ensures it is in the
            expected format and type.
        array_input(string) = string of numbers input by the user
        array(list) = output of splitting the user string into a list of ints
        :return:
        '''
        array_input = input('Please enter a series of numbers '
                            'separated by spaces\n')
        for input_number in array_input.split():
            try:
                int(input_number)
                self.array += [int(input_number)]
            except:
                raise ValueError('You did not enter a series of numbers, '
                                 'please try again')
        return self.array

    @abstractmethod
    def sorting_process(self, input_array):
        """
        This is where the sorting algorithm goes.
        """
        return None
