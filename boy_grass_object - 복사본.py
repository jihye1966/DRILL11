from pico2d import *
import random


class Grass:
    def __init__(self):
        self.image = load_image('grass - 복사본.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x = random.randint(100, 700)
        self.y = 90
        self.image = load_image('run_animation - 복사본.png')
        self.frame = random.randint(0, 7)

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

        if self.x > 800:
            self.x = 0

    def draw(self):
        self.image.clip_draw(
            self.frame * 100, 0, 100, 100,
            self.x, self.y
        )


class Zombie:
    def __init__(self):
        self.x, self.y = 100, 170
        self.frame = 0
        self.image = load_image('zombie_run_animation - 복사본.png')

    def update(self):
        self.frame = (self.frame + 1) % 10
        self.x += 5

        if self.x > 800:
            self.x = 0

    def draw(self):
        frame_width = self.image.w // 10
        frame_height = self.image.h

        self.image.clip_draw(
            self.frame * frame_width, 0,
            frame_width, frame_height,
            self.x, self.y,
            frame_width // 2, frame_height // 2
        )

class SmallBall:
    def __init__(self):
        self.x = random.randint(0,800)
        self.y = 21
        self.image = load_image('ball21x21 - 복사본.png')
        self.speed = random.randint(1,10)
    
    def update(self):
        self.y += self.speed
    
        if self.y >= 578:
            self.speed = -self.speed
        elif self.y <= 500:
            self.speed = -self.speed
    
    def draw(self):
        self.image.draw(self.x, self.y)

class BigBall:
    def __init__(self):
        self.x = random.randint(0,800)
        self.y = 41
        self.image = load_image('ball41x41 - 복사본.png')
        self.speed = random.randint(1,10)

    
    def update(self):
        self.y += self.speed

        if self.y >= 558:
            self.speed = -self.speed
        elif self.y <= 500:
            self.speed = -self.speed
    
    def draw(self):
        self.image.draw(self.x, self.y)


def reset_world():
    global running, world

    running = True
    world = []

    grass = Grass()
    world.append(grass)

    team = [Boy() for _ in range(11)]
    world += team

    zombie = Zombie()
    world.append(zombie)

    smallBallsCount = random.randint(1,20)
    bigBallsCount = 20 - smallBallsCount

    smallBalls = [SmallBall() for _ in range(smallBallsCount)]
    world += smallBalls

    bigBalls = [BigBall() for _ in range(bigBallsCount)]
    world += bigBalls


def update_world():
    for o in world:
        o.update()


def render_world():
    clear_canvas()

    for o in world:
        o.draw()

    update_canvas()


def handle_events():
    global running

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas()

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()