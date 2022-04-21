#!/usr/bin/env python3

# Created by: Miguel Santacruz
# Created on: Apr 2022
# This program shows the square of every number between 0 and input


def main():
    # This function squares numbers

    # input
    string = input("Please enter a positive integer: ")

    # process & output
    print("")
    try:
        decimal = float(string)
        if decimal < 0:
            print("It is not positive :c")
        else:
            number = int(decimal)
            if decimal != number:
                print("{} is not an integer.".format(decimal))
            else:
                for loop_counter in range(number + 1):
                    answer = loop_counter * loop_counter
                    print("{0}² = {1}".format(loop_counter, answer))
    except Exception:
        print("{} is not a number.".format(string))

    print("\nDone.")


if __name__ == "__main__":
    main()
