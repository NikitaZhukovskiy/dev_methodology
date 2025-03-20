import math
import random


def gcd(a, b):
    """наибольший общий делитель"""
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """наименьшее общее кратное"""
    return a * b // gcd(a, b)


def lcm_three(a, b, c):
    return lcm(lcm(a, b), c)


def generate_numbers():
    return [random.randint(1, 50) for _ in range(3)]


def play_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the smallest common multiple of given numbers.")

    total_rounds = 3
    correct_answers = 0

    for _ in range(total_rounds):
        numbers = generate_numbers()
        correct_answer = lcm_three(*numbers)

        print(f"Question: {' '.join(map(str, numbers))}")
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    play_game()
