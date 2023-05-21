def rps(p1, p2):
    """Let's play! You have to return which player won! In case of a draw return"""
    if p1 == p2:
        return "Draw!"
    elif p1 == "rock":
        if p2 == "scissors":
            return "Player 1 won!"
        else:
            return "Player 2 won!"
    elif p1 == "paper":
        if p2 == "rock":
            return "Player 1 won!"
        else:
            return "Player 2 won!"
    elif p1 == "scissors":
        if p2 == "paper":
            return "Player 1 won!"
        else:
            return "Player 2 won!"


assert (rps("rock", "scissors")) == "Player 1 won!"
assert (rps("scissors", "rock")) == "Player 2 won!"
