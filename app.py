from game import Game

if __name__ == '__main__':
    game = Game()
    play_again = True

    while play_again:
        game.reset_game()
        play_again = game.start()

    print("I hope you enjoyed marking my assignment")

