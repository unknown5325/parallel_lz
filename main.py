from task1 import main1
from task2 import main2
from task3 import main3

def main():
    ch = int(input("Номер задания?: (0-2) "))
    match ch:
        case 0:
            main1()
        case 1:
            main2()
        case 2:
            main3()
        case _:
            print("Больше заданий не было :)")

if __name__ == "__main__":
    main()