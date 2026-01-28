WIDTH = 800
HEIGHT = 450

TITLE = "Platformer - Teste Tutor"

# =====================
# Classe do Herói
# =====================
class Hero:
    def __init__(self):
        self.actor = Actor("hero_idle_0", (100, 350))

        self.speed = 4

        # Gravidade
        self.vy = 0
        self.gravity = 0.6
        self.jump_force = -12

        self.on_ground = False

    def move(self):
        # Movimento horizontal
        if keyboard.left or keyboard.a:
            self.actor.x -= self.speed

        if keyboard.right or keyboard.d:
            self.actor.x += self.speed

        # PULO
        if (keyboard.space or keyboard.w or keyboard.up) and self.on_ground:
            self.vy = self.jump_force
            self.on_ground = False

        # Gravidade
        self.vy += self.gravity
        self.actor.y += self.vy

        # CHÃO
        if self.actor.y >= 350:
            self.actor.y = 350
            self.vy = 0
            self.on_ground = True

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