#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import tkinter
import numpy as np
import random
import tkinter as tk
from PIL import Image, ImageTk
import pygame
import pkg_resources
empty=0
white=1
black=-1
BLACK=0
WHITE=0
board_size=8
wall=2
left=1
right=1
under=1
above=1
above_right=1
above_left=1
under_left=1
under_right=1
turn=0
MAX_turn=60
MY_turn=black
count=0
image_path1 = pkg_resources.resource_filename(__name__, 'PLAYボタン.png')
image_path2 = pkg_resources.resource_filename(__name__, 'EXITボタン.png')
image_path3 = pkg_resources.resource_filename(__name__, 'OPTIONボタン.png')
image_path4 = pkg_resources.resource_filename(__name__, 'othello_tail.png')
image_path5 = pkg_resources.resource_filename(__name__, 'othello_black.png')
image_path6 = pkg_resources.resource_filename(__name__, 'othello_white.png')
image_path7 = pkg_resources.resource_filename(__name__, 'othello_wall.png')
image_path8 = pkg_resources.resource_filename(__name__, 'haikei_renga.png')
image_path9 = pkg_resources.resource_filename(__name__, 'othello_icon.ico')
image_path10 = pkg_resources.resource_filename(__name__, '決定ボタンを押す7.mp3')
image_path11 = pkg_resources.resource_filename(__name__, 'spo_ge_osero02.mp3')
image_path12 = pkg_resources.resource_filename(__name__, '決定ボタンを押す35.mp3')
image_path13 = pkg_resources.resource_filename(__name__, '歓声と拍手.mp3')
image_path14 = pkg_resources.resource_filename(__name__, 'ビープ音4.mp3')
image_path15= pkg_resources.resource_filename(__name__, 'othello_tail1.png')
class Board():
    def __init__(self):
        
        #self.Board1=[[0]*10 for _ in range(10)]
        self.Board1=np.zeros((board_size+2,board_size+2),dtype=int)
        self.color_selection=wall
        self.button_list=[]
        self.button_images = []
        self.button_grid = []
        self.image_row = []
        self.button_row = []
        self.pt=0
        self.sqr=0
        self.CPU_current=0
        for x in range(10):
            for y in range(10):
                if x==0 or x==board_size+1:
                    self.Board1[x][y]=wall
                if y==0 or y==board_size+1:
                    self.Board1[x][y]=wall
                
        self.Board1[4][5]=black
        self.Board1[4][4]=white
        self.Board1[5][4]=black
        self.Board1[5][5]=white
        self.current=black
    def direction(self,x1,y1,color):
        dir=[0]*8
        no=0
        count=0
        if (self.Board1[x1][y1]!=empty):            
            return no
        if self.Board1[x1][y1-1]==-color:
            x_tmp=x1
            y_tmp=y1-2
            while self.Board1[x_tmp][y_tmp]==-color:               
                y_tmp-=1
            if self.Board1[x_tmp][y_tmp]==color:
                dir[0]=left
        if self.Board1[x1][y1+1]==-color:
            x_tmp=x1
            y_tmp=y1+2
            while self.Board1[x_tmp][y_tmp]==-color:
                y_tmp+=1                
            if self.Board1[x_tmp][y_tmp]==color:
                    dir[1]=right
        if self.Board1[x1+1][y1]==-color:
            x_tmp=x1+2
            y_tmp=y1
            while self.Board1[x_tmp][y_tmp]==-color:               
                x_tmp+=1
            if self.Board1[x_tmp][y_tmp]==color:
                    dir[2]=under
        if self.Board1[x1-1][y1]==-color:
            x_tmp=x1-2
            y_tmp=y1
            while self.Board1[x_tmp][y_tmp]==-color:
                x_tmp-=1  
                
            if self.Board1[x_tmp][y_tmp]==color:
                    dir[3]=above        
        if self.Board1[x1-1][y1+1]==-color:
            x_tmp=x1-2
            y_tmp=y1+2
            while self.Board1[x_tmp][y_tmp]==-color:
                x_tmp-=1
                y_tmp+=1
            if self.Board1[x_tmp][y_tmp]==color:
                    dir[4]=above_right
        if self.Board1[x1-1][y1-1]==-color:
            x_tmp=x1-2
            y_tmp=y1-2
            while self.Board1[x_tmp][y_tmp]==-color:
                x_tmp-=1
                y_tmp-=1                
            if self.Board1[x_tmp][y_tmp]==color:
                    dir[5]=above_left
        if self.Board1[x1+1][y1-1]==-color:
            x_tmp=x1+2
            y_tmp=y1-2
            while self.Board1[x_tmp][y_tmp]==-color:
                x_tmp+=1
                y_tmp-=1
            if self.Board1[x_tmp][y_tmp]==color:
                    dir[6]=under_left
        if self.Board1[x1+1][y1+1]==-color:
            x_tmp=x1+2
            y_tmp=y1+2
            while self.Board1[x_tmp][y_tmp]==-color:
                x_tmp+=1
                y_tmp+=1  
            if self.Board1[x_tmp][y_tmp]==color:
                    dir[7]=under_right
        for i in range(8):
            if dir[i]==0:
                count+=1
        if count==8:
            return no
        else:           
            return dir
    
    def frip(self,x2,y2):
        if type((self.direction(x2,y2,self.current)))==int:
            return 0
        else:
            list=self.direction(x2,y2,self.current)
            self.Board1[x2][y2]=self.current
            x=np.zeros((8),dtype=int)
            for i in range(8):
                x[i]=list[i]
                if x[0]==1:
                    x_tmp=x2
                    y_tmp=y2-1
                    while self.Board1[x_tmp][y_tmp]==-self.current:
                        self.Board1[x_tmp][y_tmp]=self.current
                        y_tmp-=1
                if x[1]==1:
                    x_tmp=x2
                    y_tmp=y2+1
                    while self.Board1[x_tmp][y_tmp]==-self.current:
                        self.Board1[x_tmp][y_tmp]=self.current
                        y_tmp+=1
                if x[2]==1:
                    x_tmp=x2+1
                    y_tmp=y2
                    while self.Board1[x_tmp][y_tmp]==-self.current:
                        self.Board1[x_tmp][y_tmp]=self.current
                        x_tmp+=1
                if x[3]==1:
                    x_tmp=x2-1
                    y_tmp=y2
                    while self.Board1[x_tmp][y_tmp]==-self.current:
                        self.Board1[x_tmp][y_tmp]=self.current
                        x_tmp-=1
                if x[4]==1:
                    x_tmp=x2-1
                    y_tmp=y2+1
                    while self.Board1[x_tmp][y_tmp]==-self.current:
                        self.Board1[x_tmp][y_tmp]=self.current
                        x_tmp-=1
                        y_tmp+=1
                if x[5]==1:
                    x_tmp=x2-1
                    y_tmp=y2-1
                    while self.Board1[x_tmp][y_tmp]==-self.current:
                        self.Board1[x_tmp][y_tmp]=self.current
                        x_tmp-=1
                        y_tmp-=1
                if x[6]==1:
                    x_tmp=x2+1
                    y_tmp=y2-1
                    while self.Board1[x_tmp][y_tmp]==-self.current:
                        self.Board1[x_tmp][y_tmp]=self.current
                        x_tmp+=1
                        y_tmp-=1
                if x[7]==1:
                    x_tmp=x2+1
                    y_tmp=y2+1
                    while self.Board1[x_tmp][y_tmp]==-self.current:
                        self.Board1[x_tmp][y_tmp]=self.current
                        x_tmp+=1
                        y_tmp+=1
    
    def create_button(self,image_path,row,column):
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        if self.pt==0:
            if self.sqr==0 or self.sqr==2:
                button = tk.Button(frame, image=photo,command=lambda r=row,c=column: self.button_click(r,c,self.color_selection))
            else:
                button = tk.Button(frame, image=photo,command=lambda r=row,c=column: opt)
        else:
            button = tk.Button(frame, image=photo,command=lambda r=row,c=column: self.button_click1(r,c,self.color_selection))
        button.photo=photo
        return button
    def button_click(self,row,column,color1):
        self.Board1[row][column]=color1
        play_sound2()
        main1()
    def button_click1(self,row,column,color1):
        deleate_label()
        if self.pt==1:
            
            if self.move(row,column)==True:
                self.frip(row,column)
                self.current=-self.current
                play_sound1()
                main()
            else:
                play_sound4()
                main()
        else:
            if self.move(row,column)==True:
                self.frip(row,column)
                self.current=-self.current
                play_sound1()
                CPU_game()
            else:
                play_sound4()
                CPU_game()
    def button_click_white(self):
        self.color_selection=white
    def button_click_black(self):
        self.color_selection=black
    def button_click_tile(self):
        self.color_selection=0
    def button_click_wall(self):
        self.color_selection=wall
    def display(self):
        for x in range(1,9):
            for y in range(1,9):
                if self.Board1[x][y]==2:
                    image_path = image_path7
                    button = self.create_button(image_path,x,y)
                    button.grid(row=x,column=y)
                if self.Board1[x][y]==0:
                    image_path = image_path4
                    button = self.create_button(image_path,x,y)
                    button.grid(row=x,column=y)
                if self.Board1[x][y]==1:
                    image_path = image_path6
                    button = self.create_button(image_path,x,y)
                    button.grid(row=x, column=y)
                if self.Board1[x][y]==-1:
                    image_path = image_path5
                    button = self.create_button(image_path,x,y)
                    button.grid(row=x, column=y)
    def display1(self):
        for x in range(1,9):
            for y in range(1,9):
                if type(self.direction(x,y,self.current))!=int:
                    image_path = image_path15
                    button = self.create_button(image_path,x,y)
                    button.grid(row=x,column=y)
                else:
                    
                    if self.Board1[x][y]==2:
                        image_path = image_path7
                        button = self.create_button(image_path,x,y)
                        button.grid(row=x,column=y)
                    if self.Board1[x][y]==0:
                        image_path = image_path4
                        button = self.create_button(image_path,x,y)
                        button.grid(row=x,column=y)
                    if self.Board1[x][y]==1:
                        image_path = image_path6
                        button = self.create_button(image_path,x,y)
                        button.grid(row=x, column=y)
                    if self.Board1[x][y]==-1:
                        image_path = image_path5
                        button = self.create_button(image_path,x,y)
                        button.grid(row=x, column=y)
    def move(self,x3,y3):
        
        if type((self.direction(x3,y3,self.current)))==int:
            return False
        else:
            return True
        
    def skip(self):
        count=0
        for x in range(1,9):
            for y in range(1,9):
                if type(self.direction(x,y,self.current))==int:
                    count+=1
        if count==64:
            return True
        else:
            return False
    def hantei(self):
        count=0
        count1=0
        for x in range(1,9):
            for y in range(1,9):
                if type(self.direction(x,y,self.current))==int:
                    count+=1
        for x in range(1,9):
            for y in range(1,9):
                if type(self.direction(x,y,-self.current))==int:
                    count1+=1
        
        if count==count1&count==64:
            return True
        else:
            return False
        
    def isgameover(self):
        if (self.hantei()==True) or (turn>=MAX_turn):
            return True
        else:
            return False
    def randomAI(self):
        list1=np.zeros((64),dtype=int)
        i=0
        for x in range(1,9):
            for y in range(1,9):
                if type(self.direction(x,y,self.current))!=int:
                    z=10*x+y 
                    list1[i]=z
                    i+=1                   
        list2=list1[np.nonzero(list1)]
        a=random.choice(list2)
        return a
