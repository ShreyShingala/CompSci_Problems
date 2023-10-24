import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window and background
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 800
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Flappy Bird")
background = pygame.image.load("background.png")

# Create a bird object with a starting position and velocity
class Bird:
    def __init__(self):
        self.x = 100
        self.y = 300
        self.velocity = 0
        self.gravity = 0.5
        self.lift = -10
        self.image = pygame.image.load("bird.png")
    
    def show(self):
        window.blit(self.image, (self.x, self.y))
    
    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity
        
        if self.y < 0:
            self.y = 0
            self.velocity = 0
        
        if self.y > WINDOW_HEIGHT - 50:
            self.y = WINDOW_HEIGHT - 50
            self.velocity = 0
    
    def up(self):
        self.velocity += self.lift

bird = Bird()

# Create a list of pipe objects with random heights and positions
class Pipe:
    def __init__(self):
        self.x = WINDOW_WIDTH
        self.width = 50
        self.top_height = random.randint(100, 400)
        self.bottom_height = WINDOW_HEIGHT - self.top_height - 200
        self.speed = 5
        self.color = (0, 255, 0)
    
    def show(self):
        pygame.draw.rect(window, self.color, (self.x, 0, self.width, self.top_height))
        pygame.draw.rect(window, self.color, (self.x, WINDOW_HEIGHT - self.bottom_height, self.width, self.bottom_height))
    
    def update(self):
        self.x -= self.speed

pipes = [Pipe()]

# Create a game loop that updates the bird's position and checks for collisions with pipes
score = 0
font = pygame.font.Font(None, 50)
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.up()
    
    window.blit(background, (0, 0))
    
    for pipe in pipes:
        pipe.show()
        pipe.update()
        
        if pipe.x < -pipe.width:
            pipes.remove(pipe)
            pipes.append(Pipe())
        
        if pipe.x < bird.x + 50 < pipe.x + pipe.width:
            if bird.y < pipe.top_height or bird.y + 50 > WINDOW_HEIGHT - pipe.bottom_height:
                game_over = True
    
    bird.show()
    bird.update()
    
    for pipe in pipes:
        if pipe.x == bird.x:
            score += 1
    
    score_text = font.render(str(score), True, (255, 255, 255))
    window.blit(score_text, (WINDOW_WIDTH // 2 - 25, 50))
    
    if game_over:
        game_over_text = font.render("Game Over", True, (255, 255, 255))
        window.blit(game_over_text, (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2 - 25))
    
    pygame.display.update()

# Quit Pygame
pygame.quit()
