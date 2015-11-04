__author__ = 'tchitchikov'
"""
An insert sort will allow you to compare a single element to multiple at once
The first value is inserted into the sorted portion, all others remain in
the unsorted portion. The next value is selected from the unsorted array and
compared against each value in the sorted array and inserted in its proper
ascending or descending order depending on how you code this.
Run so all values are in the sorted array.
"""
from base_class import Sort


class InsertSort(Sort):
    def sorting_process(self, input_array):
        """
        Uses only a single list and compares the two indexed values
        """
        unsorted = input_array
        for index in range(1, len(unsorted)):
            value = unsorted[index]
            index_2 = index - 1
            while(index_2 >= 0 and unsorted[index_2] > value):
                unsorted[index_2+1] = unsorted[index_2]  # shift number in slot i to slot i + 1
                unsorted[index_2] = value  # shift value left into slot i
                index_2 = index_2-1
        return unsorted



if __name__ == '__main__':
    sorting = InsertSort()
    sorting.main()
    print('Subclass: ', issubclass(InsertSort, Sort))
    print('Instance: ', isinstance(InsertSort(), Sort))
