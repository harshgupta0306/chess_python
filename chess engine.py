import pygame,copy
pygame.init()

Height = 600
Width = 600
Margin = 0
boxsize=75
window = pygame.display.set_mode((Height,Width))
pygame.display.set_caption("chess")
clock = pygame.time.Clock()
#colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)
brown = (150,75,0)

flip = "white"

chess_board = pygame.image.load("chess bo.jpg") 

chessbuttonB = pygame.image.load("chess_peices/chessbuttonB.png")
chessbuttonW = pygame.image.load("chess_peices/chessbuttonW.png")
#turn dittermination
turn="white"

enpassent_loc = []


move_made = False

check_to_white = False
check_to_black = False

can_move_list =[]

peices_images = {}

#parent class of all the pieces 
class pieces:
    # board matrix
    board = [['br1', 'bkn1', 'bb1', 'bq1', 'bk1', 'bb2', 'bkn2', 'br2'],
             ['bp1', 'bp2', 'bp3', 'bp4', 'bp5', 'bp6', 'bp7', 'bp8'],
             ['__', '__', '__', '__', '__', '__', '__', '__'],
             ['__', '__', '__', '__', '__', '__', '__', '__'],
             ['__', '__', '__', '__', '__', '__', '__', '__'],
             ['__', '__', '__', '__', '__', '__', '__', '__'],
             ['wp1', 'wp2', 'wp3', 'wp4', 'wp5', 'wp6', 'wp7', 'wp8'],
             ['wr1', 'wkn1', 'wb1', 'wq1', 'wk1', 'wb2', 'wkn2', 'wr2']]

    def __init__(self,type,name,col,row):
        self.type = type
        self.name = name
        # self.row = row
        # self.col = col
        self.x = row
        self.y = col

#pawn class that contains all the specific information about pawn 
class pawn(pieces):


    # def __init__(self):
    #     self.pinned = False
    #     self.can_move = True
    enpassentW = [False,[]]
    enpassentB = [False,[]]
    # enpasant_pawn_loc = []

    def can_move_to(self,board):
        
        
        for i in range(8):
            for j in range(8):
                
                loc = board[i][j]
                
                #balck pawn movement 
                if self.type == "b" :
                    if self.y == 1:
                        not_moved = True
                    else:
                        not_moved = False    
                    if loc[0:1] != "b":
                        if i == self.y + 1 and (j == self.x - 1 or j == self.x + 1) :
                            
                            if loc[0:1] == "w":
                                can_move_list.append([i,j])
                                
                            #if white moved his pawn two squares in pevious turn 
                            
                            if pawn.enpassentW[0]:
                                # print(i,j,pawn.enpassentW[1],"white")
                                # if black's pawn is beside that pawn can capture that pawn
                                if [i,j] == pawn.enpassentW[1]:
                                    can_move_list.append([i,j])

                        if i == self.y + 1 and j == self.x:
                            if loc == "__":
                                can_move_list.append([i,j])
                        elif not_moved :
                            
                            if i == self.y + 2  and j == self.x :
                                if board[self.y+1][self.x]== '__':
                                    if loc == "__":
                                        #location of blacks pawn when it moves two squares
                                        # pawn.enpasant_pawn_loc = (i,j)
                                        can_move_list.append([i,j])         
                #white pawn movement 
                else :

                    if self.y == 6:
                        not_moved = True
                    else:
                        not_moved = False

                    if loc[0:1] != "w":
                        if i == self.y - 1 and (j == self.x - 1 or j == self.x+1) :
                            if loc[0:1] == "b":
                                can_move_list.append([i,j])
                            
                            #if black moved two squares can capture that peice    
                            
                              
                            if pawn.enpassentB[0]:
                                # print(i,j,pawn.enpassentB[1],"black")
                                #if white's pawn is beside that pawn can capture that pawn 
                                if [i,j] == pawn.enpassentB[1]:
                                    can_move_list.append([i,j])
                        if i == self.y - 1  and j == self.x : 
                            if loc== "__":
                                can_move_list.append([i,j])     
                        elif not_moved:
                            if i == self.y - 2  and j == self.x : 
                                if board[self.y-1][self.x]== '__':
                                    if loc=="__":   
                                        #location of white pawn when it  move two squares
                                        # pawn.enpasant_pawn_loc = (i,j)
                                        # print( pawn.enpasant_pawn_loc)
                                        can_move_list.append([i,j])     

#Knight class that contains all the specific information about knight 
class knight(pieces):

    def can_move_to(self,board):
        
        for i in range(8):
            for j in range(8):
                
                loc = board[i][j]
                
                if self.type == "b" :
                    if loc[0:1] != "b":
                        if i == self.y + 2  and (j == self.x - 1 or j == self.x + 1):
                            can_move_list.append([i,j])
                        elif i == self.y - 2  and (j == self.x - 1 or j == self.x + 1):
                            can_move_list.append([i,j])
                        elif j == self.x + 2  and (i == self.y - 1 or i == self.y + 1):
                            can_move_list.append([i,j])
                        elif j == self.x - 2  and (i == self.y - 1 or i == self.y + 1):
                            can_move_list.append([i,j])   
                else :
                    if loc[0:1] != "w":
                        if i == self.y + 2  and (j == self.x - 1 or j == self.x + 1):
                            can_move_list.append([i,j])
                        elif i == self.y - 2  and (j == self.x - 1 or j == self.x + 1):
                            can_move_list.append([i,j])
                        elif j == self.x + 2  and (i == self.y - 1 or i == self.y + 1):
                            can_move_list.append([i,j])
                        elif j == self.x - 2  and (i == self.y - 1 or i == self.y + 1):
                            can_move_list.append([i,j])    

#rook  class that contains all the specific information about rook 
class rook(pieces):

    black_r1=True
    black_r2=True
    white_r1=True
    white_r2=True
    def can_move_to(self,board):

        direction = {"up":(-1,0),"down":(1,0),"left":(0,-1),"right":(0,1)}
        for i in range(self.y+1,8):
            
            if board[i][self.x][0:1] == "w":
                if self.type == "w" :
                    break
                else:
                    can_move_list.append([i,self.x]) 
                    break 
            elif board[i][self.x][0:1] == "b":
                if self.type == "w" :
                    can_move_list.append([i,self.x])  
                    break
                else :
                    break 
            else:
                can_move_list.append([i,self.x])
        
        for i in range(self.y-1,-1,-1):
            
            if board[i][self.x][0:1] == "w":
                if self.type == "w" :
                    break
                else:
                    can_move_list.append([i,self.x])
                    break
            elif board[i][self.x][0:1] == "b": 
                if self.type == "w":
                    can_move_list.append([i,self.x])  
                    break
                else:
                    break
            else :
                can_move_list.append([i,self.x])
        for i in range(self.x+1,8):
            
            if board[self.y][i][0:1] == "w":
                if self.type == "w" :
                    break
                else:
                    can_move_list.append([self.y,i])  
                    break 

            elif board[self.y][i][0:1] == "b":
                if self.type == "w":
                    can_move_list.append([self.y,i])  
                    break
                else:
                    break 

            else:
                can_move_list.append([self.y,i])
        for i in range(self.x-1,-1,-1):
            
            if board[self.y][i][0:1] == "w":
                if self.type == "w" :
                    break
                else:
                    can_move_list.append([self.y,i])  
                    break
            elif board[self.y][i][0:1] == "b":
                if self.type == "w":
                    can_move_list.append([self.y,i])  
                    break
                else:
                    break 
            else :
                can_move_list.append([self.y,i])     

