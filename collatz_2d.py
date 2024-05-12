# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 10:52:08 2024

@author: mikep
"""

import matplotlib.pyplot as plt

def collatz(n):
    return n//2 if n%2==0 else (3*n+1)//2

def plot_integer_sequence(sequence):
    plt.figure(figsize=(8, 6))
    plt.plot(sequence, marker='o', color='green', linestyle='-')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Collatz sequence')
    plt.grid(True)
    plt.show()

def plot_consecutive_pairs(numbers):
    x_values = numbers[:-1]  # Get all but the last element
    y_values = numbers[1:]   # Get all but the first element

    plt.figure(figsize=(8, 6))
    plt.scatter(x_values, y_values, color='blue', label='Pairs')
    for i in range(len(numbers)-2):
        plt.arrow(numbers[i], numbers[i+1], numbers[i+1]-numbers[i], numbers[i+2]-numbers[i+1], head_width=0.2, head_length=0.2, fc='red', ec='red')
    plt.xlabel('First number')
    plt.ylabel('Second number')
    plt.title('Consecutive pairs')
    plt.grid(True)
    plt.legend()
    plt.show()
    
def count_upward_steps(a):
    ans = 0
    for i in range(len(a)-1):
        if a[i+1] > a[i]:
            ans = ans + 1
    return ans
            
def count_downward_steps(a):
    ans = 0
    for i in range(len(a)-1):
        if a[i+1] < a[i]:
            ans = ans + 1
    return ans

if __name__=='__main__':
    # Storing variables
    a = []
    # Script
    a0 = int(input('Input starting number: '))
    a.append(a0)
    while a0 != 1:
        a0 = collatz(a0)
        a.append(a0)
    # Reports
    print('Collatz sequence: ', a)
    print('Number of steps to 1: ', len(a)-1)
    up = count_upward_steps(a)
    print('Number of upward steps: ', up)
    down = count_downward_steps(a)
    print('Number of downward steps: ', down)
    print('Up/down: ', up/down)
    print('Maximum: ', max(a))
    print('Sum: ', sum(a))
    plot_integer_sequence(a)
    plot_consecutive_pairs(a)