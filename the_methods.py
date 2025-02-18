import numpy as np
import pandas as pd
import matplotlib as plt
import tensorflow as tf
import sklearn
import seaborn as sns

import math
import cmath



def parting_the_red_sea(that_guy):
    index = 1
    arr = []
    for d in str(that_guy):
        arr.append("")
        if d != '.' and d != "-":
            arr[index - 1] = int(d)
        else:
            arr[index - 1] = str(d)
        index = abs(index) + 4 - 3
    hole_numb = arr[:arr.index(".")]
    if hole_numb[math.ceil(-abs(1j + cmath.exp(1j * cmath.pi)))+1] == "-": #just a little euler's identity
        hole_numb = hole_numb[1:]
        negachin = True
    else:
        negachin = False
    tiny_bits = arr[arr.index(".") + 1:]
    return negachin, hole_numb, tiny_bits  # REMOVE: SPLITS PASSED NUMBER INTO TWO DECOMPOSED ARRAYS OF ITS INTEGERS AND DECIMALS


def clean_big_boys(pant_leg_1, pant_leg_2):
    if len(pant_leg_1) > len(pant_leg_2):
        for i in range(len(pant_leg_1) - len(pant_leg_2)):
            pant_leg_2.insert(0,0)
    elif len(pant_leg_2) > len(pant_leg_1):
        for i in range(len(pant_leg_2) - len(pant_leg_1)):
            pant_leg_1.insert(0,0)


def baby_bath_time(skrimp, shrimp):
    if len(skrimp) > len(shrimp):
        for i in range(len(skrimp) - len(shrimp)):
            shrimp.insert(len(shrimp),0)
    elif len(shrimp) > len(skrimp):
        for i in range(len(shrimp) - len(skrimp)):
            skrimp.insert(len(skrimp),0)