#bishop class that contains all the specifics information about bishop
class bishop(pieces):
    

    def can_move_to(self,board):
        right = True
        left = True
        direction =[(-1,1,"downleft"),(-1,-1,"upleft"),(1,-1,"upright"),(1,1,"downright")]
        fake_x1,fake_y1 = self.x,self.y
        fake_x2,fake_y2 = self.x,self.y
        #up
        for i in range(self.y-1,-1,-1):
            fake_x1+=direction[2][0]
            fake_y1=i
            # print(fake_y1,fake_x1,"upRIght")
            #right
            if fake_x1<8 and right and fake_y2>=0:
                
                if board[fake_y1][fake_x1][0:1] == "b":
                    if self.type =="b":

                        right = False
                    else:
                        can_move_list.append([fake_y1,fake_x1])
                        right = False
                elif board[fake_y1][fake_x1][0:1] == "w":
                    if self.type =="w":

                        right = False
                    else:
                        can_move_list.append([fake_y1,fake_x1])
                        right = False

                else:
                    can_move_list.append([fake_y1,fake_x1])
            #left
            fake_x2+=direction[1][0]
            fake_y2=i
            # print(fake_y2,fake_x2,"upleft")
            if fake_x2>=0 and left and fake_y2>=0:
                
                if board[fake_y2][fake_x2][0:1] == "b":
                    if self.type == "b":    
                        left = False
                    else :
                        can_move_list.append([fake_y2,fake_x2])
                        left = False
                elif board[fake_y2][fake_x2][0:1] == "w":
                    if self.type == "w":    
                        left = False
                    else :
                        can_move_list.append([fake_y2,fake_x2])
                        left = False
                else:
                    can_move_list.append([fake_y2,fake_x2])

        #down
        right = True
        left = True
        fake_x1,fake_y1 = self.x,self.y
        fake_x2,fake_y2 = self.x,self.y
        for i in range(self.y+1,8):
            fake_x1+=direction[3][0]
            fake_y1=i 
            #right
            if fake_x1<8 and right and fake_y1<8:
               

                if board[fake_y1][fake_x1][0:1] == "b":
                    if self.type == 'b':
                        right = False
                    else :
                        can_move_list.append([fake_y1,fake_x1])
                        right = False
                elif board[fake_y1][fake_x1][0:1] == "w":
                    if self.type == 'w':
                        right = False
                    else :
                        can_move_list.append([fake_y1,fake_x1])
                        right = False   
                else:
                
                    can_move_list.append([fake_y1,fake_x1])
            #left
            fake_x2+=direction[0][0]
            fake_y2= i
            if fake_x2>=0 and left and fake_y2<8 :
                

                if board[fake_y2][fake_x2][0:1] == "b":
                    if self.type == "b":
                        left = False
                    else:
                        can_move_list.append([fake_y2,fake_x2])
                        left = False
                elif board[fake_y2][fake_x2][0:1] == "w":
                    if self.type == "w":
                        left = False
                    else:
                        can_move_list.append([fake_y2,fake_x2])
                        left = False

                else:
                    can_move_list.append([fake_y2,fake_x2])

#Queen class that contains all the specifics information about Queen
class queen(pieces):
    def can_move_to(self,board):
        # rook movement +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=+++++++++++++++++++++++++++
        direction = {"up":(-1,0),"down":(1,0),"left":(0,-1),"right":(0,1)}
        for i in range(self.y+1,8):
            
            if board[i][self.x][0:1] == "w":
                if self.type == "w" :
                    break
                else:
                    can_move_list.append([i,self.x]) 
                    break 
            elif board[i][self.x][0:1] == "b":
                if self.type == "w" :
                    can_move_list.append([i,self.x])  
                    break
                else :
                    break 
            else:
                can_move_list.append([i,self.x])
        
        for i in range(self.y-1,-1,-1):
            
            if board[i][self.x][0:1] == "w":
                if self.type == "w" :
                    break
                else:
                    can_move_list.append([i,self.x])
                    break
            elif board[i][self.x][0:1] == "b": 
                if self.type == "w":
                    can_move_list.append([i,self.x])  
                    break
                else:
                    break
            else :
                can_move_list.append([i,self.x])
        for i in range(self.x+1,8):
            
            if board[self.y][i][0:1] == "w":
                if self.type == "w" :
                    break
                else:
                    can_move_list.append([self.y,i])  
                    break 

            elif board[self.y][i][0:1] == "b":
                if self.type == "w":
                    can_move_list.append([self.y,i])  
                    break
                else:
                    break 

            else:
                can_move_list.append([self.y,i])
        for i in range(self.x-1,-1,-1):
            
            if board[self.y][i][0:1] == "w":
                if self.type == "w" :
                    break
                else:
                    can_move_list.append([self.y,i])  
                    break
            elif board[self.y][i][0:1] == "b":
                if self.type == "w":
                    can_move_list.append([self.y,i])  
                    break
                else:
                    break 
            else :
                can_move_list.append([self.y,i])     

        #bishop movement+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        right = True
        left = True
        direction =[(-1,1,"downleft"),(-1,-1,"upleft"),(1,-1,"upright"),(1,1,"downright")]
        fake_x1,fake_y1 = self.x,self.y
        fake_x2,fake_y2 = self.x,self.y
        #up
        for i in range(self.y-1,-1,-1):
            fake_x1+=direction[2][0]
            fake_y1=i
            # print(fake_y1,fake_x1,"upRIght")
            #right
            if fake_x1<8 and right and fake_y2>=0:
                
                if board[fake_y1][fake_x1][0:1] == "b":
                    if self.type =="b":

                        right = False
                    else:
                        can_move_list.append([fake_y1,fake_x1])
                        right = False
                elif board[fake_y1][fake_x1][0:1] == "w":
                    if self.type =="w":

                        right = False
                    else:
                        can_move_list.append([fake_y1,fake_x1])
                        right = False

                else:
                    can_move_list.append([fake_y1,fake_x1])
            #left
            fake_x2+=direction[1][0]
            fake_y2=i
            # print(fake_y2,fake_x2,"upleft")
            if fake_x2>=0 and left and fake_y2>=0:
                
                if board[fake_y2][fake_x2][0:1] == "b":
                    if self.type == "b":    
                        left = False
                    else :
                        can_move_list.append([fake_y2,fake_x2])
                        left = False
                elif board[fake_y2][fake_x2][0:1] == "w":
                    if self.type == "w":    
                        left = False
                    else :
                        can_move_list.append([fake_y2,fake_x2])
                        left = False
                else:
                    can_move_list.append([fake_y2,fake_x2])

        #down
        right = True
        left = True
        fake_x1,fake_y1 = self.x,self.y
        fake_x2,fake_y2 = self.x,self.y
        for i in range(self.y+1,8):
            fake_x1+=direction[3][0]
            fake_y1=i 
            #right
            if fake_x1<8 and right and fake_y1<8:
               

                if board[fake_y1][fake_x1][0:1] == "b":
                    if self.type == 'b':
                        right = False
                    else :
                        can_move_list.append([fake_y1,fake_x1])
                        right = False
                elif board[fake_y1][fake_x1][0:1] == "w":
                    if self.type == 'w':
                        right = False
                    else :
                        can_move_list.append([fake_y1,fake_x1])
                        right = False   
                else:
                
                    can_move_list.append([fake_y1,fake_x1])
            #left
            fake_x2+=direction[0][0]
            fake_y2= i
            if fake_x2>=0 and left and fake_y2<8 :
                

                if board[fake_y2][fake_x2][0:1] == "b":
                    if self.type == "b":
                        left = False
                    else:
                        can_move_list.append([fake_y2,fake_x2])
                        left = False
                elif board[fake_y2][fake_x2][0:1] == "w":
                    if self.type == "w":
                        left = False
                    else:
                        can_move_list.append([fake_y2,fake_x2])
                        left = False

                else:
                    can_move_list.append([fake_y2,fake_x2])

        
