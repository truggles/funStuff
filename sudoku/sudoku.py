from smallSquare import Square



class SudokuGame :
    """ A class for the sudoku board and it's operations """
    

    def __init__( self, gridSize, inputString ):
        self.gridSize = gridSize

        # Check input string size
        checkSize = inputString.strip().split(',')
        assert( (self.gridSize*self.gridSize)**2 == len( checkSize ) ), "Input string \
            is the wrong length: %i  for grid size: %i" % (len( checkSize),
            self.gridSize)

        # a string of 81 integers
        self.board = self.createBoard( inputString)
        

        print "\nStarting board configuration:"
        self.printBoard()

        self.playGame()



    def createBoard( self, inputString ):
        # create board from input integers
        print "inputString",inputString
        #reverseInput = inputString[::-1]
        #inputValues = reverseInput.strip().split(',')
        inputValues = inputString.strip().split(',')
        board = [[ 0 for x in range( self.gridSize*self.gridSize ) ] for y in range ( self.gridSize*self.gridSize ) ]
        for x in range(  self.gridSize*self.gridSize ) :
            for y in range( self.gridSize*self.gridSize ) :
                #val = int( inputValues.pop() )
                val = int( inputValues[ x + y * self.gridSize*self.gridSize ] )
                print "new square:",x,y," init val:",int(val)
                board[y][x] = Square( self.gridSize, x, y, val )
        return board


    # nice print function
    def printBoard( self ) :
        horiz = ['-' for i in range( self.gridSize * 9 )]
        horizBorder = ' '+''.join( horiz )
        print horizBorder
        for y, row in enumerate( self.board ) :
            printRow = ''
            for x, sq in enumerate( row ) :
                if (x) % self.gridSize == 0 : printRow += ' | '
                printRow += ' %i ' % int( sq.finalValue )
            print printRow,'|'
            if (y+1) % self.gridSize == 0 : print horizBorder



    # return square class
    def getSquare( self, x, y ) :
        assert (x < self.gridSize*self.gridSize and y < self.gridSize*self.gridSize ), "Querying for a square outside the range of the board"
        return self.board[y][x]

    # get values for a square
    def getSquareVal( self, x, y ) :
        sq = self.getSquare( x, y )
        return sq.finalValue


    # Get final values associated with a row
    def getValuesRow( self, nRow ) :
        values = []
        for iCol in range( self.gridSize*self.gridSize ) :
            values.append( self.getSquareVal( iCol, nRow ) )
        return values
        
    # Get final values associated with a column
    def getValuesCol( self, nCol ) :
        values = []
        for iRow in range( self.gridSize*self.gridSize ) :
            values.append( self.getSquareVal( nCol, iRow ) )
        return values
        

    # Get final values associated with a sub-square
    def getValuesBigSq( self, x, y ) :
        values = []
        if self.gridSize == 2 : # simpler 4x4 super square and 2x2 sub-square
            for iRow in range( self.gridSize*self.gridSize ) :
                if self.inSubRange2x2( y, iRow ) :
                    for iCol in range( self.gridSize*self.gridSize ) :
                        if self.inSubRange2x2( x, iCol ) :
                            values.append( self.getSquareVal( iCol, iRow ) )
        elif self.gridSize == 3 : # 9x9 super square and 3x3 sub-square
            for iRow in range( self.gridSize*self.gridSize ) :
                if self.inSubRange3x3( y, iRow ) :
                    for iCol in range( self.gridSize*self.gridSize ) :
                        if self.inSubRange3x3( x, iCol ) :
                            values.append( self.getSquareVal( iCol, iRow ) )
        return values
        
    # check if values is in subrange
    def inSubRange2x2( self, x, iCol ) : # same for y, iRow
        if x < self.gridSize and iCol < self.gridSize : return True
        if x >= self.gridSize and iCol >= self.gridSize : return True
        else : return False
    def inSubRange3x3( self, x, iCol ) : # same for y, iRow
        # lower range
        if x < self.gridSize and iCol < self.gridSize : return True
        # upper range
        if x >= self.gridSize*2 and iCol >= self.gridSize*2 : return True
        # middle
        if (x >= self.gridSize and x < self.gridSize*2) and (iCol >= self.gridSize and iCol < self.gridSize*2) : return True
        else : return False
        


    # loop over square and solve game
    def playGame( self ) :
        play = True
        cnt = 0
        lastUpdate = 0 # track how long ago we made progress to kill if too long
        while play :
            for y in range( self.gridSize*self.gridSize ) :
                rowValues = self.getValuesRow( y )
                for x in range( self.gridSize*self.gridSize ) :
                    colValues = self.getValuesCol( x )
                    bigSqValues = self.getValuesBigSq( x, y )
                    sq = self.getSquare( x, y )
                    wasUpdatedRow = sq.updatePotentialValue( rowValues )
                    wasUpdatedCol = sq.updatePotentialValue( colValues )
                    wasUpdatedSq = sq.updatePotentialValue( bigSqValues )
                    wasUpdated = True if (wasUpdatedRow or wasUpdatedCol or wasUpdatedSq) else False
                    if wasUpdated :
                        lastUpdate = 0
                        self.printBoard()
                    else : lastUpdate += 1
                    cnt += 1
            #if cnt > 50 : break
            if lastUpdate > (self.gridSize*self.gridSize)**2+5 : break

        print "\n\nFinished!\n"
        self.printBoard()
        print "\n"




