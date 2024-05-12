# -*- coding: utf-8 -*-
"""
Created on Sun May 12 07:48:04 2024

@author: mikep
"""

import matplotlib.pyplot as plt
import math

def naive_extended_collatz(n):
    '''
    Ignores the simple fact that we hit float precision with this...
    '''
    print("\n")
    print(math.floor(n))
    print(math.ceil(n))
    fn = math.floor(n)
    cn = math.ceil(n)
    if fn == cn:
        # we have an integer, but we still need execute an operation
        cn = cn + 1
    if fn%2 != 0:
        # floor is odd
        return (cn-n)*(3*n+1)+(n-fn)*(n/2)
    elif fn%2 == 0:
        # floor is even
        return (cn-n)*(n/2)+(n-fn)*(3*n+1)
    
def extended_collatz(p, q):
    '''
    Let's just do rational numbers for starters...
    '''
    print("\n")
    print('p =', p)
    print('q =', q)
    r = p%q
    a = (p-r)//q
    print('a =', a)
    print('r =', r)
    nenner = 2*q*q
    if a%2 != 0:
        zaehler = 2*(q-r)*(3*a*q+3*r+q)+r*(a*q+r)
    elif a%2 == 0:
        zaehler = (q-r)*(a*q+r)+2*r*(3*a*q+3*r+q)
    # divide by GCD
    g = math.gcd(zaehler, nenner)
    zaehler = zaehler//g
    nenner = nenner//g
    print('n -->', zaehler/nenner)
    return zaehler, nenner

def plot_sequence(sequence):
    plt.figure(figsize=(8, 6))
    plt.plot(sequence, marker='o', color='green', linestyle='-')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Sequence')
    plt.grid(True)
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
    c = []
    # Script
    p0 = int(input('Input starting p: '))
    q0 = int(input('Input starting q: '))
    c.append((p0,q0))
    i = 0
    max_iter = 10
    while p0 > q0 and i < max_iter:
        p0, q0 = extended_collatz(p0, q0)
        c.append((p0, q0))
        i = i + 1
    # Reports
    print('Collatz sequence: ', c)
    print('Number of steps to below 1 or max_iter: ', len(c)-1)
    #up = count_upward_steps(a)
    #print('Number of upward steps: ', up)
    #down = count_downward_steps(a)
    #print('Number of downward steps: ', down)
    #print('Up/down: ', up/down)
    #print('Maximum: ', max(a))
    #print('Sum: ', sum(a))
    cf = [(p-p%q)//q for p,q in c]
    plot_sequence(cf)
    input()
    
    # Experiment
    # See how high the sequence reaches if q0=1000 and p0 goes from 1001 to 1999
    print('Experiment with q0=1000 and p0=1001...1999')
    c10 = []
    q0 = 10000
    max_iter = 10
    for p0 in range(16160,16180):
        i = 0
        p = p0
        q = q0
        while i < max_iter:
            p, q = extended_collatz(p, q)
            i = i + 1
        c10.append(p/q)
    plot_sequence(c10)