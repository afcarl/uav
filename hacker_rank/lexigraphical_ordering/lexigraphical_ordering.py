import sys
from itertools import permutations

def find_new_arrangement(word):
    other_arrangements = [''.join(p) for p in permutations(word)]
    if 1 == len(set(list(word))):
        return "no answer"
    min_arrangement = "z"*101
    for arrangement in other_arrangements:
        if arrangement > word:
            if arrangement < min_arrangement:
                min_arrangement = arrangement
    return min_arrangement

def next_permutation(arr):
    arr = list(arr)
    # Find non-increasing suffix
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return False
    
    # Find successor to pivot
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]
    
    # Reverse suffix
    arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
    return arr

def fact(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
        
def permute(string, listing,step = 0):
    # if we've gotten to the end, print the permutation
    if step == len(string):
        print("".join(string))
        
    # everything to the right of step has not been swapped yet
    for i in range(step, len(string)):

        # copy the string (store as array)
        string_copy = [character for character in string]

        # swap the current index with the step
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]

        # recurse on the portion of the string that has not been swapped yet (now it's index will begin with step + 1)
        permutations(string_copy, step + 1)        
    
    
size = int(input().strip())
words = []
for _ in range(size):
    words.append(input().strip())


for word in words:
    exists = next_permutation(word[:])
    if exists:
        print("".join(exists))
    else:
        print("no answer")
    
    
    
    