#King class that contains all the specifics infomation about king 
class king(pieces):
    white_king = True
    black_king = True
    def can_move_to(self,board):
        # X+1,y+1
        # x+1,y+0
        # x+1,y-1
        # x-1,y+1
        # x-1,y+0
        # x-1,y-1
        # x+0,y+1
        # X+0,Y-1
        for i in range(1,-2,-1):

            for j in range(1,-2,-1):
                n= self.x+i
                m= self.y+j
                
                if i == j == 0:
                    continue
                if (n==8 or n<0 or m==8 or m<0) :
                    continue

                
                # white king 
                if self.type == "w":
                    
                    if pieces.board[m][n][0:1]=="b":
                        can_move_list.append([m,n])
                    elif pieces.board[m][n][0:1]=="w":
                        # print(pieces.board[m][n])
                        continue
                    else:
                        can_move_list.append([m,n])

                # black king
                else:
                    if pieces.board[m][n][0:1]=="w":
                        can_move_list.append([m,n])
                    elif pieces.board[m][n][0:1]=="b":
                        continue
                    else:
                        can_move_list.append([m,n])
        

        if self.type == "w":
            if not(check_to_white):
                #if white king is untouched 
                if king.white_king:
                    # if white rook 1 is untouched cannot do short castle
                    if rook.white_r1:
                        #just to count how many pieces are there between rook and king
                        peice_count = 0 
                        for i in range(1,4):
                            if board[self.y][self.x-i] != "__":
                                # print(pieces.board[self.y][self.x-i])
                                peice_count += 1
                            if [self.y,self.x-i] in all_moves_list and i != 3:
                                peice_count+=1    
                        if peice_count == 0:
                            can_move_list.append([self.y,self.x-2])
                    # if white rook 2 is untouched cannot do lon g castle 
                    if rook.white_r2:
                        #just to count how many pieces are there between rook and king
                        peice_count = 0 
                        for i in range(1,3):
                            if board[self.y][self.x+i] != "__":
                                # print(pieces.board[self.y][self.x+i])
                                peice_count += 1
                            if [self.y,self.x+i] in all_moves_list:
                                peice_count+=1    
                        if peice_count == 0:
                            can_move_list.append([self.y,self.x+2])
        elif self.type == "b":
            if not(check_to_black):
                #if white king is untouched 
                if king.black_king:
                    # if white rook 1 is untouched cannot do short castle
                    if rook.black_r1:
                        #just to count how many pieces are there between rook and king
                        peice_count = 0 
                        for i in range(1,4):
                            if board[self.y][self.x-i] != "__":
                                # print(pieces.board[self.y][self.x-i])
                                peice_count += 1
                            if [self.y,self.x-i] in all_moves_list and i != 3:
                                peice_count+=1    
                        if peice_count == 0:
                            can_move_list.append([self.y,self.x-2])
                    # if white rook 2 is untouched cannot do lon g castle 
                    if rook.black_r2:
                        #just to count how many pieces are there between rook and king
                        peice_count = 0 
                        for i in range(1,3):
                            if board[self.y][self.x+i] != "__":
                                # print(pieces.board[self.y][self.x+i])
                                peice_count += 1
                            if [self.y,self.x+i] in all_moves_list:
                                peice_count+=1    
                        if peice_count == 0:
                            can_move_list.append([self.y,self.x+2])
#upper stuff is just racism  :)


#to load images before loop because it is a very heavy thing to do for coomputer
for i in pieces.board:
    for j in i:
        if j != '__':
            peices_images[j[0:-1]] = pygame.image.load("chess_peices/"+j[0:-1]+'.png')

peices_images['bc1'] = pygame.image.load("chess_peices/bc.png")





def flip_board(board):
    global fliped_board
    fliped_board = []
    for i in range(7,-1,-1):
        semi_board=[]
        for j in range(7,-1,-1):
            semi_board.append(board[i][j])
        fliped_board.append(semi_board)

# display the pieces on the board
def display(board):
    move_list = copy.deepcopy(can_move_list)
    #drawing the board
    window.blit(chess_board,(0,0+Margin))
    # for i in range(0,8):
    #     for j in range(i%2,8,2):
    #         pygame.draw.rect(window,white,(i*boxsize,j*boxsize+Margin,boxsize,boxsize))
    
    y=0
    for i in board:
        x = 0
        # print(i)
        for j in i:

            if j != '__' :
                window.blit(peices_images[j[0:-1]],(x*boxsize,y*boxsize+Margin))
            x += 1
        y+= 1
    
    if flip == "black":
        for element in move_list:
            for i,n in zip(range(8),range(7,-1,-1)):
                for j,m in zip(range(8),range(7,-1,-1)):
                    if [i,j] == element:
                        index = move_list.index(element)
                        move_list.remove(element)
                        move_list.insert(index,[n,m])
                        break
    for i in move_list:
        p_x,p_y=(i[1])*boxsize,(i[0])*boxsize
        window.blit(peices_images['bc1'],(p_x,p_y+Margin))



