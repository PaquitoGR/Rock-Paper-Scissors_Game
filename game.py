from enum import Enum

# User choices
class GameChoice(Enum):
    INVALID = -1
    PAPER = 0
    ROCK = 1
    SCISSORS = 2
    LIZARD = 3
    SPOCK = 4
    QUIT = 5


def game_loop():
    """
    Arranca el bucle principal del juego
    """
    while True:
        # Leo la selección del usuario (piedra, papel, tijera o parar el juego)
        user_choice = read_user_choice()
        # Siempre y cuando no quiera parar
        if not is_exit(user_choice):
            # genero una jugada del ordenador
            comp_choice = generate_computer_choice()
            # evalúo la jugada
            result = evaluate_move(user_choice, comp_choice)
            print("I choose...", comp_choice.name)
            # muestro el ganador en pantalla y vuelta al principio
            print_result(result)
            input("Press ENTER to continue...")
        else:
            # el humano es un gallina: salgo
            break


def read_user_choice() -> GameChoice:
    """
    Lee una selección del usuario (piedra, papel, tijera o salir) y
    la devuelve
    """
    user_choice = GameChoice.INVALID
    while user_choice == GameChoice.INVALID:
        print("\nSelect one number:")
        print(f'{GameChoice.PAPER.value}. Paper')
        print(f'{GameChoice.ROCK.value}. Rock')
        print(f'{GameChoice.SCISSORS.value}. Scissors')
        print(f'{GameChoice.LIZARD.value}. Lizard')
        print(f'{GameChoice.SPOCK.value}. Spock')
        print("---------------------------")
        print(f'{GameChoice.QUIT.value}. Quit the game\n\n')

        try:
            user_choice = GameChoice(int(input("Enter your choice: ")))
        except ValueError:
            user_choice = GameChoice.INVALID

    return user_choice



def is_exit(user_choice):
    """
    Predicado que devuelve True si el usuario ha decidido parar y False
    si quiere seguir jugando
    """
    return user_choice == GameChoice.QUIT


def generate_computer_choice():
    """
    Genera y devuelve una jugada al azar
    """
    from random import choice
    return choice([GameChoice.PAPER, GameChoice.ROCK, GameChoice.SCISSORS, GameChoice.LIZARD, GameChoice.SPOCK])


def evaluate_move(user_choice, comp_choice):
    """
    compara las dos jugadas y devuelve un texto con el resultado
    """
    assert user_choice != GameChoice.INVALID and user_choice != GameChoice.QUIT
    assert comp_choice != GameChoice.INVALID and comp_choice != GameChoice.QUIT

    result = ""

    if user_choice == GameChoice.PAPER:
        if comp_choice == GameChoice.PAPER:
            result = "Is's a tie!"
        elif comp_choice == GameChoice.ROCK:
            result = "You WIN! Paper covers rock"
        elif comp_choice == GameChoice.LIZARD:
            result = "I Win! Lizard eats paper"
        elif comp_choice == GameChoice.SPOCK:
            result = "You Win! Paper disproves Spock"
        else:
            # Scissors
            result = "I win! Scissors cut paper"
    elif user_choice == GameChoice.ROCK:
        if comp_choice == GameChoice.ROCK:
            result = "Is's a tie!"
        elif comp_choice == GameChoice.PAPER:
            result = "I WIN! Paper covers rock"
        elif comp_choice == GameChoice.LIZARD:
            result = "You WIN! Rock crushes lizard"
        elif comp_choice == GameChoice.SPOCK:
            result = "I WIN! Spock vaporizes rock"
        else:
            # Scissors
            result = "You win! Rock smashes scissors"
    elif user_choice == GameChoice.LIZARD:
        if comp_choice == GameChoice.ROCK:
            result = "I WIN! Rock crushes lizard"
        elif comp_choice == GameChoice.SCISSORS:
            result = "I WIN! Scissors decapitates lizard"
        elif comp_choice == GameChoice.LIZARD:
            result = "It's a tie!"
        elif comp_choice == GameChoice.PAPER:
            result = "Yoy WIN! Lizard eats paper"
        else:
            # Spock
            result = "You WIN! Lizard poisons Spock"
    elif user_choice == GameChoice.SPOCK:
        if comp_choice == GameChoice.SPOCK:
            result = "It's a tie!"
        elif comp_choice == GameChoice.PAPER:
            result = "I WIN! Paper disproves Spock"
        elif comp_choice == GameChoice.ROCK:
            result = "You WIN! Spock vaporizes rock"
        elif comp_choice == GameChoice.LIZARD:
            result = "I WIN! Lizard poisons Spock"
        else:
            #scissors
            result = "You WIN! Spock smashes scissors"
    else:
        # Scissors
        if comp_choice == GameChoice.ROCK:
            result = "I win! Rock smashes scissors"
        elif comp_choice == GameChoice.PAPER:
            result = "You WIN! Paper covers rock"
        elif comp_choice == GameChoice.LIZARD:
            result = "You WIN! Scissors decapitates lizard"
        elif comp_choice == GameChoice.SPOCK:
            result = "I WIN! Spock smashes scissors"
        else:
            #Scissors
            result = "Is's a tie!"
        pass

    return result


def print_result(result):
    """
    Imprime bonito el resultado
    """
    print("\n\n---------------------------")
    print("Game Over!")
    print(result)
    print("---------------------------\n\n")
    return None

def log_error(error):
    """
    Guarda los datos del error en crashlytics
    """
    print(error)

if __name__ == "__main__":

    try:
        game_loop()
    except Exception as error:
        log_error(error)

else:
    print("Si llegó hasta aquí, es que me están importando")
