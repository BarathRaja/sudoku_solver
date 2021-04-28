class solver:
    def __init__(self, board):
        self.board = board

    def solve(self):
        find_zero = self.find_empty()
        if find_zero is None:
            return True
        else:
            row, col = find_zero

        for i in range(1, 10):
            if self.isvalid(i, (row, col)):
                self.board[row][col] = i
                if self.solve():
                    return True
                self.board[row][col] = 0
        return False

    def isvalid(self, num, pos):
        #check col
        for i in range(9):
            if self.board[pos[0]][i] == num and pos[1]!=i:
                return False
        #check row
        for i in range(9):
            if self.board[i][pos[1]] == num and pos[0]!=i:
                return False
        #check cube
        box_x = pos[1] // 3
        box_y = pos[0] // 3
        for i in range(box_y * 3, box_y * 3 + 1):
            for j in range(box_x * 3, box_x * 3 + 1):
                if self.board[i][j] == num:
                    return False
        return True

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)
        return None


    def print_board(self):
        for i in range(len(self.board)):
            if i%3==0 and i!=0:
                print("-"*21)
            for j in range(len(self.board[i])):
                if j%3==0 and j!=0:
                    print("|", end=" ")
                if j==8:
                    print(self.board[i][j])
                else:    
                    print(self.board[i][j], end=" ")