# this function distributes pieces white and black player
# seems waste but very important  
def peices_dist(board):
    global w_peices,b_peices
    w_peices = []
    b_peices = []
    for i in range(8):
        for j in range(8):
            #print(board[i][j][0:1])
            if board[i][j][0:1] == "w":
                w_peices.append([i,j])
            elif board[i][j][0:1] == "b":
                b_peices.append([i,j])


# choose which peice to move
def choose_peice(turn):
    skip = False
    piece =None
    if turn == "white":
        for i in w_peices:
            p_x,p_y=(i[1])*boxsize,(i[0])*boxsize+Margin
            x, y = pygame.mouse.get_pos()
            if x <= p_x + 75 and x >= p_x and y >= p_y - 0 and y <= p_y + 75:
                for event in pygame.event.get(pygame.MOUSEBUTTONDOWN):
                    if event.button == 1:                      
                        piece = i
    else:
        for i in b_peices:
            p_x, p_y = (i[1]) * boxsize, (i[0]) * boxsize+Margin
            x, y = pygame.mouse.get_pos()
            if x <= p_x + 75 and x >= p_x and y >= p_y - 0 and y <= p_y + 75:
                for event in pygame.event.get(pygame.MOUSEBUTTONDOWN):
                    if event.button == 1:
                        # print(i)
                        piece = i
    if flip == "black" and piece != None:
        for i,n in zip(range(8),range(7,-1,-1)):
            for j,m in zip(range(8),range(7,-1,-1)):
                if [n,m] == piece:
                    piece = [i,j]
                    skip = True  
                    print(turn,pieces.board[piece[0]][piece[1]])
                    break
            if skip == True:
                skip = False
                break    
    return piece
# it changes information into information which is usable in pieces class                
def peice_info(peice,x,y):

    return peice[0:1],peice[1:-1],x,y
        

# this function is used to choose where to move 
def move_to():
    global turn
    skip = False
    move = None
    move_list = copy.deepcopy(can_move_list)
    if flip == "black":
        for element in move_list:
            for i,n in zip(range(8),range(7,-1,-1)):
                for j,m in zip(range(8),range(7,-1,-1)):
                    if [i,j] == element:
                        index = move_list.index(element)
                        move_list.remove(element)
                        move_list.insert(index,[n,m])
                        break
                    
                    # real_list= [n,m]
    
    for i in move_list:
            
        p_x,p_y=(i[1])*boxsize,(i[0])*boxsize+Margin
        x, y = pygame.mouse.get_pos()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
        
            if x <= p_x + 75 and x >= p_x and y >= p_y - 0 and y <= p_y + 75:
                if event.button == 1:
                    # can_move_list =[]
                    
                    move = i 
                    break
                break
    if flip == 'black' and move != None:
        for i,n in zip(range(8),range(7,-1,-1)):
            for j,m in zip(range(8),range(7,-1,-1)):
                if [n,m] == move:
                    move = [i,j]
                    skip = True
                    break
            if skip == True:
                skip = False 
                break 
    return move
# this used to make pawn promote to a higher peice
def pawn_promotion(b):
    global run
    ix=150
    iy= 300-37
    running = True
    button_list = [(ix,iy),(ix+75,iy),(ix+(75*2),iy),(ix+(75*3),iy)]
    for i in range (8):
        if b[0][i][0:2] == "wp":
            
            while running:
                window.blit(chessbuttonW,(ix,iy))
                pygame.display.flip()        
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        run = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x,y = event.pos
                        for n in button_list:
                            p_x = n[0]
                            p_y = n[1]
                            # print(p_x,p_y)
                            if x <= p_x + 75 and x >= p_x and y >= p_y - 0 and y <= p_y + 75:
                                if event.button == 1:
                                    if (p_x,p_y) == button_list[0]:
                                        # print("Rook")
                                        pieces.board[0][i] = 'wr3'
                                        running = False
                                    elif (p_x,p_y) == button_list[1]:
                                        # print("Kinght")
                                        pieces.board[0][i] = 'wkn3'
                                        running = False
                                    elif (p_x,p_y) == button_list[2]:
                                        # print("bishop")
                                        pieces.board[0][i] = 'wb3'
                                        running = False  
                                    elif (p_x,p_y) == button_list[3]:
                                        # print("queen")
                                        pieces.board[0][i] = 'wq3'     
                                        running = False   
        elif b[7][i][0:2] == "bp":
            while running:
                window.blit(chessbuttonB,(ix,iy))
                pygame.display.flip()        
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        run = False
                        
                    
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x,y = event.pos
                        for n in button_list:
                            p_x = n[0]
                            p_y = n[1]
                            # print(p_x,p_y)
                            if x <= p_x + 75 and x >= p_x and y >= p_y - 0 and y <= p_y + 75:
                                if event.button == 1:
                                    if (p_x,p_y) == button_list[0]:
                                        # print("Rook")
                                        pieces.board[7][i] = 'br3'
                                        running = False
                                    elif (p_x,p_y) == button_list[1]:
                                        # print("Kinght")
                                        pieces.board[7][i] = 'bkn3'
                                        running = False
                                    elif (p_x,p_y) == button_list[2]:
                                        # print("bishop")
                                        pieces.board[7][i] = 'bb3'
                                        running = False  
                                    elif (p_x,p_y) == button_list[3]:
                                        # print("queen")
                                        pieces.board[7][i] = 'bq3'     
                                        running = False   
        else:
            continue

# give all the place where player can move   
def all_moves(turn,board):
    global can_move_list,all_moves_list
    all_moves_list =[]
    
    if turn == "black":
        for i in w_peices:
            can_move_list=[]
            loc = board[i[0]][i[1]]

            name = loc[1:-1]
            p = pieces('w',name,i[0],i[1])
            if name  == "p":
                pawn.can_move_to(p,board)
            elif name == "kn":
                knight.can_move_to(p,board)               
            elif name == "b":
                bishop.can_move_to(p,board)
            elif name == "r":
                rook.can_move_to(p,board)            
            elif name == "q":
                queen.can_move_to(p,board)        
            elif name == "k":
                king.can_move_to(p,board)
            all_moves_list.extend(can_move_list)   
           
    elif turn == "white":
        for i in b_peices:
            can_move_list=[]
            loc = board[i[0]][i[1]]
            name = loc[1:-1]
            p = pieces('b',name,i[0],i[1])
            if name  == "p":
                pawn.can_move_to(p,board)
            elif name == "kn":
                knight.can_move_to(p,board)
            elif name == "b":
                bishop.can_move_to(p,board)
            elif name == "r":
                rook.can_move_to(p,board)            
            elif name == "q":
                queen.can_move_to(p,board)        
            elif name == "k":
                king.can_move_to(p,board)
            all_moves_list.extend(can_move_list)
    can_move_list = []


