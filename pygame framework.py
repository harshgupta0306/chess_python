import pygame
pygame.init()

Height = 600
Width = 600
boxsize=Height//8
window = pygame.display.set_mode((Height,Width))
pygame.display.set_caption("chess")
clock = pygame.time.Clock()
#colors
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
black = (0,0,0)
white = (255,255,255)
brown = (150,75,0)

#turn dittermination
turn="white"

# coordinates of each square
# button = pygame.image.load("chess_peices/bc.png")
# button_rect = button.get_rect()
peices_images = {}

class peices:

    board = [['br1', 'bkn1', 'bb1', 'bq1', 'bk1', 'bb2', 'bkn2', 'br2'],
             ['bp1', 'bp2', 'bp3', 'bp4', 'bp5', 'bp6', 'bp7', 'bp8'],
             ['__', '__', '__', '__', '__', '__', '__', '__'],
             ['__', '__', '__', '__', '__', '__', '__', '__'],
             ['__', '__', '__', '__', '__', '__', '__', '__'],
             ['__', '__', '__', '__', '__', '__', '__', '__'],
             ['wp1', 'wp2', 'wp3', 'wp4', 'wp5', 'wp6', 'wp7', 'wp8'],
             ['wr1', 'wkn1', 'wb1', 'wq1', 'wk1', 'wb2', 'wkn2', 'wr2']
             ]

    black_list = [["black", "rook",0, 0], ["black", "knight", 1, 0], ["black", "bishop", 2, 0],["black", "queen", 3, 0],
                  ["black", "king", 4, 0], ["black", "bishop", 5, 0], ["black", "knight", 6, 0], ["black", "rook", 7, 0],
                  ["black", "pawn", 0, 1], ["black", "pawn", 1, 1], ["black", "pawn", 2, 1], ["black", "pawn", 3, 1],
                  ["black", "pawn", 4, 1], ["black", "pawn", 5, 1], ["black", "pawn", 6, 1], ["black", "pawn", 7, 1]

                  ]
    white_list = [["white", "pawn", 0, 6], ["white", "pawn", 1, 6], ["white", "pawn", 2, 6], ["white", "pawn", 3, 6],
                  ["white", "pawn", 4, 6], ["white", "pawn", 5, 6], ["white", "pawn", 6, 6], ["white", "pawn", 7, 6],
                  ["white", "rook", 0, 7], ["white", "knight", 1, 7], ["white", "bishop", 2, 7],["white", "queen", 3, 7],
                  ["white", "king", 4, 7], ["white", "bishop", 5, 7], ["white", "knight", 6, 7], ["white", "rook", 7, 7]
                  ]

    def __init__(self,type,name,col,row):
        self.type= type
        self.name = name
        self.row = row
        self.col = col
        self.x = boxsize*(col)
        self.y = boxsize*(row)
class pawn(peices):
    # def __init__(self):
    #     self.pinned = False
    #     self.can_move = True

    def can_move_to(self):
        y = 0
        for i in peices.board:
            x = 0
            for j in i:
                # print(j)
                if j == '__':
                    peices.board[y][x]='bc1'
                    print()


                x+=1
            y+=1
class knight(peices):

    def can_move_to(self):
        pass
    #     y = 0
    #     for i in peices.board:
    #         x = 0
    #         for j in i:
    #             # print(j)
    #             if j == '__':
    #                 peices.board[y][x] = 'bc1'
    #                 peices.can_move_list.append((x, y))
    #
    #             x += 1
    #         y += 1
class rook(peices):
    def can_move_to(self):
        pass
    #     y = 0
    #     for i in peices.board:
    #         x = 0
    #         for j in i:
    #             # print(j)
    #             if j == '__':
    #                 peices.board[y][x] = 'bc1'
    #                 peices.can_move_list.append((x, y))
    #
    #             x += 1
    #         y += 1
class bishop(peices):
    def can_move_to(self):
        pass

    #     y = 0
    #     for i in peices.board:
    #         x = 0
    #         for j in i:
    #             # print(j)
    #             if j == '__':
    #                 peices.board[y][x] = 'bc1'
    #                 peices.can_move_list.append((x, y))
    #
    #             x += 1
    #         y += 1
class queen(peices):
    def can_move_to(self):
        pass
        # y = 0
        # for i in peices.board:
        #     x = 0
        #     for j in i:
        #         # print(j)
        #         if j == '__':
        #             peices.board[y][x] = 'bc1'
        #             peices.can_move_list.append((x, y))
        #
        #
        #         x += 1
        #     y += 1