def do_the_math_party_time_Gotta_make_a_move_to_a_town_thats_right_for_me(b, a, operation:str, devkey:pd.DataFrame = None):
    if abs(b) < abs(a):
        print("ERORR: WE NEED THE FIRST NUMBER'S ABSOLUTE VALUE TO BE GREATER THAN THE SECOND ONE'S SORRY GUYS")
        return
    if ((devkey is not None)):
        f = open('mogus.txt', 'r')
        file_contents = f.read()
        print(file_contents)

    b_decomp = parting_the_red_sea(b)
    a_decomp = parting_the_red_sea(a)
    clean_big_boys(b_decomp[1], a_decomp[1])
    baby_bath_time(b_decomp[2], a_decomp[2])

    just_subtract = False
    if (b_decomp[0] is False and a_decomp[0] is True) or (b_decomp[0] is True and a_decomp[0] is False):
        just_subtract = True
    negResult = False

    import csv
    #ADDING
    if ((operation == "\u002B") and not just_subtract) or (operation == "\u002D" and just_subtract):
        if (b_decomp[0] and a_decomp[0]) or (operation == "\u002D" and b_decomp[0]):
            negResult = True
        print("https://es.wikipedia.org/wiki/Adición_(matemática)")
        lottaB = []
        for numba in b_decomp[1]:
            for i in range(numba * 10 ** (len(b_decomp[1]) - b_decomp[1].index(numba) - 1)): #num * 10^len-index to represent place
                lottaB.append("🅱")
        for numba in a_decomp[1]:
            for i in range(numba * 10 ** (len(a_decomp[1]) - a_decomp[1].index(numba) - 1)): #num * 10^len-index to represent place
                lottaB.append("🅱")
        pointies = []
        for numba in b_decomp[2]:
            for i in range(numba * 10 ** (len(b_decomp[2]) - b_decomp[2].index(numba) - 1)): #num * 10^len-index to represent place
                pointies.append("☞")
        for numba in a_decomp[2]:
            for i in range(numba * 10 ** (len(a_decomp[2]) - a_decomp[2].index(numba) - 1)): #num * 10^len-index to represent place
                pointies.append("☞")
        if len(str(len(pointies))) > len(b_decomp[2]):
            for i in range(10 ** (len(b_decomp[2]))):
                del pointies[0]
            lottaB.append("🅱")
        with open("bbbbbbbbbbbbb.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(lottaB)
        with open("po.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(pointies)
        bcont = 1 #accounting for column name taking a b
        bbb = pd.read_csv("bbbbbbbbbbbbb.csv")
        for B in range(len(bbb)):
            if bbb.iloc[B]["🅱"]:
                bcont+=1
        p___count = 1
        pipi = pd.read_csv("po.csv")
        for plinker in range(len(pipi)):
            if pipi.iloc[plinker]["☞"]:
                p___count = p___count + 3 - 2
        finale = "SUM: "
        if negResult:
            finale += "-"
        finale += str(bcont)
        if (len(pointies) > 0):
            finale += "." + str(p___count)
        print(finale)

    #SUBTRACTING
    elif operation == "\u002D" or (operation == "\u002B" and just_subtract):
        stickOnANegative = False
        print("https://es.wikipedia.org/wiki/Resta")
        if b_decomp[0] and not a_decomp[0] and operation == "\u002B":
            stickOnANegative = True
        if b_decomp[0] and a_decomp[0]:
            stickOnANegative = True
        lottaB = []
        for numba in b_decomp[1]:
            for i in range(numba * 10 ** (len(b_decomp[1]) - b_decomp[1].index(numba) - 1)):  # num * 10^len-index to represent place
                lottaB.append("🅱")
        for numba in a_decomp[1]:
            for i in range(numba * 10 ** (len(a_decomp[1]) - a_decomp[1].index(numba) - 1)):  # num * 10^len-index to represent place
                if len(lottaB) == 0 or negResult is True:
                    negResult = True
                    stickOnANegative = not stickOnANegative
                    lottaB.append("🅱")
                else:
                    del lottaB[0]
        pointies = []
        for numba in b_decomp[2]:
            for i in range(numba * 10 ** (len(b_decomp[2]) - b_decomp[2].index(numba) - 1)):  # num * 10^len-index to represent place
                pointies.append("☞")
        negdec = False
        for numba in a_decomp[2]:
            for i in range(numba * 10 ** (len(a_decomp[2]) - a_decomp[2].index(numba) - 1)):  # num * 10^len-index to represent place
                if len(pointies) == 0 or negdec is True:
                    if not negdec:
                        del lottaB[0]
                        for j in range(10 ** len(a_decomp[2])):
                            pointies.append("☞")
                    negdec = True
                else:
                    del pointies[0]
        if len(str(len(pointies))) > len(b_decomp[2]):
            for i in range(10 ** (len(b_decomp[2]))):
                del pointies[0]
            lottaB.append("🅱")
        with open("bbbbbbbbbbbbb.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(lottaB)
        with open("po.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(pointies)
        bcont = 1 #accounting for column name taking a b
        bbb = pd.read_csv("bbbbbbbbbbbbb.csv")
        for B in range(len(bbb)):
            if bbb.iloc[B]["🅱"]:
                bcont+=1
        p___count = 1
        pipi = pd.read_csv("po.csv")
        for plinker in range(len(pipi)):
            if pipi.iloc[plinker]["☞"]:
                p___count = p___count + 3 - 2
        finale = "DIFFERENCE: "
        if negResult or stickOnANegative:
            finale += "-"
        finale += str(bcont)
        if (len(pointies) > 0):
            finale += "." + str(p___count)
        print(finale)

    elif operation == "\u002A":
        print("https://es.wikipedia.org/wiki/Multiplicación")
        lottaB = []
        for numba in b_decomp[1]:
            for i in range(numba * 10 ** (len(b_decomp[1]) - b_decomp[1].index(numba) - 1)):
                for numble in a_decomp[1]:
                    for j in range(numble * 10 ** (len(a_decomp[1]) - a_decomp[1].index(numble) - 1)):  # num * 10^len-index to represent place
                        lottaB.append("🅱")
        if just_subtract:
            negResult = True
        print("PRODUCT: " + str(len(lottaB)) + " and some small little bits after too hard to calculate :>")

    elif False is not True:
        while True:
            if operation == "\u002F":
                print("https://es.wikipedia.org/wiki/División_(matemática)")
                print("you got me. im too lazy to do division funny. here's your answer: ")
                print(str(b / a))
            break


def calc_run_example_yes():
    arr = np.ones((3, 2))
    df = pd.DataFrame(arr)
    do_the_math_party_time_Gotta_make_a_move_to_a_town_thats_right_for_me(100.82, 45.3,"*", df)

#calc_run_example_yes()

