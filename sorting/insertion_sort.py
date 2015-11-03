__author__ = 'tchitchikov'
"""
An insert sort will allow you to compare a single element to multiple at once
The first value is inserted into the sorted portion, all others remain in
the unsorted portion. The next value is selected from the unsorted array and
compared against each value in the sorted array and inserted in its proper
ascending or descending order depending on how you code this.
Run all values are in the sorted array.
"""
from base_class import Sort


class InsertSort(Sort):
    def sorting_process(self, input_array):
        """
        :return:
        """
        unsorted = input_array
        sorted_array = [input_array[0]]
        # unsorted_array.pop(0)  # look into making this a collections.deque object instead of a list
        # `i = 0
        # while i < len(unsorted_array):
        #     element = sorted_array[i]
        #     j = i + 1
        #     while ((j > 0) and (sorted_array[j-1] > element)):
        #         # sorted_array[j] = sorted_array[j-1]
        #         j = j - 1
        #     sorted_array.insert(j, element)
        #     i = i + 1
        #     print( i , j , element)`
        # return sorted_array
        i = 1
        while i < (len(unsorted)-1):
            x = unsorted[i]
            j = i
            while((j > 0) and (unsorted[j-1] > x)):
                unsorted[j] = unsorted[j-1]
                j = j -1
            unsorted[j] = x
            i = i + 1
        return unsorted


if __name__ == '__main__':
    sorting = InsertSort()
    sorting.main()
    print('Subclass: ', issubclass(InsertSort, Sort))
    print('Instance: ', isinstance(InsertSort(), Sort))
