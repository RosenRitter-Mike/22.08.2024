import random as rnd
import pprint
import sys

from art import *

def init_game() -> dict:
    '''
    Initializes the game data.
    :return:
    Returns a dictionary with the game settings (size of the board, the cards, the score, etc.) .
    '''

    deck: list[str] = ["A", "A", "B", "B", "C", "C", "D", "D", "E", "E", "F", "F", "G", "G", "H", "H"];
    rows, columns = 4, 4;

    game_data: dict = {
        'rows': rows,
        'columns': columns,
        'score': {'player 1': 0, 'player 2': 0},
        'turn': 'player 1',
        'game over': False,
        'board': prepare_board(rows, columns, deck),
        'move history': []
    }

    return game_data;


def prepare_board(rows, columns, cards) -> dict[any]:
    """
    Prepares the game board by shuffling cards and placing them into the board structure.

    Args:
        rows (int): Number of rows in the board.
        columns (int): Number of columns in the board.
        cards (list): List of card values to be placed on the board.

    Returns:
        dict: A dictionary representing the game board, where each key is a tuple (row, col)
              and the value is a dictionary with card information (card value, flipped state, matched state).
    """
    board = {}
    # shuffle the cards!
    rnd.shuffle(cards);
    # place the cards in the board- i.e.
    card_idx: int = 0;
    for column in range(columns):
        for row in range(rows):
            board[(row, column)] = {'card': cards[card_idx], 'flipped': False, 'matched': False};
            card_idx += 1;

    return board;

def display_board(game_data: dict) -> None:
    '''
    Displays the current state of the playing board;
    :param game_data:
    the current game data.
    :return:
    Displays the board.
    '''
    board: dict[any] = game_data['board'];
    rows = game_data['rows'];
    columns = game_data['columns'];

    for i in range(rows):
        print("", end=" | ")
        for j in range(columns):
            box = board[(i, j)]
            print(str(box['card']) if box['flipped'] else '_', end=" | ")
        print()
    print()
def get_valid_card(game_data: dict) -> list[any]:

    '''
    Gets a valid card guess from the user.
    :param game_data:
    the data of the ongoing game.
    :return:
    the index of the guess.
    '''

    idx_list: list[str] = [str(i) for i in range(16)];
    print("", idx_list[0:4], "\n", idx_list[4:8], "\n", idx_list[8:12], "\n", idx_list[12:16], "\n")
    guess: str = input("Make your guess: ");
    try:
        if guess.upper() == "R":
            return ['R', 99, 99];
        elif guess.upper() == "EXIT":
            return ['EXIT', 99, 99];
        elif int(guess) > 15 or int(guess) < 0:
            print(f"invalid choice for a card, choose again.");
            return get_valid_card(game_data);
        else:
            i_guess = int(guess);
            if i_guess > 11:
                j = 3;
            elif i_guess > 7:
                j = 2;
            elif i_guess > 3:
                j = 1;
            else:
                j = 0;
            i = i_guess - j * game_data['columns'];
            board: dict[any] = game_data['board'];
            if board[(j, i)]['flipped']:
                print(f"invalid choice for a card, card already flipped, choose again.");
                return get_valid_card(game_data);
            else:
                board[(j, i)]['flipped'] = True;
            return [board[(j, i)]['card'], j, i];
    except Exception as e:
        print("The error is: ", e);
        return get_valid_card(game_data);

def match(card1: list, card2: list, game_data: dict) -> bool:

    '''
    Check if the cards match and if they do then matched is changed.
    :param card1:
    First card data
    :param card2:
    Second card data
    :param game_data:
    game data needed to monitor the board
    :return:
    returns True if the cards are matched, and False if they are not.
    '''

    board: dict[any] = game_data['board'];
    if card1[0] == card2[0]:
        board[(card1[1], card1[2])]['matched'] = True;
        board[(card2[1], card2[2])]['matched'] = True;
        tprint("It's a match!", "chunky");
        print(art("cheers") * 4, "\n\n");
        return True;
    else:
        tprint("guess again!", "chunky");
        print(art("dunno2") * 8, "\n\n");
        return False;
