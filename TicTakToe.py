import numpy as np


def print_arr(arr):
    for i in arr:
        print('|',end='')
        for j in i:
            if j == None:
                print('-',end=' ')
            else:
                print(j,end=' ')
        print('\b|')


def decide(arr):
    bool1 = []
    bool2 = [] 
    for  i,j,k in arr:
        bool1.append(i==j==k=='x')
        bool2.append(i==j==k=='0')
        
    for  i,j,k in arr.transpose():
        bool1.append(i==j==k=='x')
        bool2.append(i==j==k=='0')
    if arr[0,0]==arr[1,1]==arr[2,2]=='x' or arr[0,2]==arr[1,1]==arr[2,0]=='x':
        bool1.append(True)
    else :
        bool1.append(False)
    if arr[0,0]==arr[1,1]==arr[2,2]=='0' or arr[0,2]==arr[1,1]==arr[2,0]=='0':
        bool2.append(True)
    else:
        bool2.append(False)
        
   
    if any(bool1):
        print_arr(arr)
        print('Player  1  wins!')
        quit()
    if any(bool2):
        print_arr(arr)
        print('Player  2  wins!')
        quit()
    elif None not in arr:
        print('Draw!')
        print_arr(arr)
        quit()              


arr = np.array([
    [None,None,None],
    [None,None,None],
    [None,None,None]])
print_arr(arr)
print('Please Enter index to fill gaps!\n')


while True:
    while True:
        index = input('Player 1: ')
        try:
            if arr[eval(index)]==None:
                arr[eval(index)]='x'
                break;
            else:
                print('The Index is either already occupied or invalid!')
        except(IndexError,NameError):
           print('Enter proper Index-\n(For Example - 1,2 or 2,2 or 0,2...)')
    decide(arr)
    print_arr(arr)
    
    while True:
        index = input('Player 2: ')
        try:
            if arr[eval(index)]==None:
                arr[eval(index)]='0'
                break;
            else:
                print('The Index is either invalid or already occupied!')
        except(IndexError):
           print('Enter proper Index')
    decide(arr)
    print_arr(arr) 