import random
X =[]
Y =[]

def main():
    try:
        repetitions = 1
        mistakes = 0
        generate_integer(get_level())
        for i in range (10):
            result = int(input(f"{X[i]} + {Y[i]} = "))
            while result  != X[i]+Y[i]:
                if repetitions == 3:
                    mistakes += 1
                    print(f"{X[i]} + {Y[i]} = {X[i]+Y[i]}")
                    break
                print("EEE")
                result  = int(input(f"{X[i]}+{Y[i]} = "))
                repetitions += 1
        print(f"{10-mistakes}")
    except ValueError:
        print("Invalid Input!")



def get_level():
    level = int(input("Level: "))
    while level not in[1,2,3]:
        level = int(input("Level: "))
    return level

def generate_integer(level):
    if level == 1:
        for _ in range (10):
            X.append(random.randint(0, 9))
            Y.append(random.randint(0, 9))
    elif level == 2:
        for _ in range (10):
            X.append(random.randint(10, 99))
            Y.append(random.randint(10, 99))
    elif level == 3:
        for _ in range (10):
            X.append(random.randint(100, 999))
            Y.append(random.randint(100, 999))
    return X,Y


if __name__ == "__main__":
    main()
