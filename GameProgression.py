import random


def generate_geometric_sequence():
    start = random.randint(1, 10)
    ratio = random.randint(2, 5)
    length = random.randint(5, 10)
    sequence = [start * (ratio**i) for i in range(length)]
    return sequence


def hide_element(sequence):
    hidden_index = random.randint(0, len(sequence) - 1)
    hidden_value = sequence[hidden_index]
    sequence[hidden_index] = ".."
    return sequence, hidden_value


def play_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the geometric progression?")

    correct_answers = 0
    total_rounds = 3

    for _ in range(total_rounds):
        sequence = generate_geometric_sequence()
        sequence_with_hidden, hidden_value = hide_element(sequence)

        print("Question:", " ".join(map(str, sequence_with_hidden)))
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if user_answer == hidden_value:
            print("Correct!")
            correct_answers += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was '{hidden_value}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    play_game()
