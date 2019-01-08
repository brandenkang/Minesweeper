import random, os

class Tile:
    def __init__(self,r,c,v):
        self.r=r
        self.c=c
        self.v=v
        self.w=52
        self.h=52
        self.s="H" #status: hidden or unhidden
        self.img=loadImage("images/0.png")
        self.imgHidden=loadImage("images/tile.png") 
        
    def display(self):
        if self.s=='H':
            image(self.imgHidden,self.c*self.w,self.r*self.h)
        else:
            image(self.img,self.c*self.w,self.r*self.h)

class Minesweeper:
    def __init__(self,numRows,numCols,numMines):
        self.numRows=numRows
        self.numCols=numCols
        self.numMines=numMines
        self.leftTiles=numRows*numCols-numMines
        self.board=[]

    
    def createBoard(self):
        for r in range(self.numRows):
            for c in range(self.numCols):
                self.board.append(Tile(r,c,'.'))
        random.shuffle(self.board)
        self.assignMines()
        self.assignNumbers()

        self.gameover = False
        self.gameoverImg = loadImage("images/gameover.png")
        self.win = False 
        self.winImg = loadImage("images/win.png")
        #self.play()

    def getTile(self,r,c):
        for t in self.board:
            if t.r == r and t.c == c:
                return t
    
    def display(self):
        for t in self.board:
            t.display()
        if self.gameover == True:
            image(self.gameoverImg, 20, 20)

        if self.win == True:
            image(self.winImg, 20, 20)


          



    def assignMines(self):
        for m in range(self.numMines):
            self.board[m].v="*"
            self.board[m].img=loadImage("images/mine.png")

    def assignNumbers(self):
        for each in self.board:
            if each.v!='*':
                count=0
                for r in [-1,0,1]:
                    for c in [-1,0,1]:
                        if each.r+r in range(self.numRows) and each.c+c in range(self.numCols) and self.getTile(each.r+r,each.c+c).v=='*':
                            count+=1
                if count == 0:
                    each.v = " "
                else:
                    each.v=count
                    each.img=loadImage("images/"+str(each.v)+".png")

    def uncover(self,t):
        if t.v in range(1,9):
            t.s = 'UH'
            self.leftTiles-=1

        else: # empty space
            t.s = 'UH'
            self.leftTiles-=1

            for r in [-1,0,1]:
                for c in [-1,0,1]:
                    nTile = self.getTile(t.r+r,t.c+c)
                    if nTile != None and nTile.s == "H":
                        self.uncover(nTile)
        
        if self.leftTiles == 0: 
            self.win = True
            print("Win")
            return False
        
        elif t.v == '*':
            self.gameover = True
            print ("Game Over")
            return True


m = Minesweeper(10,10,10)

def setup():
    size(m.numCols*52, m.numRows*52)
    m.createBoard()
    # reset()
    
def draw():
    m.display()

def mouseClicked():
    global m 
    if m.uncover(m.getTile(mouseY//52, mouseX//52)):
        for t in m.board:
            t.s="UH"
        return

    if m.gameover == True or m.win == True:
        m = Minesweeper(10,10,10)
        m.createBoard()
   