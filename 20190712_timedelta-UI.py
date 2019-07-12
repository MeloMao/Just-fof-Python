# -*- coding:UTF-8 -*-

from tkinter import *
import codecs
import os
import datetime
from datetime import date

LOG_LINE_NUM = 0

class M_notebook():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name


    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("日期间隔计算器")              #窗口名
        self.init_window_name.geometry('200x80')                   #窗口大小
        self.init_window_name["bg"] = "CornflowerBlue"               #窗口背景色
        #self.init_window_name.attributes("-alpha",0.5)              #界面透明化程度
        #标签
        self.start_label = Label(self.init_window_name, bg='pink', font=('Arial', 10), text="起始日期")
        self.start_label.grid(row=1, column=0)
        self.end_label = Label(self.init_window_name, bg='pink', font=('Arial', 10), text="结束日期")
        self.end_label.grid(row=5, column=0)
        self.y1_label = Label(self.init_window_name, bg='pink', font=('Arial', 10), text="年")
        self.y1_label.grid(row=1, column=6, rowspan=1, columnspan=1)
        self.m1_label = Label(self.init_window_name, bg='pink', font=('Arial', 10), text="月")
        self.m1_label.grid(row=1, column=8, rowspan=1, columnspan=1)
        self.d1_label = Label(self.init_window_name, bg='pink', font=('Arial', 10), text="日")
        self.d1_label.grid(row=1, column=10, rowspan=1, columnspan=1)
        self.y2_label = Label(self.init_window_name, bg='pink', font=('Arial', 10), text="年")
        self.y2_label.grid(row=5, column=6, rowspan=1, columnspan=1)
        self.m2_label = Label(self.init_window_name, bg='pink', font=('Arial', 10), text="月")
        self.m2_label.grid(row=5, column=8, rowspan=1, columnspan=1)
        self.d2_label = Label(self.init_window_name, bg='pink', font=('Arial', 10), text="日")
        self.d2_label.grid(row=5, column=10, rowspan=1, columnspan=1)
        self.show_label = Label(self.init_window_name, bg='pink', font=('Arial', 10), text="相距天数为")
        self.show_label.grid(row=10, column=1, rowspan=7, columnspan=7)
        #文本框
        self.start_year = Text(self.init_window_name, width=4, height=1)  #起始年
        self.start_year.grid(row=1, column=1, rowspan=1, columnspan=1)
        self.start_month = Text(self.init_window_name, width=2, height=1)  #起始月
        self.start_month.grid(row=1, column=7, rowspan=1, columnspan=1)
        self.start_day = Text(self.init_window_name, width=2, height=1)  # 起始日
        self.start_day.grid(row=1, column=9, rowspan=1, columnspan=1)
        self.end_year = Text(self.init_window_name, width=4, height=1)  #结束年
        self.end_year.grid(row=5, column=1, rowspan=1, columnspan=1)
        self.end_month = Text(self.init_window_name, width=2, height=1)  #结束月
        self.end_month.grid(row=5, column=7, rowspan=1, columnspan=1)
        self.end_day = Text(self.init_window_name, width=2, height=1)  # 结束日
        self.end_day.grid(row=5, column=9, rowspan=1, columnspan=1)
        self.result = Text(self.init_window_name, width=8, height=1)  # 计算结果
        self.result.grid(row=10, column=8, rowspan=7, columnspan=7)
        #按钮
		
        self.encrypt_button = Button(self.init_window_name, text="计算", font=(3), bg="Cyan", width=5,command=self.calculate)  #计算按钮
        self.encrypt_button.grid(row=10, column=0, rowspan=1, columnspan=1)


		
	#计算功能函数
    def calculate(self):
        y1 = self.start_year.get(1.0,END)
        m1 = self.start_month.get(1.0,END)
        d1 = self.start_day.get(1.0,END)
        y2 = self.end_year.get(1.0,END)
        m2 = self.end_month.get(1.0,END)
        d2 = self.end_day.get(1.0,END)

        date1 = date(int(y1),int(m1),int(d1))
        date2 = date(int(y2),int(m2),int(d2))

        date_delta = date2 - date1
        date_num = str(date_delta)
        print(date_num)
        if(len(date_num) == 14 or len(date_num) == 15):
            newnum = date_num[0:1]
        elif(len(date_num) == 16):
            newnum = date_num[0:2]
        elif(len(date_num) == 17):
            newnum = date_num[0:3]
        elif(len(date_num) == 18):
            newnum = date_num[0:4]
        elif(len(date_num) == 7):
            newnum = '调皮？？？'
        else:
            newnum = date_num[0:5]
        self.result.delete(1.0,END)
        self.result.insert(1.0, newnum+"天")

def gui_start():
    init_window = Tk()              #实例父窗口
    ZMJ_PORTAL = M_notebook(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()          #父窗口进入事件循环，保持窗口运行


gui_start()