board=Board()
def main1_1():
    play_sound()
    main1()
def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load(image_path10)  # ここに使用する音声ファイルのパスを指定してください
    pygame.mixer.music.play()
def play_sound1():
    pygame.mixer.init()
    pygame.mixer.music.load(image_path11)  # ここに使用する音声ファイルのパスを指定してください
    pygame.mixer.music.play()
def play_sound2():
    pygame.mixer.init()
    pygame.mixer.music.load(image_path12)  # ここに使用する音声ファイルのパスを指定してください
    pygame.mixer.music.play()
def play_sound3():
    pygame.mixer.init()
    pygame.mixer.music.load(image_path13)  # ここに使用する音声ファイルのパスを指定してください
    pygame.mixer.music.play()
def play_sound4():
    pygame.mixer.init()
    pygame.mixer.music.load(image_path14)  # ここに使用する音声ファイルのパスを指定してください
    pygame.mixer.music.play()

def deleate_label():    
    label.pack_forget()
def deleate_label1():   
    label1.pack_forget()
def deleate_optin():    
     option_button1.pack_forget()
def CPU_game_1():
    vshuman.pack()
    play_sound()
    CPU_game()
def deleate_labelHUMAN():    
    label.pack_forget()
    vshuman.pack_forget()
    vscpu.pack()
    play_sound()
    main()
