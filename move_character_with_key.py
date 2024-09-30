from pico2d import *

open_canvas()
bg = load_image('TUK_GROUND.png')
character = load_image('enemy.bmp')


def handle_events():
    global running, dir, dir2
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_UP:
                dir2 += 1
            elif event.key == SDLK_DOWN:
                dir2 -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
            if event.key == SDLK_UP:
                dir2 -= 1
            if event.key == SDLK_DOWN:
                dir2 += 1
    pass


running = True
x = 800 // 2
y = 600 // 2
frame = 0
dir = 0
dir2 = 0

while running:
    clear_canvas()
    bg.draw(400, 100)

    # 좌하단 (스프라이트 1)
    if dir == -1 or dir2 == -1:
        character.clip_draw(frame * 45, 46, 33, 30, x, y)
    # 우상단 (스프라이트 2)
    else:
        character.clip_draw(frame * 45, 0, 50, 30, x, y)

    update_canvas()
    handle_events()

    if dir == -1 or dir2 == -1:
        frame = (frame + 1) % 8
    else:
        frame = (frame + 1) % 7

    # x, y 좌표를 업데이트하기 전에 화면 경계 확인
    x += dir * 10
    y += dir2 * 10

    # 화면 경계 체크 (화면 크기: 800x600)
    if x < 0:
        x = 0
    elif x > 800:
        x = 800

    if y < 0:
        y = 0
    elif y > 600:
        y = 600

    delay(0.05)

close_canvas()
