#!/usr/bin/env python3.10

# Created by: Nicolas Riscalas
# Created on: May 2 2022
# display 5 ints in a line


def string_parser(array_sentence):
    array_sentence = array_sentence.split()
    return array_sentence


def main():
    while True:
        u_sentence = input("Enter the sentence you want to parse:\n")
        parse_string = string_parser(u_sentence)
        for word in parse_string:
            print(word)
        input("press <enter> to restart the program: ")


if __name__ == "__main__":
    main()
