
################################################################################
#                                 MagicJarsGame                                #
################################################################################

# A Magic Jars Game - PictureVersion
# v2.0 build 18
# 07/01/2021 20:25
# by RWP

################################################################################
#                                    IMPORTS                                   #
################################################################################

from tkinter import *
import random


################################################################################
#                                   FUNCTIONS                                  #
################################################################################

def load_images():
    # Description
    # ******************************************************
    img_dict = {
        'menu_bg': PhotoImage(file="assets/bgd/menu.png"),
        'easy_bg': PhotoImage(file="assets/bgd/easy.png"),
        'medium_bg': PhotoImage(file="assets/bgd/medium.png"),
        'hard_bg': PhotoImage(file="assets/bgd/hard.png"),
        'btn_easy': PhotoImage(file="assets/btn/easy.png"),
        'btn_easy_act': PhotoImage(file="assets/btn/easy_.png"),
        'btn_medium': PhotoImage(file="assets/btn/medium.png"),
        'btn_medium_act': PhotoImage(file="assets/btn/medium_.png"),
        'btn_hard': PhotoImage(file="assets/btn/hard.png"),
        'btn_hard_act': PhotoImage(file="assets/btn/hard_.png"),
        'btn_retry': PhotoImage(file="assets/btn/retry.png"),
        'btn_retry_act': PhotoImage(file="assets/btn/retry_.png"),
        'btn_return': PhotoImage(file="assets/btn/return.png"),
        'btn_return_act': PhotoImage(file="assets/btn/return_.png"),
        'jar': PhotoImage(file="assets/itm/jar.png"),
        'jar_act': PhotoImage(file="assets/itm/jar_.png"),
        'key': PhotoImage(file="assets/itm/key.png"),
        'snake': PhotoImage(file="assets/itm/snake.png"),
        'title': PhotoImage(file="assets/txt/title.png"),
        'difficulty': PhotoImage(file="assets/txt/difficulty.png"),
        'choose': PhotoImage(file="assets/txt/choose.png"),
        'won': PhotoImage(file="assets/win/won.png"),
        'lose': PhotoImage(file="assets/win/lose.png"),
        's1k4': PhotoImage(file="assets/win/s1k4.png"),
        's1k3': PhotoImage(file="assets/win/s1k3.png"),
        's1k2': PhotoImage(file="assets/win/s1k2.png"),
        's1k1': PhotoImage(file="assets/win/s1k1.png"),
        's2k3': PhotoImage(file="assets/win/s2k3.png"),
        's2k2': PhotoImage(file="assets/win/s2k2.png"),
        's2k1': PhotoImage(file="assets/win/s2k1.png"),
        's3k2': PhotoImage(file="assets/win/s3k2.png"),
        's3k1': PhotoImage(file="assets/win/s3k1.png")
    }

    return img_dict


################################################################################

def place_jars():
    # Description
    # ******************************************************
    x, y = (150, 485)

    for n in range(0, 5):
        dis_str = 'key' if jars[n] == 'K' else 'snake'

        canvas.create_image(x, y, image=img['jar'], activeimage=img['jar_act'], disabledimage=img[dis_str],
                            tag="jar" + str(n), state="normal")
        x += 125
        # print("Place jar" + str(n) + " (" + dis_str + ")" + jars[n])  # Debug


################################################################################

def reveal_jars():
    # Description
    # ******************************************************
    for n in range(0, 5):
        canvas.itemconfigure("jar" + str(n), state="disabled")


################################################################################

