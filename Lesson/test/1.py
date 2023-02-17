import pygame

# initialize pygame
pygame.init()

# set up the window
window = pygame.display.set_mode((800,600))
pygame.display.set_caption('Arkanoid')

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# set up game variables
ball_x = 400
ball_y = 300
ball_radius = 10

velocity_x = 1
velocity_y = 1



paddle_x = 350
paddle_y = 570
paddle_width = 100
paddle_height = 10

running = True

# keep score
score = 0

blocks = []
for y in range(100, 250, 50):
    for x in range(100, 600, 100):
        blocks.append((x, y))

# game loop
while running:
    
    # get all user events
    for event in pygame.event.get():
        # quit if the user closed the window
        if event.type == pygame.QUIT:
            running = False

    # add velocity to current positions
    ball_x += velocity_x
    ball_y += velocity_y

    # check for wall collision
    if ball_x + ball_radius > 800 or ball_x - ball_radius < 0:
        velocity_x *= -1
    if ball_y + ball_radius > 600 or ball_y - ball_radius < 0:
        velocity_y *= -1

    for block in blocks:
        if ball_x + ball_radius > block[0] and ball_x - ball_radius < block[0] + 50 and ball_y + ball_radius > block[1] and ball_y - ball_radius < block[1] + 25:
            # remove block
            blocks.remove(block)
            # reverse velocity
            velocity_y *= -1
            # add to score
            score += 1

    # check for paddle collision
    if ball_y + ball_radius > paddle_y and ball_x > paddle_x and ball_x < paddle_x + paddle_width:
        velocity_y *= -1

    # draw background
    window.fill(BLACK)

    for block in blocks:
        pygame.draw.rect(window, WHITE, (block[0], block[1], 50, 25))

    # draw the ball
    pygame.draw.circle(window, BLUE, (ball_x, ball_y), ball_radius)

    # draw the paddle
    pygame.draw.rect(window, WHITE, (paddle_x, paddle_y, paddle_width, paddle_height))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= 1
    if keys[pygame.K_RIGHT] and paddle_x < 700:
        paddle_x += 1

    # display score
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Score: ' + str(score), True, WHITE)
    window.blit(text, (25, 25))

    # game over if ball touches bottom
    if ball_y + ball_radius > 600:
        running = False
        font = pygame.font.Font('freesansbold.ttf', 64)
        text = font.render('Game Over', True, WHITE)
        window.blit(text, (200, 300))
        # add restart button
    button_x = 250
    button_y = 400
    button_width = 300
    button_height = 50
    pygame.draw.rect(window, WHITE, (button_x, button_y, button_width, button_height))


     # check for mouse click
    mouse_pos = pygame.mouse.get_pos()
    if mouse_pos[0] > button_x and mouse_pos[0] < button_x + button_width and mouse_pos[1] > button_y and mouse_pos[1] < button_y + button_height:
        if event.type == pygame.MOUSEBUTTONDOWN:
            # reset game variables
            ball_x = 400
            ball_y = 300
            ball_radius = 10
            velocity_x = 2
            velocity_y = 2
            paddle_x = 350
            paddle_y = 570
            paddle_width = 100
            paddle_height = 10
            running = True
            blocks = []
            for y in range(100, 200, 50):
                for x in range(100, 600, 100):
                    blocks.append((x, y))
            score = 0

    # update the window
    pygame.display.update()

# quit pygame
pygame.quit()