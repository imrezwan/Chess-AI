import board, pieces, numpy

class Heuristics:
    WIDTH = 4
    HEIGHT = 8


    PAWN_TABLE = numpy.array([
        [ 0, -10,  -5,  0,  0,  0,  50,  0],
        [ 0, -10, -20, 25, 35,  40,  50,  0],
        [ 0, -20, -20, 25,  40, 40, 50,  0],
        [ 0, -10, -5, 20, 20,  0,  50,  0]
    ])

    ROOK_TABLE = numpy.array([
        [-20, -10, -10, -5, -5, -10, -10, -20],
        [-10,   0,   5,  10,  10,   0,   0, -10],
        [-10,   5,   5,  5,  5,   5,   0, -10],
        [-20, -10, -10, -5, -5, -10, -10, -20]
    ])

    QUEEN_TABLE = numpy.array([
        [-20, -10, -10, 5, 5, -10, -10, -20],
        [-10,   0,   15,  10,  10,   0,   0, -10],
        [-10,   5,   15,  25,  15,   5,   0, -10],
        [-20, -10,  10, 5, 5,  10, -10, -20]
    ])

    @staticmethod
    def evaluate(board):
        material = Heuristics.get_material_score(board)

        pawns = Heuristics.get_piece_position_score(board, pieces.Pawn.PIECE_TYPE, Heuristics.PAWN_TABLE)
        rooks = Heuristics.get_piece_position_score(board, pieces.Rook.PIECE_TYPE, Heuristics.ROOK_TABLE)
        queens = Heuristics.get_piece_position_score(board, pieces.Queen.PIECE_TYPE, Heuristics.QUEEN_TABLE)

        return material + pawns + rooks + queens

    @staticmethod
    def get_piece_position_score(board, piece_type, table):
        white = 0
        black = 0
        for x in range(4):
            for y in range(8):
                piece = board.chesspieces[x][y]
                if (piece != 0):
                    if (piece.piece_type == piece_type):
                        if (piece.color == pieces.Piece.WHITE):
                            white += table[x][y]
                        else:
                            black += table[3 - x][y]

        return white - black

    @staticmethod
    def get_material_score(board):
        white = 0
        black = 0
        for x in range(4):
            for y in range(8):
                piece = board.chesspieces[x][y]
                if (piece != 0):
                    if (piece.color == pieces.Piece.WHITE):
                        white += piece.value
                    else:
                        black += piece.value

        return white - black


class AI:

    INFINITE = 10000000

    @staticmethod
    def get_ai_move(chessboard, invalid_moves):
        best_move = 0
        best_score = AI.INFINITE
        for move in chessboard.get_possible_moves(pieces.Piece.BLACK):
            if (AI.is_invalid_move(move, invalid_moves)):
                continue

            copy = board.Board.clone(chessboard)
            #print("GET AI MOVE::::==>>> "+ move.to_string())
            copy.perform_move(move)

            score = AI.alphabeta(copy, 2, -AI.INFINITE, AI.INFINITE, True)
            if (score < best_score):
                best_score = score
                best_move = move

        # Checkmate.
        if (best_move == 0):
            return 0

        copy = board.Board.clone(chessboard)
        copy.perform_move(best_move)
        if (copy.is_check(pieces.Piece.BLACK)):
            invalid_moves.append(best_move)
            return AI.get_ai_move(chessboard, invalid_moves)

        return best_move

    @staticmethod
    def is_invalid_move(move, invalid_moves):
        for invalid_move in invalid_moves:
            if (invalid_move.equals(move)):
                return True
        return False

    @staticmethod
    def minimax(board, depth, maximizing):
        if (depth == 0):
            return Heuristics.evaluate(board)

        if (maximizing):
            best_score = -AI.INFINITE
            for move in board.get_possible_moves(pieces.Piece.WHITE):
                copy = board.Board.clone(board)
                copy.perform_move(move)

                score = AI.minimax(copy, depth-1, False)
                best_score = max(best_score, score)

            return best_score
        else:
            best_score = AI.INFINITE
            for move in board.get_possible_moves(pieces.Piece.BLACK):
                copy = board.Board.clone(board)
                copy.perform_move(move)

                score = AI.minimax(copy, depth-1, True)
                best_score = min(best_score, score)

            return best_score

    @staticmethod
    def alphabeta(chessboard, depth, a, b, maximizing):
        if (depth == 0):
            return Heuristics.evaluate(chessboard)

        if (maximizing):
            best_score = -AI.INFINITE
            for move in chessboard.get_possible_moves(pieces.Piece.WHITE):
                copy = board.Board.clone(chessboard)
                copy.perform_move(move)

                best_score = max(best_score, AI.alphabeta(copy, depth-1, a, b, False))
                a = max(a, best_score)
                if (b <= a):
                    break
            return best_score
        else:
            best_score = AI.INFINITE
            for move in chessboard.get_possible_moves(pieces.Piece.BLACK):
                copy = board.Board.clone(chessboard)
                copy.perform_move(move)

                best_score = min(best_score, AI.alphabeta(copy, depth-1, a, b, True))
                b = min(b, best_score)
                if (b <= a):
                    break
            return best_score


class Move:

    def __init__(self, xfrom, yfrom, xto, yto):
        self.xfrom = xfrom
        self.yfrom = yfrom
        self.xto = xto
        self.yto = yto

    # Returns true iff (xfrom,yfrom) and (xto,yto) are the same.
    def equals(self, other_move):
        try:
            return self.xfrom == other_move.xfrom and self.yfrom == other_move.yfrom and self.xto == other_move.xto and self.yto == other_move.yto
        except:
            print("==========>>>>>>>>>>>> Error:::: "+other_move)

    def to_string(self):
        return "(" + str(self.xfrom) + ", " + str(self.yfrom) + ") -> (" + str(self.xto) + ", " + str(self.yto) + ")"
