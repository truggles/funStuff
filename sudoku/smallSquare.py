



    

class Square :
    """ A clase for a single square in the sudoku board """

    def __init__( self, gridSize, x, y, inputValue ):

        # coordinates
        self.x = x
        self.y = y
        self.gridSize = gridSize

        # map from 1 to gridSize**2, default to true, set to false by checking
        # the row/column/lrg square associated with this square
        self.potentialValues = {}

        if inputValue != 0 :
            self.finalValueSet = True # set to true when finalized
            self.finalValue = inputValue

        else : # inputValue == 0, so make list of possibilities
            for i in range( 1, gridSize*gridSize + 1 ) :
                self.potentialValues[ i ] = True
            
            self.finalValueSet = False # set to true when finalized
            self.finalValue = 0

    def printCoordinates( self ) :
        print "square: (%i,%i)" % (self.x, self.y)
    

    # convert finalized value list into available map
    def usedValuesToPotValsMap( self, useValuesList ) :
        potValues = {}
        for i in range( 1, self.gridSize*self.gridSize + 1 ) :
            potValues[ i ] = True if i not in useValuesList else False
        return potValues
        

    # function to potential values from a passed dictionary from SudokuGame 
    def updatePotentialValue( self, useValuesList ) :
        if self.finalValueSet : return False
        print "\n",self.x,self.y,self.potentialValues
        print useValuesList
        potValMap = self.usedValuesToPotValsMap( useValuesList )
        print potValMap
        updated = False
        for k, v in potValMap.iteritems() :
            # only update if valuer here is != to potentialValue
            # and the new value is False, eliminating an option
            if v != self.potentialValues[ k ] and v == False :
                self.potentialValues[ k ] = False
                updated = True
        print self.potentialValues

        self.checkIfSolved()

        # to track if changes are being made
        return updated

    def checkIfSolved( self ) :
        # Check if solved
        nTrue = 0
        valTrue = 0
        for k, v in self.potentialValues.iteritems() :
            if v == True :
                nTrue += 1
                valTrue = k
        if nTrue == 1 :
            self.finalValue = valTrue
            self.finalValueSet = True
            print "Set final value for square (%i,%i) = %i" % (self.x, self.y, valTrue)

        

