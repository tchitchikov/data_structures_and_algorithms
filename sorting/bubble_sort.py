__author__ = 'tchitchikov'
"""
A bubble sort will allow you to compare two elements in an array.
If the first value is larger than the next, it swaps positions.
Once it encounters a value larger than it, it stops.
Then go back to the beginning of the array and select the next element
Repeat the process until all elements have been sorted
"""
from base_class import Sort


class BubbleSort(Sort):
    def sorting_process(self, input_array):
        """
        Compare each number to the next and swap positions.
        input_array(list) = list of numbers to be sorted
        :return:
        """
        for i in range(0, len(input_array)-1, 1):
            for j in range(len(input_array)-1):
                if input_array[j] > input_array[j+1]:
                    input_array[j], input_array[j+1] = input_array[j+1], input_array[j]
        return input_array


if __name__ == '__main__':
    sorting = BubbleSort()
    sorting.main()
    print('Subclass: ', issubclass(BubbleSort, Sort))
    print('Instance: ', isinstance(BubbleSort(), Sort))