def all_legal_moves(turn,board):
    global can_move_list,all_legal_moves_list
    all_legal_moves_list = []

    if turn == "white":
        for i in w_peices:
            peice = [i[0],i[1]]
            can_move_list=[]
            loc = board[i[0]][i[1]]

            name = loc[1:-1]
            p = pieces('w',name,i[0],i[1])
            if name  == "p":
                pawn.can_move_to(p,board)
            elif name == "kn":
                knight.can_move_to(p,board)               
            elif name == "b":
                bishop.can_move_to(p,board)
            elif name == "r":
                rook.can_move_to(p,board)            
            elif name == "q":
                queen.can_move_to(p,board)        
            elif name == "k":
                king.can_move_to(p,board)    
            all_legal_moves_list.extend(illegal_move(turn,can_move_list,peice,board))   
           
    else:
        for i in b_peices:
            peice = [i[0],i[1]]
            can_move_list=[]
            loc = board[i[0]][i[1]]
            name = loc[1:-1]
            p = pieces('b',name,i[0],i[1])
            if name  == "p":
                pawn.can_move_to(p,board)
            elif name == "kn":
                knight.can_move_to(p,board)
            elif name == "b":
                bishop.can_move_to(p,board)
            elif name == "r":
                rook.can_move_to(p,board)            
            elif name == "q":
                queen.can_move_to(p,board)        
            elif name == "k":
                king.can_move_to(p,board)
            
            all_legal_moves_list.extend(illegal_move(turn,can_move_list,peice,board))
    can_move_list = []

    
# calculatues if there is any check to king
def check(turn,board):
    global check_to_white,check_to_black
    king = []
    check_to_white = False
    check_to_black = False
    if turn == "white":
        for i in range(8):
            for j in range(8):
                if board[i][j][0:-1]=='wk':
                    king = [i,j]
                    
        
        if (king in all_moves_list):
            check_to_white = True 
            # print("check to white ")
    else:
        for i in range(8):
            for j in range(8):
                if board[i][j][0:-1]=='bk':
                    king = [i,j]
                    
       
        if (king in all_moves_list):
            check_to_black = True
            # print("check to black")

def illegal_move(turn,moves,peice,board):

    to_remove=[]
    
    for i in moves:
        fake_board = copy.deepcopy(board)
        if fake_board[peice[0]][peice[1]][1:-1] == "p":

            # if black can enpassent white 
            if pawn.enpassentW[0]:
                if move == pawn.enpassentW[1]:                
                    fake_board[enpassent_loc[0]][enpassent_loc[1]] ="__"
                    
            # if white can enpassent black 
            if pawn.enpassentB[0]:
                if move == pawn.enpassentB[1]:
                    fake_board[enpassent_loc[0]][enpassent_loc[1]] ="__"

            fake_board[i[0]] [i[1]] = fake_board[peice[0]][peice[1]]
            fake_board[peice[0]][peice[1]] = "__"

        

        else:

            if fake_board[peice[0]][peice[1]] == "bk1":
                # this is for long castle for black king
                if [i[0],i[1]] == [peice[0],peice[1]-2]:
                    fake_board[i[0]][i[1]+1] = "br1"
                    fake_board[peice[0]][peice[1]-4] ='__'
                    # print("long castle")
                # this is for short castle for black king 
                if [i[0],i[1]] == [peice[0],peice[1]+2]:
                    fake_board[i[0]][i[1]-1] = "br2"
                    fake_board[peice[0]][peice[1]+3] ='__'
                    # print("short castle")    
                
            elif fake_board[peice[0]][peice[1]] == "wk1":
                # this is for long castle for white king
                if [i[0],i[1]] == [peice[0],peice[1]-2]:
                    fake_board[i[0]][i[1]+1] = "wr1"
                    fake_board[peice[0]][peice[1]-4] ='__'
                    # print("long castle")
                # this is for short castle for white king
                if [i[0],i[1]] == [peice[0],peice[1]+2]:
                    fake_board[i[0]][i[1]-1] = "wr2"
                    fake_board[peice[0]][peice[1]+3] ='__'
                    # print("short castle")    

               
            # print(i,peice)
            fake_board[i[0]][i[1]] = fake_board[peice[0]][peice[1]]
            fake_board[peice[0]][peice[1]] = "__"     
      


        peices_dist(fake_board)
        all_moves(turn,fake_board)
        check(turn,fake_board)
        if turn == "white":
            # print('WHITE')
            if check_to_white:
                to_remove.append(i)
        else :
            # print("BLACK")
            if check_to_black:
                to_remove.append(i)           
    
    for i in to_remove:
        moves.remove(i)             
    
    return moves


