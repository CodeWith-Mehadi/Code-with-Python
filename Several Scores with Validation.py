def get_valid_score():
    while True:
        score = float(input())
        if 0 <= score <= 10:
            return score
        else:
            print("nota invalida")


def calculate_average():
    score1 = get_valid_score()
    score2 = get_valid_score()
    average = (score1 + score2) / 2
    print(f"media = {average:.2f}")


while True:
    calculate_average()
    while True:
        print("novo calculo (1-sim 2-nao)")

        choice = int(input())
        if choice == 1:
            break
        elif choice == 2:
            exit()