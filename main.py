from tkinter import Tk
from TinUI import *
from themelight import TinUILight



def load_ui():
    title.add_image((0,0),width=title.winfo_width(),height=title.winfo_height()
                ,imgfile='back.png')
    title.add_title((0,0),'     天 阁 \nTinga World',fg='white',size=0)
    title.add_pivot((900,0),content=(('首页',''),('正传',''),('外传',''),('外史','')),
                    fg='#a6a6a6',activefg='#ffffff')
    title.add_button2((1120,3),text='关于',font='微软雅黑 14',fg='white',activefg='#FFDB65',bg='',activebg='',line='',activeline='')


r=Tk()
r.title('Tinga World')
r.geometry('1175x770+5+5')

title=BasicTinUI(r,height=250)
title.pack(fill='x')


ui=BasicTinUI(r)
ui.pack(fill='both',expand=True)


r.after(500,load_ui)
r.resizable(False,False)
r.mainloop()