def evaluate(board,color):

    pawntable_w = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [50, 50, 50, 50, 50, 50, 50, 50],
        [10, 10, 20, 30, 30, 20, 10, 10],
        [5, 5, 10, 25, 25, 10, 5, 5],
        [0, 0, 0, 20, 20, 0, 0, 0],
        [5, -5, -10, 0, 0, -10, -5, 5],
        [5, 10, 10, -20, -20, 10, 10, 5],
        [0, 0, 0, 0, 0, 0, 0, 0]]
    pawntable_b = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [5, 10, 10, -20, -20, 10, 10, 5],
        [5, -5, -10, 0, 0, -10, -5, 5],
        [0, 0, 0, 20, 20, 0, 0, 0],
        [5, 5, 10, 25, 25, 10, 5, 5],
        [10, 10, 20, 30, 30, 20, 10, 10],
        [50, 50, 50, 50, 50, 50, 50, 50],
        [0, 0, 0, 0, 0, 0, 0, 0]]
    knightstable = [
        [-50, -40, -30, -30, -30, -30, -40, -50],
        [-40, -20, 0, 5, 5, 0, -20, -40,],
        [-30, 5, 10, 15, 15, 10, 5, -30,],
        [-30, 0, 15, 20, 20, 15, 0, -30,],
        [-30, 5, 15, 20, 20, 15, 5, -30,],
        [-30, 0, 10, 15, 15, 10, 0, -30,],
        [-40, -20, 0, 0, 0, 0, -20, -40,],
        [-50, -40, -30, -30, -30, -30, -40, -50]]
    bishopstable = [
        [-20, -10, -10, -10, -10, -10, -10, -20,],
        [-10, 5, 0, 0, 0, 0, 5, -10,],
        [-10, 10, 10, 10, 10, 10, 10, -10,],
        [-10, 0, 10, 10, 10, 10, 0, -10,],
        [-10, 5, 5, 10, 10, 5, 5, -10,],
        [-10, 0, 5, 10, 10, 5, 0, -10,],
        [-10, 0, 0, 0, 0, 0, 0, -10,],
        [-20, -10, -10, -10, -10, -10, -10, -20]]
    rookstable_b = [
        [0, 0, 0, 5, 5, 0, 0, 0,],
        [-5, 0, 0, 0, 0, 0, 0, -5,],
        [-5, 0, 0, 0, 0, 0, 0, -5,],
        [-5, 0, 0, 0, 0, 0, 0, -5,],
        [-5, 0, 0, 0, 0, 0, 0, -5,],
        [-5, 0, 0, 0, 0, 0, 0, -5,],
        [5, 10, 10, 10, 10, 10, 10, 5,],
        [0, 0, 0, 0, 0, 0, 0, 0]]
    rookstable_w = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [5, 10, 10, 10, 10, 10, 10, 5],
        [-5, 0, 0, 0, 0, 0, 0, -5],
        [-5, 0, 0, 0, 0, 0, 0, -5],
        [-5, 0, 0, 0, 0, 0, 0, -5],
        [-5, 0, 0, 0, 0, 0, 0, -5],
        [-5, 0, 0, 0, 0, 0, 0, -5],
        [0, 0, 0, 5, 5, 0, 0, 0]]
    queenstable = [
        [-20, -10, -10, -5, -5, -10, -10, -20,],
        [-10, 0, 0, 0, 0, 0, 0, -10,],
        [-10, 5, 5, 5, 5, 5, 0, -10,],
        [0, 0, 5, 5, 5, 5, 0, -5,],
        [-5, 0, 5, 5, 5, 5, 0, -5,],
        [-10, 0, 5, 5, 5, 5, 0, -10,],
        [-10, 0, 0, 0, 0, 0, 0, -10,],
        [-20, -10, -10, -5, -5, -10, -10, -20]]
    kingstable_b = [
        [20, 30, 10, 0, 0, 10, 30, 20,],
        [20, 20, 0, 0, 0, 0, 20, 20,],
        [-10, -20, -20, -20, -20, -20, -20, -10,],
        [-20, -30, -30, -40, -40, -30, -30, -20,],
        [-30, -40, -40, -50, -50, -40, -40, -30,],
        [-30, -40, -40, -50, -50, -40, -40, -30,],
        [-30, -40, -40, -50, -50, -40, -40, -30,],
        [-30, -40, -40, -50, -50, -40, -40, -30]]
    kingstable_w = [
        [-30, -40, -40, -50, -50, -40, -40, -30],
        [-30, -40, -40, -50, -50, -40, -40, -30],
        [-30, -40, -40, -50, -50, -40, -40, -30],
        [-30, -40, -40, -50, -50, -40, -40, -30],
        [-20, -30, -30, -40, -40, -30, -30, -20],
        [-10, -20, -20, -20, -20, -20, -20, -10],
        [20, 20, 0, 0, 0, 0, 20, 20],
        [20, 30, 10, 0, 0, 10, 30, 20]]
    
    white_score = 0
    black_score = 0
    peices_dist(board)
    for i in w_peices:
        if board[i[0]][i[1]][1:-1] == "b":
            white_score += (30 + (bishopstable[i[0]][i[1]]/10))
            
        if board[i[0]][i[1]][1:-1] == "r":
            white_score += 50 + (rookstable_w[i[0]][i[1]]/10)
           
        if board[i[0]][i[1]][1:-1] == "kn":
            white_score += (30+ (knightstable[i[0]][i[1]]/10))
           
        if board[i[0]][i[1]][1:-1] == "q":
            white_score += (90 + (queenstable[i[0]][i[1]]/10))
           
        if board[i[0]][i[1]][1:-1] == "p":
            white_score += 10+(pawntable_w[i[0]][i[1]]/10)
            
        if board[i[0]][i[1]][1:-1] == "k":
            white_score += 900+(kingstable_w[i[0]][i[1]]/10)
    
    for i in b_peices:
        if board[i[0]][i[1]][1:-1] == "b":
            black_score += (30 + (bishopstable[i[0]][i[1]]/10))
        
        if board[i[0]][i[1]][1:-1] == "r":
            black_score += 50 + (rookstable_b[i[0]][i[1]]/10)
            

        if board[i[0]][i[1]][1:-1] == "kn":
            black_score += (30 +(knightstable[i[0]][i[1]]/10))
        

        if board[i[0]][i[1]][1:-1] == "q":
            black_score += (90 + (queenstable[i[0]][i[1]]/10))
            

        if board[i[0]][i[1]][1:-1] == "p":
            black_score += 10+(pawntable_b[i[0]][i[1]]/10)
            
        if board[i[0]][i[1]][1:-1] == "k":
            black_score +=  900+(kingstable_b[i[0]][i[1]]/10)
    
    
    if winner(board,color) == "white":
        black_score = 0
    elif winner(board,color) == "black":
        white_score = 0        
    print(white_score-black_score)     
    return black_score - white_score


def all_moves_of_peice(peice,color,board):

    loc = board[peice[0]][peice[1]]
    moves = []
    name = loc[1:-1]
    p = pieces(color[0:1],name,peice[0],peice[1])
    if name  == "p":
        pawn.can_move_to(p,board)
    elif name == "kn":
        knight.can_move_to(p,board)               
    elif name == "b":
        bishop.can_move_to(p,board)
    elif name == "r":
        rook.can_move_to(p,board)            
    elif name == "q":
        queen.can_move_to(p,board)        
    elif name == "k":
        king.can_move_to(p,board)
    moves = illegal_move(color,can_move_list,peice,board)    
    return moves


def simulated_move_data(board,color):
    peices_dist(board)
    move_data = []
    if color == "white":
        for i in w_peices:
            for j in all_moves_of_peice(i,"white",board):
                move_data.append((i,j))
    else:
        for i in b_peices:
            for j in all_moves_of_peice(i,"black",board):
                move_data.append((i,j))

    return move_data        


