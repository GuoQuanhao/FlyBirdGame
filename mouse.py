import pygame


arrow = ( "xX                      ",
          "X.X                     ",
          "X..X                    ",
          "X...X                   ",
          "X....X                  ",
          "X.....X                 ",
          "X......X                ",
          "X.......X               ",
          "X........X              ",
          "X.........X             ",
          "X......XXXXX            ",
          "X...X..X                ",
          "X..XX..X                ",
          "X.X XX..X               ",
          "XX   X..X               ",
          "X     X..X              ",
          "      X..X              ",
          "       X..X             ",
          "       X..X             ",
          "        XX              ",
          "                        ",
          "                        ",
          "                        ",
          "                        ")


no = (  "xX                      ",
        "X.X                     ",
        "X..X                    ",
        "X...X                   ",
        "X....X                  ",
        "X.....X                 ",
        "X......X                ",
        "X.......X               ",
        "X........X              ",
        "X.........X             ",
        "X..........X            ",
        "X...X..X....X           ",
        "X..X     X...X          ",
        "X.X        X..X         ",
        "XX           X.X        ",
        "X              XX       ",
        "                        ",
        "                        ",
        "                        ",
        "                        ",
        "                        ",
        "                        ",
        "                        ",
        "                        ")

def TestCursor(arrow):
    hotspot = None
    for y in range(len(arrow)):
        for x in range(len(arrow[y])):
            if arrow[y][x] in ['x', ',', 'O']:
                hotspot = x,y
                break
        if hotspot != None:
            break
    if hotspot == None:
        raise Exception("Error")
    s2 = []
    for line in arrow:
        s2.append(line.replace('x', 'X').replace(',', '.').replace('O',
'o'))
    cursor, mask = pygame.cursors.compile(s2, 'X', '.', 'o')
    size = len(arrow[0]), len(arrow)
    pygame.mouse.set_cursor(size, hotspot, cursor, mask)


