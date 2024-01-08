import random

still = True

with open('words.txt', encoding='utf-8') as f:
    read = f.readlines()

while still:
    correct = random.choice(read)
    correct = correct.split(":")

    qustion = correct[1]
    
    correct = str(correct[0])

    '''
    first = random.choice(read)
    first = first.split(":")
    first = first[0]

    
    second = random.choice(read)
    second = second.split(":")
    second = second[0]

    
    third = random.choice(read)
    third = third.split(":")
    third = third[0]

    choices = [correct, first, second, third]
    random.shuffle(choices)

    print(qustion)
    for i in choices:
        print(i)
    '''
    print(qustion)
    answer = input("type your answer: ")
    
    while answer not in correct:
        if answer == "stop":
            still = False
            break
            
        if answer == "answer" or answer == None:
            print(correct)
            
        
        answer = input("try again! ")

    print("well done!")
    print("-----------------------------")