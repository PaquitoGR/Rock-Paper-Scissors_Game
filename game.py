from enum import Enum

# User choices
class GameChoice(Enum):
    INVALID = -1
    PAPER = 0
    ROCK = 1
    SCISSORS = 2
    QUIT = 3


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
            # muestro el ganador en poantalla y vuelta al principio
            print_result(result)
        else:
            # el humano es un gallina: salgo
            break


def read_user_choice():
    """
    Lee una selección del usuario (piedra, papel, tijera o salir) y
    la devuelve
    """
    user_choice = GameChoice.INVALID
    while user_choice == GameChoice.INVALID:
        print("Select one number:")
        print(f'{GameChoice.PAPER.value}. Paper')
        print(f'{GameChoice.ROCK.value}. Rock')
        print(f'{GameChoice.SCISSORS.value}. Scissors')
        print("-" * 20)
        print(f'{GameChoice.QUIT.value}. Quit the game')

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
    return choice([GameChoice.PAPER, GameChoice.ROCK, GameChoice.SCISSORS])


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
        else:
            result = "I win! Scissors cut paper"

    elif user_choice == GameChoice.ROCK:
        if comp_choice == GameChoice.ROCK:
            result = "Is's a tie!"
        elif comp_choice == GameChoice.PAPER:
            result = "I WIN! Paper covers rock"
        else:
            result = "You win! Rock smashes Scissors"
    else:
        # Scissors
        if comp_choice == GameChoice.ROCK:
            result = "I win! Rock smashes Scissors"
        elif comp_choice == GameChoice.PAPER:
            result = "You WIN! Paper covers rock"
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
    print("-------------------------\n\n")
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

    