def game_init():
    # Description
    # ******************************************************
    global jars, key_count

    key_count = 5 - difficulty
    jars = ['K'] * key_count
    jars += ['S'] * difficulty
    # print("jars:", jars)  # Debug
    random.shuffle(jars)
    # print("jars:", jars)  # Debug

    bg_tpl = ('easy_bg', 'medium_bg', 'hard_bg')
    bg_str = bg_tpl[difficulty - 1]
    # print("Game Background: " + bg_str)  # Debug

    win_str = f's{difficulty}k{key_count}'
    # print("Window: " + win_str)  # Debug

    canvas.delete("all")

    canvas.create_image(400, 300, image=img[bg_str], tag="game_background", state="disabled")

    canvas.create_image(400, 180, image=img[win_str], tag="window", state="disabled")

    canvas.create_image(400, 380, image=img['choose'], tag="choose", state="disabled")

    canvas.create_image(752, 568, image=img['btn_return'], activeimage=img['btn_return_act'],
                        tag="return", state="normal")

    place_jars()


################################################################################

def show_menu():
    # Description
    # ******************************************************
    canvas.delete("all")

    canvas.create_image(400, 300, image=img['menu_bg'], tag="menu_background", state="disabled")
    canvas.create_image(400, 100, image=img['title'], tag="menu_title", state="disabled")
    canvas.create_image(400, 260, image=img['difficulty'], tag="menu_difficulty", state="disabled")

    canvas.create_image(204, 440, image=img['btn_easy'], activeimage=img['btn_easy_act'],
                        tag="menu_ch1", state="normal")
    canvas.create_image(400, 440, image=img['btn_medium'], activeimage=img['btn_medium_act'],
                        tag="menu_ch2", state="normal")
    canvas.create_image(596, 440, image=img['btn_hard'], activeimage=img['btn_hard_act'],
                        tag="menu_ch3", state="normal")


################################################################################

def game_over(state):
    # Description
    # ******************************************************
    canvas.delete("choose")
    canvas.itemconfigure("window", image=img[state])
    canvas.create_image(400, 300, image=img['btn_retry'], activeimage=img['btn_retry_act'],
                        tag="retry", state="normal")
    reveal_jars()


################################################################################

def left_click(_event):
    # Description
    # ******************************************************
    global key_count, difficulty

    curt = canvas.find_withtag("current")
    if len(curt) != 0:
        curt_id = curt[0]
        curt_tags = canvas.itemcget(curt_id, 'tags')
        # print("tags:", curt_tags)  # Debug

        if "menu_ch" in curt_tags:
            difficulty = int(curt_tags[7:8])
            # print("Difficulty:", difficulty)  # Debug
            game_init()

        elif "return" in curt_tags:
            show_menu()

        elif "retry" in curt_tags:
            game_init()

        elif "jar" in curt_tags:
            curt_num = int(curt_tags[3:4])
            # print("jar:", curt_num, "contain:", jars[curt_num])  # Debug

            if jars[curt_num] == 'K':
                key_count -= 1
                if key_count == 0:
                    game_over('won')

                else:
                    canvas.itemconfigure(curt_id, state="disabled")
                    win_str = f's{difficulty}k{key_count}'
                    # print("Window: " + win_str)  # Debug
                    canvas.itemconfigure("window", image=img[win_str])

            else:
                game_over('lose')


################################################################################
#                                    GLOBAL                                    #
################################################################################

# Game Variables
jars = []
key_count = 0
difficulty = 0
################################################################################
#                                     MAIN                                     #
################################################################################

# Create UserForm (Tkinter Window)
userform = Tk()
userform.title("Magic Jars Game")
userform.geometry("800x600")
userform.resizable(width=False, height=False)
userform.iconbitmap("assets/MagicJars2.ico")
userform.config(background='#404040')

# Create images dictionary
img = load_images()

# Create Gfx Area in UserForm
canvas = Canvas(userform, width=800, height=600, bg='#404040', bd=0, highlightthickness=0)
canvas.pack(expand=YES)

# Link with Event Left Mouse Button Release to left_click() Functions
canvas.bind("<ButtonRelease-1>", left_click)

# Display Menu
show_menu()

# Display UserForm
userform.mainloop()

################################################################################
#                                      EOF                                     #
################################################################################
