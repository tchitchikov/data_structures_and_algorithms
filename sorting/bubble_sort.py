__author__ = 'tchitchikov'
"""
A bubble sort will allow you to compare two elements in an array.
If the first value is larger than the next, it swaps positions.
Once it encounters a value larger than it, it stops.
Then go back to the beginning of the array and select the next element
Repeat the process until all elements have been sorted
"""


class BubbleSort:
    def __init__(self):
        self.array = []

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

    def sorting_process(self, input_array):
        """
        Compare each number to the next and swap positions.
        input_array(list) = list of numbers to be sorted
        :return:
        """
        for i in range(len(input_array)-1, 0, -1):
            for j in range(len(input_array)-1):
                if input_array[j] > input_array[j+1]:
                    input_array[j], input_array[j+1] = input_array[j+1], input_array[j]
        return input_array


if __name__ == '__main__':
    sorting = BubbleSort()
    sorting.main()