def a_and_b(a,b):
    if a==1:
        prob_student = 0.3
        if b==1:
            prob_dining = 0.75
        else:
            prob_dining = 0.25
        print("probability of a given b:", prob_dining)

    if a==2:
        prob_student = 0.7
        if b==1:
            prob_dining = 0.6
        else:
            prob_dining = 0.4
        print("probability of a given b:", prob_dining)

    prob_a_and_b = prob_student*prob_dining
    return round (prob_a_and_b, 3)

print("check the probability of any event occuring. first enter your choices.")

print("is the student a freshman? \n 1. yes \n 2. no")
a = int(input("enter your choice (1/2): "))

print("is the student eating in dining hall? \n 1. yes \n 2. no")
b = int(input("enter your choice (1/2): "))

print("here is the probability of both the events occuring :", a_and_b(a,b))