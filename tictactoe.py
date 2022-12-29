#!/usr/bin/python3
#! encoding: utf-8
import os

data =[[' ', ' ', ' '],
       [' ', ' ', ' '],
       [' ', ' ', ' ']]

def show_data():
    os.system('cls||clear')
    print(data[0][0] + '|' + data[0][1] + '|' + data[0][2])
    print(data[1][0] + '|' + data[1][1] + '|' + data[1][2])
    print(data[2][0] + '|' + data[2][1] + '|' + data[2][2])

def check_win():
    #columns
    if data[0][0] == data[1][0] and data[0][0] == data[2][0]:
        if data[0][0] != ' ' and data[1][0] != ' ' and data [2][0] != ' ':
            print(data[0][0] + ' WIN')
            exit(0)
    if data[0][1] == data[1][1] and data[0][1] == data[2][1]:
        if data[0][1] != ' ' and data[1][1] != ' ' and data [1][2] != ' ':
            print(data[0][1] + ' WIN')
            exit(0)
    if data[0][2] == data[1][2] and data[0][2] == data[2][2]:
        if data[0][2] != ' ' and data[1][2] != ' ' and data [2][2] != ' ':
            print(data[0][2] + ' WIN')
            exit(0)
    #rows
    if data[0][0] == data[0][1] and data[0][0] == data[0][2]:
        if data[0][0] != ' ' and data[0][1] != ' ' and data [0][2] != ' ':
            print(data[0][2] + ' WIN')
            exit(0)
    if data[1][0] == data[1][1] and data[0][0] == data[1][2]:
        if data[1][0] != ' ' and data[1][1] != ' ' and data [1][2] != ' ':
            print(data[0][2] + ' WIN')
            exit(0)
    if data[2][0] == data[2][1] and data[0][0] == data[2][2]:
        if data[2][0] != ' ' and data[2][1] != ' ' and data [2][2] != ' ':
            print(data[2][0] + ' WIN')
            exit(0)
    #diagonal
    if data[0][0] == data[1][1] and data[0][0] == data[2][2]:
        if data[0][0] != ' ' and data[1][1] != ' ' and data [2][2] != ' ':
            print(data[2][2] + ' WIN')
            exit(0)
    if data[2][0] == data[1][1] and data[2][0] == data[0][2]:
        if data[2][0] != ' ' and data[1][1] != ' ' and data [0][2] != ' ':
            print(data[1][1] + ' WIN')
            exit(0)


def X():
    x_column = (input('X column ==> '))
    x_row = input('X row ==> ')
    if data[int(x_row)-1][int(x_column)-1] != '0':
        data[int(x_row)-1][int(x_column)-1] = 'X'
    else:
        show_data()
        print('SPACE NOT EMPTY')
        X()
    show_data()
    check_win()

def O():
    o_column = (input('0 column ==> '))
    o_row = input('0 row ==> ')

    if data[int(o_row)-1][int(o_column)-1] != 'X':
        data[int(o_row)-1][int(o_column)-1]  = '0'
    else:
        show_data()
        print('SPACE NOT EMPTY')
        O()
    show_data()
    check_win()

def main():
    while True:
        X()
        O()
        
if __name__ == '__main__':
    show_data()
    main()