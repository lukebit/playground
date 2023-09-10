from cmu_graphics import *


app.background = 'black'
timer = Label(0, 200, 40, size=25, fill='white')
counter3 = 0
t_counter = 0
boss_scene = False

player = Circle(200, 200, 17, fill='red')
carrots = Group()
carrots.counter = 0
rockets = Group()
rockets.counter = 0


saws = []

is_game_over = False
saw_max_radius = 30

mino_speed = 3

mino = Circle(320, 200, 10, fill='gray', visible = False)
mino.speedX = mino_speed
mino.speedY = mino_speed


def spawn_carrot(trigger_count):
    carrots.counter += 1
    if carrots.counter == trigger_count:
        carrots.add(Circle(player.centerX, 20, 17, fill='grey'))
        carrots.counter = 0


def spawn_rocket(trigger_count):
    rockets.counter += 1
    if rockets.counter == trigger_count:
        rockets.add(Circle(400, player.centerY, 25, fill='white'))
        rockets.counter = 0


def onMouseMove(mouseX, mouseY):
    player.centerX = mouseX
    player.centerY = mouseY
    

def onStep():
    global counter3, is_game_over, t_counter, boss_scene
    counter3 += 1
    t_counter += 1
    
    if is_game_over:
        return

    level = int(t_counter / 30)
    timer.value = level

    if level >= 25:
        boss_scene = True
    
    if boss_scene:    
        if not mino.visible:
            mino.centerX = 360
            mino.centerY = 360
            mino.visible = True
    
    if mino.centerX >= player.centerX:
        mino.speedX = -mino_speed
    else:
        mino.speedX = mino_speed
    mino.centerX += mino.speedX
    
    if mino.centerY >= player.centerY:
        mino.speedY = -mino_speed
    else:
        mino.speedY = mino_speed
    mino.centerY += mino.speedY
    
    if not boss_scene:
        spawn_carrot(25)
        spawn_rocket(60)
    
    carrots.centerY += 3
    rockets.centerX -= 4

    for s in saws:
        if s.radius < saw_max_radius:
            s.radius += 0.5

    if counter3 == 150:
        if len(saws) >= 2:
            s = saws.pop(0)
            s.visible = False
        saws.append(Circle(player.centerX, player.centerY, 5, fill='orangeRed'))
        counter3 = 0
    
    if player.hitsShape(carrots) or player.hitsShape(rockets) or (mino.visible and player.hitsShape(mino)):
        is_game_over = True
        Label('game over', 200, 200, size=40, fill='gray', opacity=70)
    
    for s in saws:
        if s.visible and s.radius == saw_max_radius and player.hitsShape(s):
            is_game_over = True
            Label('game over', 200, 200, size=40, fill='gray', opacity=70)
    
    for c in carrots:
        if c.centerY > 410:
            carrots.remove(c)


cmu_graphics.run()
