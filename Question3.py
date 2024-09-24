def winner(points):
    player1_score = 0
    player2_score = 0

    for point in points:
        if point == 1:
            player1_score += 1
        else:
            player2_score += 1

        if player1_score >= 11 and player1_score - player2_score >= 2:
            return "Player 1 won the match."
        if player2_score >= 11 and player2_score - player1_score >= 2:
            return "Player 2 won the match."

    return "The match is still ongoing."

points = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1]
print(winner(points))
