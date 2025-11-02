# src/prisoners_dilemma.py

def resolve_round(player1_move, player2_move, payoff_matrix):
    player1_outcome = payoff_matrix[player1_move][player2_move][0]
    player2_outcome = payoff_matrix[player1_move][player2_move][1]
    return player1_outcome, player2_outcome

def conduct_tournament(roster, num_rounds, payoff_matrix):
    for i in range(num_rounds):
        for j, player1_name in enumerate(roster):
            for k, player2_name in enumerate(roster):
                if j <= k:
                    player1 = roster[player1_name]
                    player2 = roster[player2_name]
                    player1_move = player1.choose_move(player2)
                    player2_move = player2.choose_move(player1)
                    player1_result, player2_result = resolve_round(player1_move, player2_move, payoff_matrix)

                    # record in both histories
                    player1.record_interaction(
                        opponent_name=player2_name,
                        my_move=player1_move,
                        their_move=player2_move,
                        my_outcome=player1_result,
                        their_outcome=player2_result,
                    )
                    player2.record_interaction(
                        opponent_name=player1_name,
                        my_move=player2_move,
                        their_move=player1_move,
                        my_outcome=player2_result,
                        their_outcome=player1_result,
                    )