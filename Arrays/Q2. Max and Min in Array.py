
if __name__ == '__main__':
    arr = [2, 4, 5, 9, 74, 54]
    # we can use sort the array and then find the max and min out of it
    # for sorting we can use Merge Sort which gave nlog(n) TC

    arr.sort()
    max, min = arr[len(arr)-1], arr[0]
    print('The max is {0} and min is {1}'. format(max, min))