# -*- coding: utf-8 -*-
"""
Created on Sat May 11 14:30:25 2024

@author: mikep
"""

import matplotlib.pyplot as plt

def collatz(n):
    return n//2 if n%2==0 else (3*n+1)//2

def get_xy_coordinates(number):
    ans = [0, 0]
    i = 1
    direction = 'u'
    steps_in_direction = 1
    while i < number:
        move = min(steps_in_direction, number - i)
        if direction == 'u':
            ans[1] = ans[1] + move
            direction = 'r'
            i = i + move
        elif direction == 'r':
            ans[0] = ans[0] + move
            direction = 'd'
            i = i + move
            steps_in_direction = steps_in_direction + 1
        elif direction == 'd':
            ans[1] = ans[1] - move
            direction = 'l'
            i = i + move
        elif direction == 'l':
            ans[0] = ans[0] - move
            direction = 'u'
            i = i + move
            steps_in_direction = steps_in_direction + 1
    return ans
        
def plot_square_spiral(numbers):
    points = [get_xy_coordinates(n) for n in numbers]
    ups = ['red' if numbers[n+1]>numbers[n] else 'blue' for n in range(len(numbers)-1)]
    ups.append('red')
    x_values = [points[p][0] for p in range(len(points))]
    y_values = [points[p][1] for p in range(len(points))]

    plt.figure(figsize=(8, 6))
    plt.scatter(x_values, y_values, color=ups, label='Sequence on a spiral')
    #for i in range(len(points)-1):
    #    plt.arrow(x_values[i], y_values[i], x_values[i+1]-x_values[i], y_values[i+1]-y_values[i], head_width=0.2, head_length=0.2, fc='green', ec='green')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Sequence on a spiral')
    plt.grid(True)
    plt.legend()
    plt.show()
    
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
    print('Maximum: ', max(a))
    plot_square_spiral(a)