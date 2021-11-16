# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 23:03:23 2021

@author: Johnson
"""

import my_tool as mt
import matplotlib.pyplot as plt

def my_test():      
    print("my tool")
    mt.clear_screen(30)
    input_file = input(print('Please indicates the file you like to process:(remeber to add the file suffix) '))
    data_t = mt.file_read_app(input_file)
    # print(data_t)
    date = mt.date_format(data_t)
    close = mt.close(data_t)
    mean = mt.mean(close)
    median = mt.median(close)
    updown = mt.up_down(close)
    gainloss = mt.gain_loss(close)
    print('The graph would be displayed at a new window')
    graph = mt.plot(date, close, mean, median, updown, gainloss)   
    output_file = input('Please indicates the file you would like to write in the result(.csv file):')
    write = mt.write(date, close, mean, median, updown, gainloss, output_file)
    check = mt.doublecheck(output_file)
    print('The result is shown above, please check if there is any problems')
    # xbar = mtb.mean(data)
    # print(f"{xbar:0.2f}")
    # med = mtb.median(data)
    # print(f"{med:0.2f}")
      
def main():
    my_test()
    
if __name__ == '__main__' :
    main()