def main_1():
    option_button.pack_forget()
    exist_button.pack_forget()
    Button.pack_forget()
    board.display1()
    option_button.pack(side="right")
    exist_button.pack(side="left")
    vscpu.pack()
    play_sound()
    main()
def gameover_1():
    if board.pt==3:
        vshuman.pack_forget()
    elif  board.pt==1:
        vscpu.pack_forget()
    play_sound3()
    gameover()
def main1():
    if board.sqr==2:
        deleate_optin()
    if board.pt==3:
        deleate_label()
        vshuman.pack_forget()
    elif  board.pt==1:
        deleate_label()
        vscpu.pack_forget()
        
    board.sqr=0
    board.pt=0
    for widget in frame.winfo_children():
            widget.destroy()
    wall_button.pack(side="left")
    tile_button.pack(side="left")
    white_button.pack(side="right")
    black_button.pack(side="right")
    Button.pack_forget()
    Button.pack()
    option_button.pack_forget()
    
    board.display()
    exist_button.pack_forget()
    
    
def main():
    global label
    global label1
    board.pt=1
    for widget in frame.winfo_children():
            widget.destroy()
    board.display1()
    wall_button.pack_forget()
    tile_button.pack_forget()
    white_button.pack_forget()
    black_button.pack_forget()
    if board.isgameover()==True:
        if board.sqr==1:
            deleate_label()
        board.sqr=1
        gameover_1()
    else:
        if board.skip()==True:
            if board.sqr==1:
                deleate_label()
            label1=tk.Label(root,text="パスです。")
            label1.pack()
            root.after(100,deleate_label1)
            board.current=-board.current
            main()
        else:
            if board.current==-1:
                label=tk.Label(root,text="現在は黒の手番")
                label.pack()
            else:
                label=tk.Label(root,text="現在は白の手番")
                label.pack()
    board.sqr=1