def simulate_move(move,piece,board):

    global enpassent_loc

    #if user choose pawn
    temp_board = copy.deepcopy(board) 
    if temp_board[piece[0]][piece[1]][1:-1] == "p":
        # if black can enpassent white 
        if pawn.enpassentW[0]:
            if move == pawn.enpassentW[1]:
                
                temp_board[enpassent_loc[0]][enpassent_loc[1]] ="__"
                pawn.enpassentW = [False,[]]
                pawn.enpassentB = [False,[]]
                # pawn.enpasant_pawn_loc=[]
                enpassent_loc = []

        # if white can enpassent black 
        if pawn.enpassentB[0]:
            if move == pawn.enpassentB[1]:

                temp_board[enpassent_loc[0]][enpassent_loc[1]] ="__"
                pawn.enpassentW = [False,[]]
                pawn.enpassentB = [False,[]]
                # pawn.enpasant_pawn_loc=[]
                enpassent_loc = []
        #if its white's turn  
        if temp_board[piece[0]][piece[1]][0:1] == "w":
            #if white move two squares then location will be saved for next move and enpassentW will be "TRUE" for next turn 
            # print(pawn.enpasant_pawn_loc,move)
            if 4 == move[0]:
                pawn.enpassentW=[True,[move[0]+1,move[1]]]
                
                #this variables contains the location of pawn that move 2 squares 
                enpassent_loc = (move[0],move[1])   
                

        # if its black's turn 
        elif temp_board[piece[0]][piece[1]][0:1] == "b":
            #if black moves two squares then location will be saved for next move and enpassentW will be "TRUE" for next turn 
            if 3 == move[0]:
                
                pawn.enpassentB = [True,[move[0]-1,move[1]]]

                #this variable is contains the location of pawn that move 2 squares 
                enpassent_loc = (move[0],move[1])     

        

        temp_board[move[0]] [move [1]] = temp_board[piece[0]][piece[1]]
        temp_board[piece[0]][piece[1]] = "__"

    
    else:

        if temp_board[piece[0]][piece[1]] == "wr1":
            rook.white_r1 = False
        elif temp_board[piece[0]][piece[1]] == "wr2":
            rook.white_r2 = False
        elif temp_board[piece[0]][piece[1]] == "br1":
            rook.black_r1 = False
        elif temp_board[piece[0]][piece[1]] == "br2": 
            rook.black_r2 = False

        elif temp_board[piece[0]][piece[1]] == "bk1":
            # this is for long castle for black king
            if [move[0],move[1]] == [piece[0],piece[1]-2]:
                temp_board[move[0]][move[1]+1] = "br1"
                temp_board[piece[0]][piece[1]-4] ='__'
                # print("long castle")
            # this is for short castle for black king 
            if [move[0],move[1]] == [piece[0],piece[1]+2]:
                temp_board[move[0]][move[1]-1] = "br2"
                temp_board[piece[0]][piece[1]+3] ='__'
                # print("short castle")    

            king.black_king = False     
            
        elif temp_board[piece[0]][piece[1]] == "wk1":
            # this is for long castle for white king
            if [move[0],move[1]] == [piece[0],piece[1]-2]:
                temp_board[move[0]][move[1]+1] = "wr1"
                temp_board[piece[0]][piece[1]-4] ='__'
                # print("long castle")
            # this is for short castle for white king
            if [move[0],move[1]] == [piece[0],piece[1]+2]:
                temp_board[move[0]][move[1]-1] = "wr2"
                temp_board[piece[0]][piece[1]+3] ='__'
                # print("short castle")    

            king.white_king = False    

        # pawn.enpasant_pawn_loc=[]
        pawn.enpassentW = [False,[]]
        pawn.enpassentB = [False,[]] 
        temp_board[move[0]] [move [1]] = temp_board[piece[0]][piece[1]]
        temp_board[piece[0]][piece[1]] = "__"     
        enpassent_loc = []

    return temp_board,piece,move


def minmax(level,max_player,board,alpha,beta,turn):
    global enpassent_loc
    if level == 0 or winner(board,turn)!=None:
        return evaluate(board,turn) , 0 ,0
    if max_player:
        max_eval = float('-inf')
        best_move = None
        for i in simulated_move_data(board,"black"):
            
            con_enpassentW = copy.deepcopy(pawn.enpassentW)
            con_enpassentB = copy.deepcopy(pawn.enpassentB)
            con_enpassent_loc = copy.deepcopy(enpassent_loc)
            con_wr1 = rook.white_r1
            con_wr2 = rook.white_r2
            con_br1 = rook.black_r1
            con_br2 = rook.black_r2
            con_white_king = king.white_king
            con_black_king = king.black_king
            temp_board,p,m = simulate_move(i[1],i[0],board)
            
            evaluation = minmax(level-1,False,temp_board,alpha,beta,"white")[0]

            pawn.enpassentW  =copy.deepcopy(con_enpassentW)
            pawn.enpassentB  =copy.deepcopy(con_enpassentB)
            enpassent_loc = copy.deepcopy(con_enpassent_loc)
            rook.white_r1 = con_wr1
            rook.white_r2 = con_wr2
            rook.black_r1 = con_br1
            rook.black_r2 = con_br2
            king.white_king  =con_white_king
            king.black_king  =con_black_king

            max_eval = max(max_eval,evaluation)
            alpha = max(alpha,max_eval)
            if max_eval == evaluation:
                best_move = m
                piece = p
            # print("max",alpha,beta)
            if beta <= alpha:
                break
        return max_eval,best_move,piece


    else:
        min_eval = float('inf')
        best_move = None
        temp_board = copy.deepcopy(board)

        for i in simulated_move_data(board,"white"):

            con_enpassentW = copy.deepcopy(pawn.enpassentW)
            con_enpassentB = copy.deepcopy(pawn.enpassentB)
            con_enpassent_loc = copy.deepcopy(enpassent_loc)
            con_wr1 = rook.white_r1
            con_wr2 = rook.white_r2
            con_br1 = rook.black_r1
            con_br2 = rook.black_r2
            con_white_king = king.white_king
            con_black_king = king.black_king

            temp_board,p,m=simulate_move(i[1],i[0],board)
            evaluation = minmax(level-1,True,temp_board,alpha,beta,"black")[0]

            pawn.enpassentW  =copy.deepcopy(con_enpassentW)
            pawn.enpassentB  =copy.deepcopy(con_enpassentB)
            enpassent_loc = copy.deepcopy(con_enpassent_loc)
            rook.white_r1 = con_wr1
            rook.white_r2 = con_wr2
            rook.black_r1 = con_br1
            rook.black_r2 = con_br2
            king.white_king  =con_white_king
            king.black_king  =con_black_king

            min_eval = min(min_eval,evaluation)
            beta = min(beta,min_eval)
            if min_eval == evaluation:
                best_move = m
                piece = p
            
            # print("min",alpha,beta)
            if beta<= alpha:
                break
        return min_eval,best_move,piece
#decide winner of game


