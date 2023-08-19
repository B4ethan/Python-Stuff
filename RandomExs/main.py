#this project contains random exercises from this website: https://www.w3resource.com/python-exercises/puzzles/index.php

#Ex1
def puzzle1(array):
    #write a python program to find a list of integers with exactly two occurrences of 19 and at least three occurrences of five
    count19 = 0
    count5 = 0

    for num in array:
        if num == 19:
            count19+=1
        elif num == 5:
            count5+=1

    return count19 == 2 and count5>=3

#other option
def puzzle1_2(array):
    return array.count(19) == 2 and array.count(5)>=3


#Ex2
def puzzle2(array):
    return len(array) == 8 and array.count(array[5]) == 3


#Ex3


def main():
    print("hello world!")


if __name__ == "__main__":
    main()