# to display board on the screen
def display():
    y=0
    for i in peices.board:
        x = 0
        # print(i)
        for j in i:

            if j != '__' :
                window.blit(peices_images[j],(x*boxsize,y*boxsize))
            x += 1
        y += 1


# to give coordinates easily
def coordinates(l1,l2):
    x = peices.board[peices.board.index(l1)].index(l2)*boxsize
    y = peices.board.index(l1)*boxsize
    return x,y

# to convert coordiinates to index
def index(x,y):
    row = y//boxsize
    col = x//boxsize
    return peices.board[row][col]


def choose_peice():
    if turn=="white":
        for i in peices.white_list:
            p=peices(*i)
            x,y = pygame.mouse.get_pos()
            if x <= p.x + 75 and x >= p.x and y >= p.y - 0 and y <= p.y + 75:
                for event in pygame.event.get(pygame.MOUSEBUTTONDOWN):
                    if event.button == 1:
                        print(p.x, p.y)

                        print(peices.white_list)
                        return i
    else :
        for i in peices.black_list:
            p = peices(*i)
            x, y = pygame.mouse.get_pos()
            if (x <= p.x + 75 and x >= p.x - 0 and y >= p.y - 0 and y <= p.y + 75):
                for event in pygame.event.get(pygame.MOUSEBUTTONDOWN):
                    if event.button == 1:

                        return i
def choose_loc():
    # print(peices.can_move_list)

    for i in can_move_list:

        x = i[1]*boxsize
        y = i[0]*boxsize
        x_pos, y_pos = pygame.mouse.get_pos()
        if (x_pos <= x + 75 and x_pos >= x- 0 and y_pos >= y - 0 and y_pos <= y + 75):

            for event in pygame.event.get(pygame.MOUSEBUTTONDOWN):
                if event.button == 1:

                    clear_space()
                # Set the x, y postions of the mouse click

                    return x//boxsize ,y//boxsize


def clear_space():
    for i in range (8):
        for j in range(8):
            if peices.board[i][j]=="bc1":
                peices.board[i][j] = '__'

def move_to():
    global can_move_list
    can_move_list = []
    for i in range(8):
        for j in range(8):
            if peices.board[i][j] == 'bc1':
                pass
                # can_move_list.append((i,j))
#
#to load images before loop because it is a very heavy thing to do for coomputer
for i in peices.board:
    for j in i:
        if j != '__':
            peices_images[j] = pygame.image.load("chess_peices/"+j[0:-1]+'.png')

peices_images['bc1'] = pygame.image.load("chess_peices/bc.png")

#game running variable
run = True
p = None
choosen_peices = None
#main loop
while run:
    clock.tick(120)
    window.fill(white)
    keys = pygame.key.get_pressed()

    #drawing the board
    for i in range(0,8):
        for j in range(i%2,8,2):
            pygame.draw.rect(window,brown,(i*boxsize,j*boxsize,boxsize,boxsize))

    #choosing which peice to move

    choosen_peices = choose_peice()
    if choosen_peices!= None:
        if choosen_peices[1] == 'pawn':
            clear_space()
            p = pawn(*choosen_peices)

        elif choosen_peices[1] == 'queen':
            clear_space()
            p = queen(*choosen_peices)

        elif choosen_peices[1] == 'rook':
            clear_space()
            p = rook(*choosen_peices)

        elif choosen_peices[1] == 'bishop':
            clear_space()
            p = bishop(*choosen_peices)

        elif choosen_peices[1] == 'knight':
            clear_space()
            p = knight(*choosen_peices)


    if p != None:
        p.can_move_to()
        loc = choose_loc()

        if loc != None:

            # print((loc[1],loc[0]),p.row,p.col)
            peices.board[loc[1]][loc[0]] = peices.board[p.row][p.col]
            peices.board[p.row][p.col] = '__'
            if p.type == "white":
                INDEX = peices.white_list.index([p.type,p.name,p.col,p.row])
                peices.white_list[INDEX][2] = loc[0]
                peices.white_list[INDEX][3] = loc[1]
                p = None
                choosen_peices = None
            elif p.type == "black":
                INDEX = peices.black_list.index([p.type,p.name,p.col,p.row])
                peices.black_list[INDEX][2] = loc[0]
                peices.black_list[INDEX][3] = loc[1]
                choosen_peices = None
                p = None

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            run = False

    # for i in peices.board:
        # print(i)

    display()
    move_to()

    pygame.display.update()
pygame.quit()
