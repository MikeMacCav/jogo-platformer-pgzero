WIDTH = 800
HEIGHT = 450

TITLE = "Platformer - Teste Tutor"

# =====================
# Classe do Herói
# =====================
class Hero:
    def __init__(self):
        self.actor = Actor("hero_idle_0", (100, 100))
        self.speed = 4

        # Gravidade
        self.vel_y = 0
        self.gravity = 0.5
        self.on_ground = False

    def move(self):
        # Movimento horizontal
        if keyboard.left or keyboard.a:
            self.actor.x -= self.speed

        if keyboard.right or keyboard.d:
            self.actor.x += self.speed

        # Gravidade
        self.vel_y += self.gravity
        self.actor.y += self.vel_y

        # Chão
        if self.actor.bottom >= HEIGHT:
            self.actor.bottom = HEIGHT
            self.vel_y = 0
            self.on_ground = True
        else:
            self.on_ground = False

        # Limites laterais
        if self.actor.left < 0:
            self.actor.left = 0

        if self.actor.right > WIDTH:
            self.actor.right = WIDTH

    def draw(self):
        self.actor.draw()


# =====================
# Instância do herói
# =====================
hero = Hero()


# =====================
# Funções do PgZero
# =====================
def update():
    hero.move()


def draw():
    screen.clear()
    hero.draw()