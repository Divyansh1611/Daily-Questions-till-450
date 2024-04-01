'''
Ques :
    Sort an array of 0s, 1s and 2s
    MediumAccuracy: 50.58%Submissions: 636K+Points: 4
    Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.


    Example 1:

    Input:
    N = 5
    arr[]= {0 2 1 2 0}
    Output:
    0 0 1 2 2
    Explanation:
    0s 1s and 2s are segregated
    into ascending order.
    Example 2:

    Input:
    N = 3
    arr[] = {0 1 0}
    Output:
    0 0 1
    Explanation:
    0s 1s and 2s are segregated
    into ascending order.
'''
def sortArr(n):
    count_0 = count_1 = count_2 = 0
    for val in n:
        if val == 0:
            count_0 += 1
        elif val == 1:
            count_1 += 1
        else:
            if val == 2:
                count_2 += 1

    print('count 0 : {0}, count 1 : {1}, count 2 : {2}'.format(count_0, count_1, count_2))
    print('0 ' * count_0, end='')
    print('1 '* count_1, end='')
    print('2 ' * count_2, end='')



#Creating the Array
n = [0, 2, 1, 2, 0]
sortArr(n)