def CPU_game():
    global label
    global label1
    deleate_label()
    
    if board.pt==1:
        board.CPU_current=board.current
    board.pt=3
    for widget in frame.winfo_children():
            widget.destroy()
    board.display1()
    exist_button.pack_forget()
    
    vscpu.pack_forget()
    Button.pack_forget()
    option_button.pack_forget()
    option_button.pack(side="right")
    exist_button.pack(side="left")
    wall_button.pack_forget()
    tile_button.pack_forget()
    white_button.pack_forget()
    black_button.pack_forget()
    if board.isgameover()==True:
        if board.sqr==1:
            deleate_label()
        
        gameover_1()
    else:
        if board.skip()==True:
            if board.sqr==1:
                deleate_label()
            board.current=-board.current
            CPU_game()
        else:
            if board.current==board.CPU_current:
                    AI=board.randomAI()
                    syou=AI//10
                    yozyou=AI%10
                    board.frip(syou,yozyou)
                    #turn+=1
                    board.current=-board.current
                    CPU_game()
            else:
                if board.current==-1:
                    label=tk.Label(root,text="現在は黒の手番")
                    label.pack()
                else:
                    label=tk.Label(root,text="現在は白の手番")
                    label.pack()
    board.sqr=1
def opt():
    for x in range(10):
            for y in range(10):
                if x>0 and x<board_size+1:
                    board.Board1[x][y]=empty
                if y>0 and y<board_size+1:
                    board.Board1[x][y]=empty
    board.Board1[4][5]=black
    board.Board1[4][4]=white
    board.Board1[5][4]=black
    board.Board1[5][5]=white
    board.current=black
    board.sqr=2
    opt1()
