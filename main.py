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

    def move(self):
        if keyboard.left or keyboard.a:
            self.actor.x -= self.speed

        if keyboard.right or keyboard.d:
            self.actor.x += self.speed

        # Limites da tela
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
