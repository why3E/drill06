from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

def handle_events():
    global running
    global x_arr,y_arr

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if(len(x_arr) == 1):
                global i
                i =0
            x_arr.append(event.x)
            y_arr.append(TUK_HEIGHT - 1 - event.y)
            
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def draw_line(x_arr,y_arr,i):
    global frame,see

    frame = frame % 8
    x = x_arr[0]
    y = y_arr[0]

    if(len(x_arr)>1):
        t = i / 100
        x = (1-t)*x_arr[0] + t*x_arr[1]
        y = (1-t)*y_arr[0] + t*y_arr[1]
        
        if(x_arr[0] <=x_arr[1]):
            see = 1
        else:
            see = 0

    clear_canvas()
        
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        
    for k in range(1,len(x_arr),1):
        hand.clip_draw(0 , 0 , 50 , 50 , x_arr[k], y_arr[k])
        
    if(see==1):
        character.clip_draw(frame * 100 , 100 , 100 , 100, x , y)
    else:
        character.clip_draw(frame * 100 , 0 , 100 , 100, x , y)

    update_canvas()
    frame +=1
    delay(0.1)


running = True

frame,i =0,0

x_arr = [600]
y_arr = [500]
see = 0

while running:
        
    handle_events()
    clear_canvas()

    i+=4
    draw_line(x_arr,y_arr,i)

    if(len(x_arr)>1 and i == 100):
        del x_arr[0]
        del y_arr[0]

    i=i%100

close_canvas()