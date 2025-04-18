import pygame
import sys

# --- Pet class ---
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(self.hunger - 3, 0)
        self.happiness = min(self.happiness + 1, 10)

    def sleep(self):
        self.energy = min(self.energy + 5, 10)

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(self.happiness + 2, 10)
            self.hunger = min(self.hunger + 1, 10)

    def train(self, trick="Sit"):
        self.tricks.append(trick)
        self.happiness = min(self.happiness + 1, 10)

    def get_status(self):
        return f"Hunger: {self.hunger} | Energy: {self.energy} | Happiness: {self.happiness}"

    def show_tricks(self):
        return ", ".join(self.tricks) if self.tricks else "No tricks yet."


# --- Setup Pygame ---
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐶 Digital Pet")

font = pygame.font.SysFont(None, 28)
big_font = pygame.font.SysFont(None, 40)

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

pet = Pet("Buddy")

# Button class
class Button:
    def __init__(self, x, y, w, h, text, action):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.action = action

    def draw(self, surface):
        pygame.draw.rect(surface, GRAY, self.rect)
        txt_surf = font.render(self.text, True, BLACK)
        txt_rect = txt_surf.get_rect(center=self.rect.center)
        surface.blit(txt_surf, txt_rect)

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            self.action()


# Create buttons
buttons = [
    Button(50, 250, 100, 40, "Eat", pet.eat),
    Button(160, 250, 100, 40, "Sleep", pet.sleep),
    Button(270, 250, 100, 40, "Play", pet.play),
    Button(380, 250, 100, 40, "Train", pet.train),
]

clock = pygame.time.Clock()

# --- Main loop ---
while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for b in buttons:
                b.check_click(event.pos)

    # Draw pet status
    title = big_font.render(f"{pet.name}'s World", True, BLACK)
    status = font.render(pet.get_status(), True, BLACK)
    tricks = font.render("Tricks: " + pet.show_tricks(), True, BLACK)

    screen.blit(title, (WIDTH//2 - title.get_width()//2, 40))
    screen.blit(status, (50, 120))
    screen.blit(tricks, (50, 160))

    for b in buttons:
        b.draw(screen)

    pygame.display.flip()
    clock.tick(30)