def opt1():
    
    
    deleate_label()
    deleate_label1()
    play_sound()
    main1()
def gameover():
    global label
    global label1
    board.pt=0
    option_button.pack_forget()
    #exist_button.pack_forget()
    option_button1.pack(side="right")
    for widget in frame.winfo_children():
            widget.destroy()
    board.display()
    
    BLACK=0
    WHITE=0
    for x in range(1,9):
        
        for y in range(1,9):
            if board.Board1[x][y]==-1:
                BLACK+=1
            if board.Board1[x][y]==1:
                WHITE+=1
    label=tk.Label(root,text="黒石が{}、白石が{}".format(BLACK,WHITE))
    label.pack()
    if BLACK>WHITE:
        label1=tk.Label(root,text="黒の勝利です。")
        
    elif BLACK<WHITE:
        label1=tk.Label(root,text="白の勝利です。")
    else :
        label1=tk.Label(root,text="引き分けです。")
    
    
    label.pack()
    label1.pack()
root = tkinter.Tk()
root.title(u"カスタム　オセロ")


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry("1000x800")
image = Image.open(image_path1)
image = ImageTk.PhotoImage(image)
image1 = Image.open(image_path2)
image1 = ImageTk.PhotoImage(image1)
image2 =Image.open(image_path3)
image2 =ImageTk.PhotoImage(image2)
image3 =Image.open(image_path4)
image3 =ImageTk.PhotoImage(image3)
image4 =Image.open(image_path5)
image4 =ImageTk.PhotoImage(image4)
image5 =Image.open(image_path6)
image5 =ImageTk.PhotoImage(image5)
image6 =Image.open(image_path7)
image6 =ImageTk.PhotoImage(image6)
image7=Image.open(image_path8)
resized_image = image7.resize((screen_width, screen_height), Image.ANTIALIAS)
#image7=ImageTk.PhotoImage(image7)
image7=ImageTk.PhotoImage(resized_image)
renga=tk.Label(root,image=image7)


Button = tk.Button(root,image=image,command=main_1)
vscpu=tk.Button(root,text='VS CPU',command=CPU_game_1)
vscpu['bg']='white'
vscpu['fg']='black'
vscpu['width']=20
vscpu['height']=2

vshuman=tk.Button(root,text='VS HUMAN',command=deleate_labelHUMAN)
vshuman['bg']='white'
vshuman['fg']='black'
vshuman['width']=20
vshuman['height']=2
exist_button=tkinter.Button(root,image=image1,command=root.destroy)
option_button=tkinter.Button(root,image=image2,command=main1_1)
white_button=tkinter.Button(root,image=image5,command=board.button_click_white)
black_button=tkinter.Button(root,image=image4,command=board.button_click_black)
tile_button=tkinter.Button(root,image=image3,command=board.button_click_tile)
wall_button=tkinter.Button(root,image=image6,command=board.button_click_wall)

option_button1=tkinter.Button(root,image=image2,command=opt)
Button.pack(padx=100,pady=60)
option_button.pack(padx=100,pady=60)
exist_button.pack(padx=100,pady=60)
option_button.pack(padx=100,pady=60)
#renga.pack()
renga.place(relwidth=1,relheight=1)
frame=tk.Frame(root,padx=0,pady=0)
frame.pack()
root.iconbitmap(image_path9)
#print(sys.version)
root.mainloop()


# In[ ]:





# In[ ]:




