class WrongNumberOfPlayersError(Exception):
    pass


class NoSuchStrategyError(Exception):
    pass

def rps_game_winner(game):
    if len(game) != 2:
        raise WrongNumberOfPlayersError("WrongNumberOfPlayersError")
    valid_strat = ['R', 'P', 'S']
    p1, p2 = game
    if p1[1] not in valid_strat or p2[1] not in valid_strat:
        raise NoSuchStrategyError("NoSuchStrategyError")

    def win(p1, p2):
        return (p1 == 'R' and p2 == 'S') or \
            (p1 == 'S' and p2 == 'P') or \
            (p1 == 'P' and p2 == 'R')
    if win(p1[1], p2[1]) or p1[1] == p2[1]:
        return p1
    else: return p2


game = [['player1', 'S'], ['player2', 'R']]
print(rps_game_winner(game))
