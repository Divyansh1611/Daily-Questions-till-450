'''
Ques :-
Given an array arr[] and an integer K where K is smaller than size of array, the task is to find the Kth smallest element in the given array.
It is given that all array elements are distinct.

Note :-  l and r denotes the starting and ending index of the array.

Example 1:

Input:
N = 6
arr[] = 7 10 4 3 20 15
sorted [] = 3 4 7 10 15 20
K = 3
L=0 R=5

Output : 7
Explanation :
3rd smallest element in the given
array is 7.

Example 2:
Input:
N = 5

arr[] = 7 10 4 20 15
sorted arr [] = 4 7 10 15 20
K = 4 L=0 R=4

Output : 15

Explanation :
4th smallest element in the given
array is 15.
'''

if __name__ == '__main__':
    arr = [7, 10, 4, 20, 15]
    k = 4
    # first we sort the array
    arr.sort()
    print(arr[k-1])