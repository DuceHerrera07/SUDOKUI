board = [
    ["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]
]
#ire a dormir
class ValidarSudoku:
    def __init__(self,tablero)->None:
        self.tablero=tablero
        self.lista_invertida= list()
        
    def Chequeo (self):
        
        assert len(self.tablero) == 9 
        for fila in self.tablero:
            assert len(fila) == 9
#instanciar el objeto
sudoku = ValidarSudoku(board)
sudoku.Chequeo()
#mañana trabajemos xd
