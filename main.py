import pygame
import sys
import mouse
from bird import Bird
from pipeline import Pipeline


def create_map(flag1, flag2):
    mouse_flag = False
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    screen.blit(Pipeline.pineUp, (Pipeline.wallX, -300))
    screen.blit(Pipeline.pineDown, (Pipeline.wallX, 500))
    Pipeline.update_pipeline()

    if Bird.dead:
        Bird.status = 2
    elif Bird.jump:
        Bird.status = 1


    if flag1 and not flag2:
        screen.blit(Bird.birdStatus[Bird.status], (120, 350))
        Bird.bird_update()
        start_button()
        mouse_flag = True
        Pipeline.score = 0

    elif not flag1 and not flag2:
        screen.blit(Bird.birdStatus[Bird.status], (Bird.birdX, Bird.birdY))
        Bird.bird_update()
        screen.blit(font.render('Sore:' + str(Pipeline.score), -1, (255, 255, 255)), (100, 50))
        global static_score
        static_score = Pipeline.score
        mouse_flag = False

    elif not flag1 and flag2:
        get_result(static_score)
        mouse_flag = True


    elif flag1 and flag2:
        screen.blit(Bird.birdStatus[Bird.status], (Bird.birdX, Bird.birdY))
        start_button()
        mouse_flag = True
        Bird.bird_update()

    pygame.display.update()
    return mouse_flag


def check_dead(flag3, flag4):
    up_rect = pygame.Rect(Pipeline.wallX, -300,
                          Pipeline.pineUp.get_width() - 10,
                          Pipeline.pineUp.get_height())

    down_rect = pygame.Rect(Pipeline.wallX, 500,
                            Pipeline.pineDown.get_width() - 10,
                            Pipeline.pineDown.get_height())

    if not flag3 and not flag4:
        if up_rect.colliderect(Bird.birdRect) or down_rect.colliderect(Bird.birdRect):
            Bird.dead = True
        if not 0 < Bird.birdRect[1] < height:
            Bird.dead = True
            return True
        else:
            return False
    elif flag3 and flag4:
        Bird.dead = False
        return False


def get_result(score_get):
    final_text1 = 'Game_Over'
    final_text2 = 'Your final score is:' + str(score_get)
    ft1_font = pygame.font.SysFont('Arial', 70)
    ft2_font = pygame.font.SysFont('Arial', 50)
    ft1_surf = ft1_font.render(final_text1, 1, (242, 3, 36))
    ft2_surf = ft2_font.render(final_text2, 1, (253, 177, 6))

    screen.blit(ft1_surf, [screen.get_width() / 2 - ft1_surf.get_width() / 2, 100])
    screen.blit(ft2_surf, [screen.get_width() / 2 - ft2_surf.get_width() / 2, 200])
    again_button(static_score)
    pygame.display.flip()


def start_button():
    button_color = (72, 61, 139)
    text_color = (255, 255, 255)
    start_font = pygame.font.SysFont('Arial', 40)
    img_button = start_font.render("Start", True, text_color, button_color)
    screen.blit(img_button, [screen.get_width() / 2 - img_button.get_width() / 2,
                             screen.get_height() / 2 - img_button.get_height() / 2])
    screen.blit(font.render('Sore:' + str(0), -1, (255, 255, 255)), (100, 50))
    pygame.display.flip()


def again_button(score_get):
    button_color = (72, 61, 139)
    text_color = (255, 255, 255)
    start_font = pygame.font.SysFont('Arial', 40)
    img_button = start_font.render("Start Again", True, text_color, button_color)
    screen.blit(img_button, [screen.get_width() / 2 - img_button.get_width() / 2,
                             screen.get_height() / 2 - img_button.get_height() / 2])
    screen.blit(font.render('Sore:' + str(score_get), -1, (255, 255, 255)), (100, 50))
    pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont('Arial', 50)
    size = width, height = 400, 650
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    Pipeline = Pipeline()
    Bird = Bird()
    Flag = True
    again_flag = False
    mouse_shape = False

    while True:
        clock.tick(60)
        x, y = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x in range(127, 273) and y in range(311, 339) and not Flag and again_flag:
            if click[0] == 1:
                Bird.empty()
                Pipeline.empty()
                Flag = True
            if mouse_shape:
                mouse.TestCursor(mouse.no)
            else:
                mouse.TestCursor(mouse.arrow)
        elif x in range(127, 273) and y in range(311, 339) and not Flag and not again_flag:
            if mouse_shape:
                mouse.TestCursor(mouse.no)
            else:
                mouse.TestCursor(mouse.arrow)
        elif x in range(168, 232) and y in range(311, 339) and Flag and not again_flag:
            if click[0] == 1:
                Flag = False
                Bird.jump = True
            if mouse_shape:
                mouse.TestCursor(mouse.no)
            else:
                mouse.TestCursor(mouse.arrow)
        else:
            mouse.TestCursor(mouse.arrow)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not Bird.dead and not Flag:
                Bird.jump = True
                Bird.gravity = 5
                Bird.jump_speed = 10
            elif (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not Bird.dead and again_flag:
                Bird.jump = True
                Bird.gravity = 5
                Bird.jump_speed = 10
        background = pygame.image.load('picture/background.png')
        if check_dead(Flag, again_flag):
            again_flag = True
            if create_map(Flag, again_flag):
                mouse_shape = True
            else:
                mouse_shape = False
        else:
            if create_map(Flag, again_flag):
                mouse_shape = True
            else:
                mouse_shape = False
            again_flag = False

