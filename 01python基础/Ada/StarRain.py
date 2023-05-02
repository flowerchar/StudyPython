import pygame as pyg
from sys import exit
import random as ran
import os

#color
# black = (48, 35, 74)
# black = (0,0,0)
black = (0,0,0)
white = (255,255,255)

#window
window_width = 800
window_height = 800

situation = []
situation_temp = []
stars_list = []

#font
text,text_2,text_3,text_4,text_5,text_6,text_7 = 0,0,0,0,0,0,0
# text_pos,text_pos_2 = 0,0
WRITE,WRITE_2,WRITE_3,WRITE_4,WRITE_5,WRITE_6,WRITE_7 = False,False,False,False,False,False,False

# ico
touxiang = pyg.image.load(r'resource\Ada.jpg')
pyg.display.set_icon(touxiang)

def moving():

    #改变situation
    for i in situation:
        i["x"] -= 2
        i["y"] += 1

def making():

    situation.append({"x":800,"y":ran.randint(0,800)})

def making_first(window):

    situation.append({"x":800,"y":ran.randint(0,800)})
    Draw(window)

def Draw(window):

    window.fill(black)

    for i in situation:

        #1.绘制普通部分
        start_x = i["x"] - 80
        start_y = i["y"] + 40
        end_x = i["x"] - 30
        end_y = i["y"] + 15

        for j in range(0,26):

            pyg.draw.line(window,white,(start_x + j*2,start_y - j*1),(start_x + j*2,start_y - j*1),1)

        #2.绘制渐变部分
        for k in range(1,16):

            location_x = end_x + 2*k
            location_y = end_y - 1*k

            pyg.draw.line(window,(255 - 12.25*k,255 - 12.25*k,255 - 12.25*k),(location_x,location_y),(location_x,location_y),1)

        #3.画星星
        making_stars(window,flag=False)

def making_stars(window,flag):

    global stars_list

    if flag == True:
        for i in range(1,ran.randint(81,201)):
            stars_list.append({"x":ran.randint(0,800),"y":ran.randint(0,800)})

    #Draw
    for i in stars_list:
        # pyg.draw.line(window,(ran.randint(0,254),ran.randint(0,254),ran.randint(0,254)),(i["x"],i["y"]),(i["x"],i["y"]),3)
        pyg.draw.circle(window,(ran.randint(0,255),ran.randint(0,255),ran.randint(0,255)),(i["x"],i["y"]),ran.randint(1,2),3)

def check_del():

    global situation_temp,situation

    situation_temp = []

    for i in situation:
        if i["x"] > 0 and i["y"] < 800:
            situation_temp.append(i)

    situation = situation_temp

def Main():

    global situation, text_pos, text, WRITE_2, text_2, text_pos_2, WRITE_3, text_3, WRITE_4, text_4, WRITE_5, text_5, WRITE_6, text_6, WRITE_7, text_7
    global WRITE
    p_flag = 0
    pyg.init()
    os.environ["SDL_VIDEO_WINDOW_POS"] = "300,50"
    window = pyg.display.set_mode((window_width, window_height))
    pyg.display.set_caption("Ada一起来看流星雨呀")

    # 字体
    font = pyg.font.Font(r'resource\simkai.ttf',30)
    # text = font.render("摩羯座流星雨鸭",1,(255,255,255))
    # text_pos = text.get_rect()
    #创建事件的计时器
    COUNT_making = pyg.USEREVENT + 1
    pyg.time.set_timer(COUNT_making,1000)

    #移动事件的计时器
    COUNT_moving = pyg.USEREVENT + 2
    pyg.time.set_timer(COUNT_moving,50)

    #先创建第一个
    making_first(window)
    making_stars(window,flag=True)
    pyg.mixer.music.load(r'resource\My Soul.mp3')
    sound = pyg.mixer.Sound(r'resource\点击音效1.mp3')
    pyg.mixer.music.play(-1,0.0)
    while True:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                pyg.quit()
                exit()
            if event.type == COUNT_making:
                making()
            if event.type == COUNT_moving:
                moving()
                Draw(window)
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_a:
                    text = font.render("To Ada:",True, (255, 255, 255))
                    WRITE = True
                    p_flag += 1
                    sound.play()
                if event.key == pyg.K_d:
                    text_2 = font.render("  我想把漫天星河揉碎", True, (255, 255, 255))
                    WRITE_2 = True
                    sound.play()
                if event.key == pyg.K_a and p_flag>1:
                    text_3 = font.render("  化作点点微光常伴你左右", True, (255, 255, 255))
                    WRITE_3 = True
                    p_flag += 1
                    sound.play()
                if event.key == pyg.K_h:
                    text_4 = font.render("  星河滚烫你是人间理想", True, (255, 255, 255))
                    WRITE_4 = True
                    sound.play()
                if event.key == pyg.K_a and p_flag>3:
                    text_5 = font.render("  夜风寒凉你是人间火光", True, (255, 255, 255))
                    WRITE_5 = True
                    sound.play()
                if event.key == pyg.K_p:
                    text_6 = font.render("  万世沉浮你是人间归途", True, (255, 255, 255))
                    WRITE_6 = True
                    sound.play()
                if event.key == pyg.K_i:
                    text_7 = font.render("我喜欢星星，更喜欢你", True, (255, 255, 255))
                    WRITE_7 = True
                    pyg.mixer.music.stop()
                    pyg.mixer.music.load(r'resource\Ada.mp3')
                    pyg.mixer.music.play(-1,0.0)
                # if event == pyg.K_c:
                #     WRITE,WRITE_2,WRITE_3,WRITE_4,WRITE_5,WRITE_6 = False,False,False,False,False,False
                #     window.fill(black)
            if event.type == pyg.MOUSEBUTTONUP:
                sound.play()

        #释放内存
        check_del()
        if WRITE == True:
            window.blit(text, (0,0))
        if WRITE_2 == True:
            window.blit(text_2,(0,40))
        if WRITE_3 == True:
            window.blit(text_3,(0,80))
        if WRITE_4 == True:
            window.blit(text_4,(0,120))
        if WRITE_5 == True:
            window.blit(text_5,(0,160))
        if WRITE_6 == True:
            window.blit(text_6,(0,200))
        if WRITE_7 == True:
            window.blit(text_7,(0,250))
        pyg.display.update()


if __name__ == "__main__":
    Main()