def winner(board,turn):
    peices_dist(board)
    all_legal_moves(turn,board)
    check(turn,board)
    if len(all_legal_moves_list)==0:
        if turn== "white":
            if check_to_white:
                return "black"
                print("black wins")
            
            else :
                return "draw"
                print("draw by stalemate")    
        elif turn == "black":
            if check_to_black:
                return "white"
                print("white wins")
            
            else :
                return "draw"
                print("draw by stalemate")            


#game running variable
run = True

#main loop
while run:
    

    # window.fill((0,139,139))
    keys = pygame.key.get_pressed()
    flip_board(pieces.board)
    if flip == "black":
        peices_dist(fliped_board)
    else :
        peices_dist(pieces.board)
         
    choosen_peice_index = choose_peice(turn)
    # if turn == "black":
    #     if jeet == None:
    #         evalution,ai_move,choosen_peice_index = minmax(2,True,pieces.board,float('-inf'),float('inf'),turn)

    
    if choosen_peice_index != None:
        
        choosen_peice = peice_info(pieces.board[choosen_peice_index[0]][choosen_peice_index[1]],choosen_peice_index[0],choosen_peice_index[1])

        p = pieces(*choosen_peice)
        can_move_list= []
        name = choosen_peice[1]
        

        if name  == "p":
            pawn.can_move_to(p,pieces.board)
        elif name == "kn":
            knight.can_move_to(p,pieces.board)
        elif name == "b":
            bishop.can_move_to(p,pieces.board)
        elif name == "r":
            rook.can_move_to(p,pieces.board)            
        elif name == "q":
            queen.can_move_to(p,pieces.board)        
        elif name == "k":
            king.can_move_to(p,pieces.board)
           

        can_move_list = illegal_move(turn,can_move_list,[choosen_peice[2],choosen_peice[3]],pieces.board)
       

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                if flip == 'black':
                    flip = "white"
                else :
                    flip = "black"        
        move = move_to()
        # if turn =="black":
        #     if jeet == None:
        #         move = ai_move
        if move != None:
            
            move_made = True
            #if user choose pawn 
            if pieces.board[choosen_peice[2]][choosen_peice[3]][1:-1] == "p":
                # if black can enpassent white 
                if pawn.enpassentW[0]:
                    if move == pawn.enpassentW[1]:
                        
                        pieces.board[enpassent_loc[0]][enpassent_loc[1]] ="__"
                        pawn.enpassentW = [False,[]]
                        pawn.enpassentB = [False,[]]
                        # pawn.enpasant_pawn_loc=[]
                        enpassent_loc = []

                # if white can enpassent black 
                if pawn.enpassentB[0]:
                    if move == pawn.enpassentB[1]:

                        pieces.board[enpassent_loc[0]][enpassent_loc[1]] ="__"
                        pawn.enpassentW = [False,[]]
                        pawn.enpassentB = [False,[]]
                        # pawn.enpasant_pawn_loc=[]
                        enpassent_loc = []
                #if its white's turn  
                if pieces.board[choosen_peice[2]][choosen_peice[3]][0:1] == "w":
                    #if white move two squares then location will be saved for next move and enpassentW will be "TRUE" for next turn 
                    # print(pawn.enpasant_pawn_loc,move)
                    if 4 == move[0]:
                        pawn.enpassentW=[True,[move[0]+1,move[1]]]
                        
                        #this variables contains the location of pawn that move 2 squares 
                        enpassent_loc = (move[0],move[1])   
                        

                # if its black's turn 
                elif pieces.board[choosen_peice[2]][choosen_peice[3]][0:1] == "b":
                    #if black moves two squares then location will be saved for next move and enpassentW will be "TRUE" for next turn 
                    if 3 == move[0]:
                        
                        pawn.enpassentB = [True,[move[0]-1,move[1]]]

                        #this variable is contains the location of pawn that move 2 squares 
                        enpassent_loc = (move[0],move[1])     

                

                pieces.board[move[0]] [move [1]] = pieces.board[choosen_peice[2]][choosen_peice[3]]
                pieces.board[choosen_peice[2]][choosen_peice[3]] = "__"

            

            else:

                if pieces.board[choosen_peice[2]][choosen_peice[3]] == "wr1":
                    rook.white_r1 = False
                elif pieces.board[choosen_peice[2]][choosen_peice[3]] == "wr2":
                    rook.white_r2 = False
                elif pieces.board[choosen_peice[2]][choosen_peice[3]] == "br1":
                    rook.black_r1 = False
                elif pieces.board[choosen_peice[2]][choosen_peice[3]] == "br2": 
                    rook.black_r2 = False

                elif pieces.board[choosen_peice[2]][choosen_peice[3]] == "bk1":
                    # this is for long castle for black king
                    if [move[0],move[1]] == [choosen_peice[2],choosen_peice[3]-2]:
                        pieces.board[move[0]][move[1]+1] = "br1"
                        pieces.board[choosen_peice[2]][choosen_peice[3]-4] ='__'
                        # print("long castle")
                    # this is for short castle for black king 
                    if [move[0],move[1]] == [choosen_peice[2],choosen_peice[3]+2]:
                        pieces.board[move[0]][move[1]-1] = "br2"
                        pieces.board[choosen_peice[2]][choosen_peice[3]+3] ='__'
                        # print("short castle")    

                    king.black_king = False     
                    
                elif pieces.board[choosen_peice[2]][choosen_peice[3]] == "wk1":
                    # this is for long castle for white king
                    if [move[0],move[1]] == [choosen_peice[2],choosen_peice[3]-2]:
                        pieces.board[move[0]][move[1]+1] = "wr1"
                        pieces.board[choosen_peice[2]][choosen_peice[3]-4] ='__'
                        # print("long castle")
                    # this is for short castle for white king
                    if [move[0],move[1]] == [choosen_peice[2],choosen_peice[3]+2]:
                        pieces.board[move[0]][move[1]-1] = "wr2"
                        pieces.board[choosen_peice[2]][choosen_peice[3]+3] ='__'
                        # print("short castle")    

                    king.white_king = False    

                # pawn.enpasant_pawn_loc=[]
                pawn.enpassentW = [False,[]]
                pawn.enpassentB = [False,[]] 
                pieces.board[move[0]] [move [1]] = pieces.board[choosen_peice[2]][choosen_peice[3]]
                pieces.board[choosen_peice[2]][choosen_peice[3]] = "__"     
                enpassent_loc = []
            if turn == "white":
                turn = "black"
            else :
                turn ="white" 
        # pygame.time.delay(100)       

        
    pawn_promotion(pieces.board)   
    if move_made: 
        
        evaluate(pieces.board,turn)
        jeet = winner(pieces.board,turn)
        
       
            
        move_made = False
    flip_board(pieces.board)

    if flip == "white":

        display(pieces.board)
    else :
        
        display(fliped_board)  
    pygame.display.update()
    
pygame.quit()
