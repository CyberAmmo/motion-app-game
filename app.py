import pygame
import math

WIDTH = 1200
HEIGHT = 500

BG_COLOR = (104, 104, 104)
BALL_COLOR = (25, 115, 25)
LINE_COLOR = (250, 250, 250)

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Motion app')

class Ball:
    def __init__(self, x, y, r, color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color

    def draw(self, win):
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), self.r)
        pygame.draw.circle(win, self.color, (self.x, self.y), self.r-1)

    @staticmethod
    def path(start_X, start_y, power, angle, time):
        velocity_X = math.cos(angle) * power
        velocity_Y = math.sin(angle) * power

        distance_X = velocity_X * time
        distance_Y = (velocity_Y * time) + ((-4.9 * (time) ** 2) / 2)

        new_X = round(distance_X + start_X)
        new_Y = round(start_y - distance_Y)

        return new_X, new_Y


def redraw_window():
    win.fill(BG_COLOR)
    ball.draw(win)
    pygame.draw.line(win, LINE_COLOR, line[0], line[1])
    pygame.display.update()


def find_angle(pos):
    x = ball.x
    y = ball.y

    mouse_x, mouse_y = pos

    try:
        angle = math.atan((y - mouse_y) / (x - mouse_x))
    except:
        angle = math.pi / 2

    if mouse_y < y and mouse_x > x:
        angle = abs(angle)
    elif mouse_y < y and mouse_x < x:
        angle = math.pi - angle
    elif mouse_y > y and mouse_x < x:
        angle = math.pi + abs(angle)
    elif mouse_y > y and mouse_x > x:
        angle = (math.pi * 2) - angle 

    return angle

run = True
x = 0
y = 0
time = 0
power = 0
angle = 0
shoot = False
clock = pygame.time.Clock()
ball = Ball(300, 494, 5, BALL_COLOR)

while run:
    clock.tick(200)
    if shoot:
        if ball.y < 500 - ball.r:
            time += .05
            new_ball_pos = Ball.path(x, y, power, angle, time)
            ball.x = new_ball_pos[0]
            ball.y = new_ball_pos[1]
        else:
            shoot = False
            time = 0
            ball.y = 494


    line = [(ball.x, ball.y), pygame.mouse.get_pos()]
    redraw_window()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        
        if e.type == pygame.MOUSEBUTTONDOWN:
            if shoot:
                continue

            shoot = True
            x = ball.x
            y = ball.y
            pos = pygame.mouse.get_pos()
            time = 0
            power = math.sqrt((line[1][1] - line[0][1]) ** 2 + (line[1][0] - line[0][0]) ** 2) / 8
            angle = find_angle(pos)


pygame.quit()