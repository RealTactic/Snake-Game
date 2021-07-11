import pygame
import random

pygame.init()

background = (0, 0, 0)
red = (255, 0, 0)
dark_red = (20, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

X = 1100
Y = 900

ythresh = []
for i in range(Y):
    if str(i / 20).endswith(".0"):
        ythresh.append(i)
xthresh = []
for i in range(X):
    if str(i / 20).endswith(".0"):
        xthresh.append(i)

apple_size = 20

snk_size = 20

speed = snk_size

screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption("Snake")


def drawsnake(s):
    f1 = True
    savei = None
    for i33 in s:
        if f1:
            savei = i33
            f1 = False
        else:
            pygame.draw.rect(screen, blue, (i33[0], i33[1], snk_size, snk_size))
    pygame.draw.rect(screen, green, (savei[0], savei[1], snk_size, snk_size))
    pygame.draw.rect(screen, red, (apple_pos[0], apple_pos[1], apple_size, apple_size))


def drawgrid():
    for idx23, i23 in enumerate(xthresh):
        if not i23 == 0:
            if not idx23 >= 3:
                pygame.draw.line(screen, dark_red, [i23, 20], [i23, Y])
            else:
                pygame.draw.line(screen, dark_red, [i23, 0], [i23, Y])

    for i23 in ythresh:
        if not i23 == 0:
            pygame.draw.line(screen, dark_red, [0, i23], [X, i23])


font1 = pygame.font.SysFont("monospace", 19)
font2 = pygame.font.SysFont("monospace", 75)
Clock = pygame.time.Clock()

working = True

while working:
    playing = True
    snkX = 540
    snkY = 460
    apple_pos = [540, 620]
    score = 0
    direction = 4
    snake = [
        [snkX, snkY],
        [snkX, snkY - snk_size],
        [snkX, snkY - snk_size * 2]
    ]

    while playing:
        dirchange = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN and not dirchange:
                if event.key == pygame.K_LEFT and not direction == 2:
                    direction = 1
                    dirchange = True
                elif event.key == pygame.K_RIGHT and not direction == 1:
                    direction = 2
                    dirchange = True
                elif event.key == pygame.K_UP and not direction == 4:
                    direction = 3
                    dirchange = True
                elif event.key == pygame.K_DOWN and not direction == 3:
                    direction = 4
                    dirchange = True
        # head move
        if direction == 1:
            snake[0][0] -= speed
        elif direction == 2:
            snake[0][0] += speed
        elif direction == 3:
            snake[0][1] -= speed
        elif direction == 4:
            snake[0][1] += speed
        # tail follow head
        f = True
        last = None
        for idx, i in enumerate(snake):
            if idx == 0:
                last = i
            else:
                if f:
                    if direction == 1:
                        snake[idx] = [last[0] + speed, last[1]]
                    if direction == 2:
                        snake[idx] = [last[0] - speed, last[1]]
                    if direction == 3:
                        snake[idx] = [last[0], last[1] + speed]
                    if direction == 4:
                        snake[idx] = [last[0], last[1] - speed]
                else:
                    if not snake[idx] == last:
                        snake[idx] = last
                f = False
                last = i
        head = snake[0]
        # eat apple
        if head == apple_pos:
            while True:
                ax = random.choice(xthresh)
                ay = random.choice(ythresh)
                new_pos = [ax, ay]
                in_snake = False
                for test in snake:
                    if test == new_pos:
                        in_snake = True
                        break
                if not in_snake:
                    break
            apple_pos = new_pos
            tail_end = snake[-1]
            snake.append(tail_end)
            score += 5
        # run into self
        for idx, i in enumerate(snake):
            if not idx == 0:
                if head == i:
                    playing = False
                    break
        # run out of screen
        if head[0] < 0 or head[0] + snk_size > X or head[1] < 0 or head[1] + snk_size > Y:
            playing = False

        screen.fill(background)

        score_font = font1.render(str(score), False, red)
        drawgrid()
        drawsnake(snake)
        screen.blit(score_font, [3, 2])

        pygame.display.update()
        Clock.tick(8)
    pygame.time.wait(200)
    score_font = font2.render(str(score), False, red)
    screen.fill(background)
    screen.blit(score_font, [350, 200])
    pygame.display.update()
    pygame.time.wait(800)
