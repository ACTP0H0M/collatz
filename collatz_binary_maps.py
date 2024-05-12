# -*- coding: utf-8 -*-
"""
Created on Sun May  5 08:31:41 2024

@author: mikep
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import warnings
warnings.filterwarnings("ignore")

def collatz_step(binary_str):
    # 1. Append 1 to the (right) end of the number in binary
    binary_str_1 = binary_str + '1'
    # 2. Add this to the original number by binary addition
    bin_sum = binary_addition(binary_str, binary_str_1)
    # 3. Remove all trailing 0s (repeatedly divide by 2 until the result is odd)
    while bin_sum[-1] == '0':
        bin_sum = bin_sum[:-1]
    return bin_sum

def binary_addition(a, b):
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    carry = 0
    Binary_sum_result = ''
    for i in range(max_len - 1, -1, -1):
        bit_sum = carry + int(a[i]) + int(b[i])
        Binary_sum_result = str(bit_sum % 2) + Binary_sum_result
        carry = bit_sum // 2
    if carry != 0:
        Binary_sum_result = str(carry) + Binary_sum_result
    return Binary_sum_result

if __name__=='__main__':
    #a0 =  9745314011399999080353382387875188310876226857595007526867906457212948690766426102465615061097944526161493942649523510564670493573961118829912009529308256902195634774774063827363870013528097052606786461479348919502220656534396499051930369252365519668227957601483439393766301515514501922817
    #a0 = 9999999999999999999999999999999999999999999999999999999999999999999999
    a0 = 6171
    steps = 100
    size = 100
    ev = []
    #evolution = np.zeros((steps, size), dtype=np.int8)
    assert a0%2 == 1
    binary_str = np.binary_repr(a0)
    
    # direct binary input (to create regularities easier)
    #binary_str = '11111111111111111111111111111111111111111111111111111111111111111111111111111111101'
    assert binary_str[-1] == '1'
    
    i = 0
    ev.append(binary_str)
    #evolution[0] = np.array([int(b) for b in binary_str.zfill(size)])
    while binary_str != '1':
        i = i + 1
        #if i == steps:
        #    break
        binary_str = collatz_step(binary_str)
        ev.append(binary_str)
        #evolution[i] = np.array([int(b) for b in binary_str.zfill(size)])
    
    steps = i+1
    sizes = [len(x) for x in ev]
    size = max(sizes)+1
    evolution = np.zeros((steps, size), dtype=np.int8)
    for i in range(len(ev)):
        evolution[i] = np.array([int(b) for b in ev[i].zfill(size)])
    
    fig = plt.figure(figsize=(10, 10))
    
    ax = plt.axes()
    ax.set_axis_off()
    
    ax.imshow(evolution, interpolation='none',cmap='RdPu')
    plt.savefig('cellular_automaton.png', dpi=300, bbox_inches='tight')