def flip_back_cards(card1: list, card2: list, game_data: dict) -> None:

    '''
    Flip back open cards
    :param card1:
    First card data
    :param card2:
    Second card data
    :param game_data:
    game data needed to monitor the board
    :return:
    None
    '''

    board: dict[any] = game_data['board'];
    board[(card1[1], card1[2])]['flipped'] = False;
    board[(card2[1], card2[2])]['flipped'] = False;

def game_finished(game_data: dict) -> bool:

    '''
    Checks if the game is finished, and print a victory massage and winner if it is.
    :param game_data:
    current game data
    :return:
    True if the game is finished false if it is not;
    '''
    finished: bool = True;
    board: dict[any] = game_data['board'];
    rows = game_data['rows'];
    columns = game_data['columns'];
    for i in range(rows):
        for j in range(columns):
            box = board[(i, j)]
            if not box['matched']:
                finished = False;
            # print(box['matched']);

    if finished:
        game_data['game over'] = True;
        winner: str = 'player 1' if game_data['score']['player 1'] > game_data['score']['player 2'] \
            else 'player 2' if game_data['score']['player 1'] < game_data['score']['player 2']\
            else 'Its a draw!';
        tprint(f"{winner}", "epic")
        tprint("You\nhave\nwon\nthe\ngame!!\n\nCongratulations!!", "epic");
        print(art("dance" * 2));
        print()

        play_again: str = input("Want to play another game? (Y/N)   ");
        if play_again.upper() == "Y":
            tprint("game   restarted", "chunky");
            game_data = init_game();
            play(game_data);

        else:
            return True;
def play(game_data) -> None:
    """
    Runs the main game loop, handling player turns, guessing, and score updates.

    Args:
        game_data (dict): The game data dictionary containing the board, scores, and other game information.
    """
    while True:
        for player in [1, 2]:
            game_finished(game_data);
            if game_data['game over']:
                break;

            if player == 1:
                game_data['turn'] = 'player 1';

            else:
                game_data['turn'] = 'player 2';

            print(f"its {game_data['turn']}'s turn");
            print("you can write exit at any guess to exit the game");
            display_board(game_data);
            guess1 = get_valid_card(game_data);
            if guess1[0] == 'R':
                tprint("game   restarted", "chunky");
                game_data = init_game();
                play(game_data);
                return None;
            elif guess1[0] == 'EXIT':
                sys.exit();
            else:
                display_board(game_data);
            print();

            guess2 = get_valid_card(game_data);
            if guess2[0] == 'R':
                tprint("game   restarted", "chunky");
                game_data = init_game();
                play(game_data);
                return None;
            elif guess2[0].upper() == 'EXIT':
                sys.exit();
            else:
                display_board(game_data);
            print();

            if match(guess1, guess2, game_data):
                game_data['score'][game_data['turn']] += 1;
                # play(game_data);
                continue;

            else:
                flip_back_cards(guess1, guess2, game_data);



            if game_data['game over']:
                break;


        if game_data['game over']:
            break;
        """
        demo code -- just for example of how to call functions 

        for player in [1, 2]:
            diaply_board(game_data)
            guess1 = get_valid_card(...)
            diaply_board(game_data)
            guess2 = get_valid_card(...)
            diaply_board(game_data)
            if match(guess1, guess2):
                score += 1
                play again
            else:
                flip_back_cards(..)
        """




##################################______Tests_Funcs_____########################################
def test_prepare_board():
    ''' Prints the board so it can be seen no errors were made.'''
    game: dict = init_game();
    print();
    pprint.pprint(game['board']);

def test_display_board():
    game: dict = init_game();
    print();
    display_board(game);

##################################______Tests_____#############################################
# test_prepare_board()
test_display_board();
