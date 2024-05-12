# -*- coding: utf-8 -*-
"""
Created on Sat May  4 21:46:04 2024

@author: mikep
"""

import matplotlib.pyplot as plt

def collatz(n):
    return n//2 if n%2==0 else (3*n+1)//2

def plot_integer_sequence(sequence, title='', log=False):
    if log:
        plt.semilogy(figsize=(8, 6))
    else:
        plt.figure(figsize=(8, 6))
    plt.plot(sequence, marker='o', color='green', linestyle='-')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title(title)
    plt.grid(True)
    plt.show()

if __name__=='__main__':
    n_iter = 2000
    a0 = 3
    maximums = []
    lengths = []
    for i in range(n_iter):
        print('\ni = ', int(i))
        a = []
        a.append(a0)
        while a0 != 1:
            a0 = collatz(a0)
            a.append(a0)
        #print('\nCollatz sequence: ', a)
        l = len(a) - 1
        lengths.append(l)
        print('Number of steps to 1: ', l)
        # Get a maximum of a Collatz sequence
        m = max(a)
        maximums.append(m)
        print('Maximum: ', m)
        # Do something to the maximum to increase the chances of getting stronger numbers
        a0 = 3*m+1
        print('Starting new iteration from ', a0)

    #plot_integer_sequence(maximums, title='Maximums', log=True)
    plot_integer_sequence(lengths, title='Lengths', log=False)