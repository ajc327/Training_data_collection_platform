# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 09:56:16 2019

@author: ifssc
"""
from tkinter import *
from tkinter import simpledialog,filedialog
import os 
import shutil 
from PIL import Image, ImageTk



#编写上方工具栏

class Toolbar(Frame):
    def __init__(self, master ):
        Frame.__init__(self,master)
        
        
        toolbar = Frame( self.master, bd =1, relief = RAISED)
        toolbar.grid(column = 0,row=0)
        mode_button = Button(toolbar, text = "选择图片文件夹", command = self.choose_dir)
        mode_button.grid(row = 0, column = 0)
        
        pic_button = Button(toolbar, text = "选择图片", command = self.jump_to_pic)
        pic_button.grid(row = 0, column = 3)
        
        
        self.image_name =None 



#跳到指定图片函数    
    def jump_to_pic(self):
        self.jumpdir = filedialog.askopenfilename()
    
        app.jump(self.jumpdir)
  
    
#刷新上方文件名提醒
    def update_image_title(self):
        if self.image_name == None: 
            
            self.image_name = app.image_path
            self.image_label = Label(self, text = 
                                       "                                                                                                                                "+self.image_name, fg= "green")
            self.image_label_2 = Label(self, text ="{}张中的第{}张".format(str(len(app.full_image_list)), str(app.next_image_num)))
            self.image_label_2.grid(row = 0, column =2)
            self.image_label.grid(row=0, column =1)
        else: 
            self.image_name = app.image_path
            self.image_label.configure(text = "                                                                                                                                "+self.image_name)
            
            self.image_label_2.configure(text ="{}张中的第{}张".format(str(len(app.full_image_list)), str(app.next_image_num)))
 
#选择路径函数       
    def choose_dir(self):
        self.file_dir = filedialog.askdirectory()
        
        if os.path.isdir(self.file_dir):
            
            app.image_folder = self.file_dir
        
            app.init_graphics()
            self.update_image_title()
            
            
        else: 
            messagebox.showinfo("error", "路径错误")





#编写右边工具指示灯
class indicators(Frame):
    def __init__(self,master):  
        
        #初始化指示灯图片
        Frame.__init__(self, master = None)
        self.canvas = Canvas(self, bd =5, relief = "ridge" )
        self.select = Image.open("square.png")
        
        self.select_tk = select_tk= ImageTk.PhotoImage(self.select)
        self.select_1_tk = select_1_tk = ImageTk.PhotoImage(Image.open("square_1.png"))

        
        
        self.zi_tk = zi_tk = ImageTk.PhotoImage(Image.open("zi.png"))
        self.zi_1_tk = zi_1_tk = ImageTk.PhotoImage(Image.open("zi_1.png"))
        
        self.wei_tk = wei_tk = ImageTk.PhotoImage(Image.open("wei.png"))
        self.wei_1_tk = wei_1_tk = ImageTk.PhotoImage(Image.open("wei_1.png"))
        
        self.cross_tk = cross_tk = ImageTk.PhotoImage(Image.open("cross.png"))
        self.cross_1_tk = cross_1_tk = ImageTk.PhotoImage(Image.open("cross_1.png"))

        #初始化canvas
        self.canvas.config(height =250, width =200)
        self.canvas.grid(row = 0, column =0)
        self.canvas.create_image(30,40,image = select_1_tk, anchor ="nw", tags ="select_1_tk")
        self.canvas.create_image(30,80,image = cross_1_tk, anchor ="nw", tags="cross_1_tk")
        self.canvas.create_image(30,120,image = wei_tk, anchor ="nw", tags ="wei_tk")

        self.canvas.create_image(30,160,image = zi_tk, anchor ="nw", tags ="zi_tk")
        self.select_flag=1 
        self.cross_flag =1
        self. zi_flag =0 
        self. wei_flag=0 
        

#指示灯刷新函数
        
    def update_select(self):
        
    
        if self.select_flag==0: 
            self.canvas.delete("select_tk")
            self.canvas.create_image(30,40, anchor = "nw", image = self.select_1_tk, tags ="select_1_tk")
    
            self.zi_flag=1
        
        else: 
            self.canvas.delete("select_1_tk")
            self.canvas.create_image(30,40, anchor = "nw", image = self.select_tk, tags ="select_tk")
    
            self.select_flag=0
            
    def update_zi(self):
        
        
        if self.zi_flag==0: 
            self.canvas.delete("zi_tk")
            self.canvas.create_image(30,160, anchor = "nw", image = self.zi_1_tk, tags ="zi_1_tk")
    
            self.zi_flag=1
        
        else: 
            self.canvas.delete("zi_1_tk")
            self.canvas.create_image(30,160, anchor = "nw", image = self.zi_tk, tags ="zi_tk")
    
            self.zi_flag=0
    def update_wei(self):
        
        
        if self.wei_flag==0: 
            self.canvas.delete("wei_tk")
            self.canvas.create_image(30,120, anchor = "nw", image = self.wei_1_tk, tags ="wei_1_tk")
    
            self.wei_flag=1
        
        else: 
            self.canvas.delete("wei_1_tk")
            self.canvas.create_image(30,120, anchor = "nw", image = self.wei_tk, tags ="wei_tk")
    
            self.wei_flag=0
                                
    def update_cross(self):
        
        
        if self.cross_flag==0: 
            self.canvas.delete("cross_tk")
            self.canvas.create_image(30,80, anchor = "nw", image = self.cross_1_tk, tags ="cross_1_tk")
    
            self.cross_flag=1
        
        else: 
            self.canvas.delete("cross_1_tk")
            self.canvas.create_image(30,80, anchor = "nw", image = self.cross_tk, tags ="cross_tk")
    
            self.cross_flag=0
# 禁用所有框取功能，在比对识别结果时使用
                    
    def turn_off_all(self):
        
            self.canvas.delete("select_1_tk")
            self.canvas.create_image(30,40, anchor = "nw", image = self.select_tk, tags ="select_tk")
            self.select_flag=0
            self.canvas.delete("cross_1_tk")
            self.canvas.create_image(30,80, anchor = "nw", image = self.cross_tk, tags ="cross_tk")
    
            self.cross_flag=0        
            self.canvas.delete("wei_1_tk")
            self.canvas.create_image(30,120, anchor = "nw", image = self.wei_tk, tags ="wei_tk")
    
            self.wei_flag=0
            
            self.canvas.delete("zi_1_tk")
            self.canvas.create_image(30,160, anchor = "nw", image = self.zi_tk, tags ="zi_tk")
    
            self.zi_flag=0
         


#主程序        
class Example(Frame):
               
    def __init__(self, master):
        Frame.__init__(self, master =None)
        self.x =self.y = 0

        self.master.title("tool")
        self.canvas = Canvas(self, bd =5, relief = "ridge")
        self.image_folder =None 
        #self.image_folder = r"D:\caijiatong\python\platform\picture_folder"
        self.select_mode =1 
        
        #初始化画框以及各种参数
        self.sbarv= Scrollbar(self, orient = VERTICAL)
        self.sbarh =Scrollbar(self, orient = HORIZONTAL)
        self.sbarv.config(command =self.canvas.yview)
        self.sbarh.config(command = self.canvas.xview)
        
        self.canvas.config(yscrollcommand =self.sbarv.set)
        self.canvas.config(xscrollcommand =self.sbarh.set)
        self.canvas.config(height =900, width =1500)
       
        
        self.type_def_mode =0
        self.biaozhi_check_mode_flag=0
        self.can_row = 0
        self.can_col = 1
        self.recog_mod_flag = 0 
        self.check_mode_flag =0 

        self.canvas.grid(row=self.can_row,column=self.can_col)
        self.sbarv.grid(row=self.can_row,column=self.can_col+1,stick=N+S)
        self.sbarh.grid(row=self.can_row+1,column=self.can_col,sticky=E+W)
        
        
        
        #初始化按键绑定
        self.canvas.focus_set()        
        
        self.canvas.bind("<ButtonPress-3>", self.on_right_button_press)

        self.canvas.bind("<B3-Motion>", self.on_move_press)

        self.canvas.bind("<ButtonRelease-3>", self.on_right_button_release)
        
        
        
        
        
        
        self.canvas.bind("<q>", self.data_type_mode)
        self.canvas.bind("<w>", self.check_mode)
        self.canvas.bind("<e>", self.biaozhi_check_mode)
        self.canvas.bind("<r>", self.recog_modification)
    
        self.canvas.bind("<Control-MouseWheel>", self.wheel_zoom)

        self.canvas.bind("<ButtonPress-1>", self.on_button_press)

        self.canvas.bind("<B1-Motion>", self.on_move_press)

        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

        self.canvas.bind("<MouseWheel>", self.wheel_pan)
    #    self.definition_list = []
        #self.init_graphics()
    
    
    
    def init_graphics(self):
        #初始化图像
        
        if self.image_folder != None:
            if not os.path.isdir(os.path.join(self.image_folder, "segGT")):
                os.makedirs(os.path.join(self.image_folder, "segGT"))
                
            self.gt_folder = os.path.join(self.image_folder, "segGT")
    
        #生成下一张上一张按钮
        
            self.next_im_button = Button(self, text = "下一张", command = self.next_im)
            self.next_im_button.grid(row = self.can_row, column = self.can_col+2, padx = 40)
            self.prev_im_button = Button(self, text = "上一张", command = self.prev_im)
            self.prev_im_button.grid(row = self.can_row, column = self.can_col-1, padx = 40)        
            self.next_image_num = 0
    
            self.filelist = os.listdir(self.image_folder)
            self.image_list =[]
            self.full_path_list = []  
            self.full_image_list = []
            self.full_txt_list = []
            self.full_gt_list= []
            
            
            self.canvas.bind("<ButtonPress-3>", self.on_right_button_press)
    
            self.canvas.bind("<B3-Motion>", self.on_move_press)
    
            self.canvas.bind("<ButtonRelease-3>", self.on_right_button_release)
            
            
            
            
            
            
            self.canvas.bind("<q>", self.data_type_mode)
            self.canvas.bind("<w>", self.check_mode)
            self.canvas.bind("<e>", self.biaozhi_check_mode)
            self.canvas.bind("<r>", self.recog_modification)
        
            self.canvas.bind("<Control-MouseWheel>", self.wheel_zoom)
    
            self.canvas.bind("<ButtonPress-1>", self.on_button_press)
    
            self.canvas.bind("<B1-Motion>", self.on_move_press)
    
            self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
    
            self.canvas.bind("<MouseWheel>", self.wheel_pan)            
            
            #根据路径初始化文件名列表
            
            for i in range (len(self.filelist)):
                self.full_path_list.append(os.path.join(self.image_folder,self.filelist[i]))
                
                if ".txt" in self.filelist[i]:
                    self.full_gt_list.append(os.path.join(self.gt_folder,self.filelist[i].replace(".txt","GT.txt")))
                    self.full_txt_list.append(os.path.join(self.image_folder,self.filelist[i]))
                    
                elif ".jpg" in self.filelist[i]:
                    self.full_image_list.append(os.path.join(self.image_folder,self.filelist[i]))
                    self.image_list.append(self.filelist[i])
            self.image_path = self.full_image_list[0]
            for item in self.full_txt_list: 
                if self.full_image_list[0].replace(".jpg","") in item: 
                    self.txtpath= item
                    break 
                
            #将正在处理的待标注文件备份到目标文件夹
            shutil.copy(self.txtpath, self.txtpath.replace(self.image_folder,self.gt_folder).replace(".txt","GT.txt"))
            self.im = Image.open(self.image_path)
            
            self.txtpath = self.txtpath.replace(self.image_folder,self.gt_folder).replace(".txt","GT.txt")
            print(self.txtpath)
    
            self.scale_cumu=1.0
            self.refresh_canvas()
            self.draw_rectangles_from_txt(self.txtpath)
    
            self.rect = None
            self.imscale = 1.0 
            self.imageid = None
            self.delta = 0.75
            width, height = self.im.size
            
            minsize, maxsize = 5,20 
            
    
    
    
            self.start_x = None
    
            self.start_y = None
           # self.text = self.canvas.create_text(0,0,anchor = "nw", text = "Scroll to zoom")
           #生成图片
            self.show_image()
    
    
            self.canvas.config(scrollregion=self.canvas.bbox('all'))
        else: 
            pass
        # self.tk_im = ImageTk.PhotoImage(self.im)
    
       # self.canvas.create_image(0,0,anchor="nw",image=self.tk_im)   
       
       
       
       #处理下一张图片函数
       
    def next_im(self):
        
        
        #初始化各项尺寸参数
        self.scale_cumu=1.0
        self.imscale=1.0
        self.canvas.delete("all")
        self.next_image_num+=1
        
        
        
        self.image_path= self.full_image_list[self.next_image_num]
        self.image_name = self.image_list[self.next_image_num]
        
        #根据图片名找到相应的txt文件，备份到目标文件夹
        
        
        for item in self.full_gt_list: 
            
            if self.image_name.replace(".jpg","") in item:
                shutil.copy(item.replace(r"\segGT","").replace("GT.txt",".txt"), item)

                self.txtpath = item
            
                break
            else:
                self.txtpath = ""
        print(self.txtpath)
        
        
        #初始化图片id等参数，重新定义图片，重新根据txt标注长方形
        self.imageid = None
        self.canvas.tk_im = None 
        self.im = Image.open(self.image_path)
        tk_im = ImageTk.PhotoImage(self.im)
        self.imageid = self.canvas.create_image(0,0, anchor = "nw", image = tk_im)
        #       self.text = self.canvas.create_text(0,0,anchor = "nw", text = "Scroll to zoom")
 
        self.canvas.lower(self.imageid)
        self.canvas.tk_im = tk_im        
        self.draw_rectangles_from_txt(self.txtpath)
        bar.update_image_title()
        self.rect= None 
     
        #上一张图片按钮函数    
    def prev_im(self): 
        self.scale_cumu=1.0
        self.imscale=1.0
        self.canvas.delete("all")
        self.next_image_num-=1
        
        self.image_path= self.full_image_list[self.next_image_num]
        self.image_name = self.image_list[self.next_image_num]
        for item in self.full_gt_list: 
            
            if self.image_name.replace(".jpg","") in item:
                shutil.copy(item.replace(r"\segGT","").replace("GT.txt",".txt"), item)

                self.txtpath = item
            
                break
            else:
                self.txtpath = ""
        print(self.txtpath)
        self.imageid = None
        self.canvas.tk_im = None 
        self.im = Image.open(self.image_path)
        tk_im = ImageTk.PhotoImage(self.im)
        self.imageid = self.canvas.create_image(0,0, anchor = "nw", image = tk_im)
 #       self.text = self.canvas.create_text(0,0,anchor = "nw", text = "Scroll to zoom")

        self.canvas.lower(self.imageid)
        self.canvas.tk_im = tk_im        
        self.draw_rectangles_from_txt(self.txtpath)
        bar.update_image_title()
        self.rect= None 
        
        
        
        #跳到指定图片函数，与下一张上一张函数基本相同
        
    def jump(self, jumpdir):
        self.scale_cumu=1.0
        self.imscale=1.0
        self.canvas.delete("all")
        print(self.full_image_list )
        image_name = ''
        for item in self.full_image_list: 
            if item.split("\\")[-1].replace(".jpg","").replace(".txt","") in jumpdir: 
                image_name = item 
                break 
        self.next_image_num = self.full_image_list.index(image_name)

        self.image_path= self.full_image_list[self.next_image_num]
        self.image_name = self.image_list[self.next_image_num]
        
        for item in self.full_gt_list: 
            
            if self.image_name.replace(".jpg","") in item:
                shutil.copy(item.replace(r"\segGT","").replace("GT.txt",".txt"), item)

                self.txtpath = item
            
                break
            else:
                self.txtpath = ""
        print(self.txtpath)
        self.imageid = None
        self.canvas.tk_im = None 
        self.im = Image.open(self.image_path)
        tk_im = ImageTk.PhotoImage(self.im)
        self.imageid = self.canvas.create_image(0,0, anchor = "nw", image = tk_im)
 #       self.text = self.canvas.create_text(0,0,anchor = "nw", text = "Scroll to zoom")

        self.canvas.lower(self.imageid)
        self.canvas.tk_im = tk_im        
        self.draw_rectangles_from_txt(self.txtpath)
        bar.update_image_title()
        self.rect= None         
        
        
        
        #重置图片大小函数
    def refresh_canvas(self):
        print(self.image_folder)
        self.scale_cumu=1.0
        self.imscale=1.0
        self.canvas.delete("all")
        self.imageid = None
        self.canvas.tk_im = None 
        self.im = Image.open(self.image_path)
        tk_im = ImageTk.PhotoImage(self.im)
        self.imageid = self.canvas.create_image(0,0, anchor = "nw", image = tk_im)
 #       self.text = self.canvas.create_text(0,0,anchor = "nw", text = "Scroll to zoom")

        self.canvas.lower(self.imageid)
        self.canvas.tk_im = tk_im        
        self.draw_rectangles_from_txt(self.txtpath)
        self.rect= None         
  



        #识别结果比对函数      
    def check_mode(self, event):
        
        if self.check_mode_flag ==0: 
            
            #禁用框取功能， 删除标注长方形， 放大到固定尺寸
            indicator_app.turn_off_all()
            self.select_mode = 0 
            self.canvas.delete("rects")
            myTxt = open(self.txtpath, 'r')
            self. refresh_canvas()
            myLines = myTxt.readlines()
            self.imscale*=self.delta            
            self.canvas.scale('all',0,0,0.75,0.75)
            self.scale_cumu *= 0.75
            self.show_image()
            self.canvas.configure(scrollregion = self.canvas.bbox("all")) 
            self.canvas.unbind("<q>")
            self.canvas.unbind("<r>")


            #读txt文件，画出标注长方形以及识别结果长方形
            for i in range(len(myLines)):
                if i %2 ==1:
            
                    x1,x2, y1,y2  = int(myLines[i].split("\t")[0]),int(myLines[i].split("\t")[1]), int(myLines[i].split("\t")[2]), int(myLines[i].split("\t")[3])
                    # print (x1,y1,x2,y2)
                    scaled_coors = []
                    for item in [x1,y1,x2,y2]:
                        item = int(item* self.scale_cumu)
                        scaled_coors.append (item)
                    self.canvas.create_rectangle (scaled_coors[0],scaled_coors[1],scaled_coors[2],scaled_coors[3], outline = "green", tags="rects")
                    recog_result = myLines[i-1].replace("\n","")
                    
                    #生成识别结果长方形和识别结果
                    wid = int(self.im.size[0]*0.6)
                    
                    self.canvas.create_rectangle (scaled_coors[0]+wid,scaled_coors[1],scaled_coors[2]+wid,scaled_coors[3], fill ="white", outline = "green", tags="rects")
                    self.canvas.create_text((scaled_coors[0]+scaled_coors[2])/2+wid, (scaled_coors[3] +scaled_coors[1])/2,text =recog_result.replace("\t",""), font = ("freemono bold", 13))
                    
            myTxt.close() 
            self.check_mode_flag =1 
            
        #如果已经在识别结果比对模式中， 再次按快捷键则退出该模式
        else: 
            self.refresh_canvas()
            self.check_mode_flag = 0
            self.select_mode=1
            indicator_app.update_cross()
            indicator_app.update_select()            
            self.canvas.bind("<q>", self.data_type_mode)

            self.canvas.bind("<r>", self.recog_modification)   
            
            
            
            #标志位比对函数, 和识别结果比对函数类似
    def biaozhi_check_mode(self, event):
        
        if self.biaozhi_check_mode_flag ==0: 
            
            
            self.canvas.delete("rects")
            myTxt = open(self.txtpath, 'r')
            self. refresh_canvas()
            self.select_mode = 0 

            self.imscale*=self.delta            
            myLines = myTxt.readlines()
            self.canvas.scale('all',0,0,0.75,0.75)
            self.scale_cumu *= 0.75
            self.show_image()
            self.canvas.configure(scrollregion = self.canvas.bbox("all"))            
            self.canvas.unbind("<q>")
            self.canvas.unbind("<r>")            
            for i in range(len(myLines)):
                if i %2 ==1:
                    x1,x2, y1,y2  = int(myLines[i].split("\t")[0]),int(myLines[i].split("\t")[1]), int(myLines[i].split("\t")[2]), int(myLines[i].split("\t")[3])
                    # print (x1,y1,x2,y2)
                    scaled_coors = []
                    for item in [x1,y1,x2,y2]:
                        item = int(item* self.scale_cumu)
                        scaled_coors.append (item)
                    self.canvas.create_rectangle (scaled_coors[0],scaled_coors[1],scaled_coors[2],scaled_coors[3], outline = "green", tags="rects")
                    biaozhi_result = myLines[i].split("\t")[4].replace("\n",'')
                    wid = int(self.im.size[0]*0.6)
                    self.canvas.create_rectangle (scaled_coors[0]+wid,scaled_coors[1],scaled_coors[2]+wid,scaled_coors[3], fill ="#FCF3CF", outline = "blue", tags="rects")
                    self.canvas.create_text((scaled_coors[0]+scaled_coors[2])/2+wid, (scaled_coors[3] +scaled_coors[1])/2,text =biaozhi_result, font = ("freemono bold", 13))
                    
            myTxt.close() 
            indicator_app.turn_off_all()            
            
            
            self.biaozhi_check_mode_flag =1 
        
        else: 
                        
            self.refresh_canvas()
            self.biaozhi_check_mode_flag = 0        
            self.select_mode =1
            indicator_app.update_cross()
            indicator_app.update_select()
    
            self.canvas.bind("<q>", self.data_type_mode)

            self.canvas.bind("<r>", self.recog_modification)     
            
            
            
    #改字函数        
    def recog_modification(self, event):
        
        print("recog_mod_flag =%d" % self.recog_mod_flag )
        if self.recog_mod_flag ==0:
            #先禁用框取各功能
            self.select_mode=0 
            print(self.select_mode)
            
            #将鼠标按键绑定到改字鼠标按下函数
            self.canvas.bind("<ButtonPress-1>", self.on_recog_mod_button_press)

            indicator_app.turn_off_all()
            indicator_app.zi_flag=0

            indicator_app.update_zi()

            self.recog_mod_flag =1
            
            #如果已经在这个模式下则退出该模式
        else: 
            self.select_mode =1 
            self.canvas.bind("<ButtonPress-1>", self.on_button_press)
    
            indicator_app.select_flag=0
            indicator_app.zi_flag=1
            indicator_app.update_select()
            indicator_app.update_cross()            
            indicator_app.update_zi()
            self.recog_mod_flag =0
        
        
        
        
        
    #改字模式的鼠标按下函数    
    def on_recog_mod_button_press(self, event): 
        x, y = self.canvas.canvasx(event.x),self.canvas.canvasy(event.y)
        
        
        
        my_txt = open(self.txtpath, "r")
        myLines = my_txt.readlines()
        
        coors =[]
        for i in range(len(myLines)):
            
            #读取txt，按积累放大倍数调整
            if i %2 ==1:
                x1,x2, y1,y2 = int(myLines[i].split("\t")[0]),int(myLines[i].split("\t")[1]), int(myLines[i].split("\t")[2]), int(myLines[i].split("\t")[3])
                # print (x1,y1,x2,y2)
                x1 *=self.scale_cumu
                x2 *=self.scale_cumu
                y1 *=self.scale_cumu
                y2 *=self.scale_cumu
                
                
                #如果鼠标点击的位置在某个框中间则弹窗问识别结果，将结果存在列表中
                if x1<x and x2>x and y1<y and y2>y:
                    org_value = myLines[i-1].replace("\t","").replace("\n","")
                    recognition= simpledialog.askstring("Input Number", "当前值:{0}, \n输入识别结果".format(org_value))
                    if recognition=="":
                        pass 
                    else:
                        coors.append([i,recognition])    
                    self.canvas.focus_set()        
                    
        print(coors)
        #过一遍识别结果列表，修改txt
        for pair in coors:
            
            myLines[pair[0]-1] = pair[1]+"\t\n"
            
          
        
        my_txt = open(self.txtpath, "w")
        for item in myLines: 
            my_txt.write(item)
        
        my_txt.close()
        #刷新一下识别长方形
        self.canvas.delete("rects")

        
        self.draw_rectangles_from_txt(self.txtpath)      
        
        
        
    def draw_rectangles_from_txt(self, path):
        
        myTxt = open(path, 'r')
        
        myLines = myTxt.readlines()
        
        for i in range(len(myLines)):
            if i %2 ==1:
                x1,x2, y1,y2 = int(myLines[i].split("\t")[0]),int(myLines[i].split("\t")[1]), int(myLines[i].split("\t")[2]), int(myLines[i].split("\t")[3])
                # print (x1,y1,x2,y2)
                scaled_coors = []
                for item in [x1,y1,x2,y2]:
                    item = int(item* self.scale_cumu)
                    scaled_coors.append (item)
                self.canvas.create_rectangle (scaled_coors[0],scaled_coors[1],scaled_coors[2],scaled_coors[3], outline = "cyan",width=2, tags="rects")
                
                
        myTxt.close()
        
        
        
    
        
        
        
    #框取模式鼠标按下函数
        
    def on_button_press(self, event):
        if self.select_mode ==1:
            global x_atclick, y_atclick
            #鼠标按下地点的坐标
            x_atclick = self.canvas.canvasx(event.x)
            y_atclick = self.canvas.canvasy(event.y)
            print ("x0:  ",self.canvas.canvasx(0))
            print ("x_ev: ", self.canvas.canvasx(event.x))
            
            print ("y0: ",self.canvas.canvasy(0))
            print ("yevent: ",self.canvas.canvasy(event.y)) 
            
            
        
            
            self.start_x = self.canvas.canvasx(event.x)
    
            self.start_y = self.canvas.canvasy(event.y)
    
            
            self.canvas.delete("select")
            self.rect= None


            #生成标注长方形    
            if not self.rect:
    
                self.rect = self.canvas.create_rectangle(self.x, self.y, 1, 1, outline='yellow', tags= "select")
        else:
            pass 


    #鼠标右键函数（删除框）
    def on_right_button_press(self, event):
        if self.select_mode ==1: 
            global x_atclick, y_atclick
            x_atclick = self.canvas.canvasx(event.x)
            y_atclick = self.canvas.canvasy(event.y)
            print ("x0:  ",self.canvas.canvasx(0))
            print ("x_ev: ", self.canvas.canvasx(event.x))
            
            print ("y0: ",self.canvas.canvasy(0))
            print ("yevent: ",self.canvas.canvasy(event.y)) 
            # save mouse drag start position
    
            self.start_x = self.canvas.canvasx(event.x)
    
            self.start_y = self.canvas.canvasy(event.y)
    
            
            self.canvas.delete("select")
            self.rect = None 
    
            # create rectangle if not yet exist
    
            if not self.rect:
    
                self.rect = self.canvas.create_rectangle(self.x, self.y, 1, 1, outline='red', tags ="select")

        else: 
            pass 
        

    


#鼠标滑轮缩放功能函数
    def wheel_zoom(self,event):
      #  print(event.delta)

        scale = 1.0 
        
        #如果鼠标滚轮数值对应上滚活下滚，改变缩放参数
        if event.delta ==-120:
            #self.canvas.yview_scroll(2, "units")
            scale *= self.delta 
            self.imscale*=self.delta
           
        if event.delta ==120:
            #self.canvas.yview_scroll (-2, "units")
            scale /= self.delta 
            self.imscale/= self.delta 
        
        
        #将画布根据缩放参数进行缩放并启动生成图片函数
        x= self.canvas.canvasx(event.x)
        y= self.canvas.canvasy(event.y)
        self.canvas.scale('all',0,0,scale,scale)
        self.scale_cumu *= scale
        self.show_image()
        print(self.scale_cumu)
        self.canvas.configure(scrollregion = self.canvas.bbox("all"))
        
    #鼠标滚轮平移函数   
    def wheel_pan(self,event):
      #  print(event.delta)

        scale = 1.0 
        
        if event.delta ==-120:
            self.canvas.yview_scroll(2, "units")
            #scale *= self.delta 
            #self.imscale*=self.delta
           
        if event.delta ==120:
            self.canvas.yview_scroll (-2, "units")
            #scale /= self.delta 
            #self.imscale/= self.delta 
        
    
        self.show_image()
        print(self.scale_cumu)
        self.canvas.configure(scrollregion = self.canvas.bbox("all"))   
        
        
    #生成图片函数    
    def show_image(self):
        #初始化各项图片参数
        if self.imageid: 
            self.canvas.delete(self.imageid)
            self.imageid = None
            self.canvas.tk_im = None 
        width, height = self.im.size 
        #使用缩放参数生成图片
        new_size = int(self.imscale*width), int(self.imscale* height)
        tk_im = ImageTk.PhotoImage(self.im.resize(new_size))
        self.imageid = self.canvas.create_image(0,0, anchor = "nw", image = tk_im)
        self.canvas.lower(self.imageid)
        self.canvas.tk_im = tk_im
        
        
        
        #鼠标拖拽函数
    def on_move_press(self, event):
        if self.select_mode==1:
            
            #采用鼠标坐标
            curX = self.canvas.canvasx(event.x)
    
            curY = self.canvas.canvasy(event.y)
    
    
    
            w, h = self.canvas.winfo_width(), self.canvas.winfo_height()
    
    
    
    
    
            #刷新生成出的标注框
            self.canvas.coords(self.rect, self.start_x, self.start_y, curX, curY)    
        else: 
            pass 



        #框取模式鼠标松开左键的函数
    def on_button_release(self, event):
        if self.select_mode==1:
            
            global finish_x, finish_y
            finish_x, finish_y = self.canvas.canvasx(event.x),self.canvas.canvasy(event.y)
            
            #计算鼠标点下和松开的极限坐标
            outTxt = open('out.txt', 'a')
            
            x= (int(min([finish_x,x_atclick])), int(max([finish_x, x_atclick] )))
            y = (int(min([finish_y,y_atclick])), int(max([finish_y, y_atclick] )))
            out_list_old = [x[0], x[1],y[0],y[1]]
            out_list=[]
            print(out_list_old)
            print(self.scale_cumu)
            
            #除以缩放参数
            
            for item in out_list_old: 
                item = int(item/self.scale_cumu) 
                out_list.append(item)
                
            #框小了就不要了
            if abs(out_list[0]-out_list[1])*abs(out_list[3]-out_list[2])>=60:
                
                #输入识别结果，将识别结果写入
                recognition= simpledialog.askstring("Input Number", "输入识别数值")
                if recognition != None and recognition !="":
                    print(recognition)
                    self.canvas.focus_set()        
        
                    my_txt = open(self.txtpath, "a")
                    print(out_list)
                    my_txt.write("{0}\t\n".format(recognition))
                    
                    my_txt.write("{0}\t{1}\t{2}\t{3}\t\n".format(out_list[0], out_list[1], out_list[2], out_list[3]))
                    
                    my_txt.close()
            
            self.canvas.delete("rects")
            self.draw_rectangles_from_txt(self.txtpath)
            pass    
        else:
            pass

    #鼠标右键松开的函数（删除框）
    def on_right_button_release(self, event):
        if self.select_mode==1:
            global finish_x, finish_y
            finish_x, finish_y = self.canvas.canvasx(event.x),self.canvas.canvasy(event.y)
            
            #计算极限坐标
            x= (int(min([finish_x,x_atclick])), int(max([finish_x, x_atclick] )))
            y = (int(min([finish_y,y_atclick])), int(max([finish_y, y_atclick] )))
            
            my_txt = open(self.txtpath, "r")
            print(x,y)
            myLines = my_txt.readlines()
            
            #如果极限坐标内有标注结果，将它们的序号记下
            coors =[]
            for i in range(len(myLines)):
                if i %2 ==1:
                    x1,x2, y1,y2 = int(myLines[i].split("\t")[0]),int(myLines[i].split("\t")[1]), int(myLines[i].split("\t")[2]), int(myLines[i].split("\t")[3])
                    # print (x1,y1,x2,y2)
                    x1 *=self.scale_cumu
                    x2 *=self.scale_cumu
                    y1 *=self.scale_cumu
                    y2 *=self.scale_cumu
                    
                    if x[0]<x1 and x[1]>x2 and y[0]<y1 and y[1]>y2 :
                       coors.append(i-1)
                       coors.append(i)
            #根据该删的序号列表倒序进行删除
            for index in sorted(coors, reverse = True):
                del myLines[index]
            
            my_txt = open(self.txtpath, "w")
            for item in myLines: 
                my_txt.write(item)
            
            my_txt.close()
            
            self.canvas.delete("rects")
    
            
            self.draw_rectangles_from_txt(self.txtpath)
            pass    
        else:
            pass 
        
        
    #标志位模式
    def data_type_mode(self,event):
        
        
        if self.type_def_mode ==0: 
            #把鼠标右键绑定的各函数换成标志位函数
            indicator_app.wei_flag= 0
            indicator_app.cross_flag=1
            indicator_app.update_cross()
            indicator_app.update_wei()
            
            self.canvas.bind("<ButtonPress-3>", self.on_type_button_press)
    
            self.canvas.bind("<B3-Motion>", self.on_move_press)
    
            self.canvas.bind("<ButtonRelease-3>", self.on_type_button_release) 
            self.type_def_mode =1
        else: 
            self.canvas.bind("<ButtonPress-3>", self.on_right_button_press)
    
            self.canvas.bind("<B3-Motion>", self.on_move_press)
    
            self.canvas.bind("<ButtonRelease-3>", self.on_right_button_release)
            self.type_def_mode =0 
            indicator_app.wei_flag= 1
            indicator_app.cross_flag=0
            indicator_app.update_cross()
            indicator_app.update_wei()
        
        
        
    #标志位模式鼠标函数    
    def on_type_button_release(self, event):
        if self.select_mode==1:
            
            global finish_x, finish_y
            finish_x, finish_y = self.canvas.canvasx(event.x),self.canvas.canvasy(event.y)
            
            
            x= (int(min([finish_x,x_atclick])), int(max([finish_x, x_atclick] )))
            y = (int(min([finish_y,y_atclick])), int(max([finish_y, y_atclick] )))
            if abs(x[0]-x[1])*abs(y[0]-y[1])>=60:
    
                my_txt = open(self.txtpath, "r")
                print(x,y)
                myLines = my_txt.readlines()
                
                
                data_type_num= simpledialog.askstring("Input Number", "输入标志位值")
                self.canvas.focus_set()        
                #如果有框取结果在极限坐标之内则记录序号
                coors =[]
                for i in range(len(myLines)):
                    if i %2 ==1:
                        x1,x2, y1,y2 = int(myLines[i].split("\t")[0]),int(myLines[i].split("\t")[1]), int(myLines[i].split("\t")[2]), int(myLines[i].split("\t")[3])
                        # print (x1,y1,x2,y2)
                        x1 *=self.scale_cumu
                        x2 *=self.scale_cumu
                        y1 *=self.scale_cumu
                        y2 *=self.scale_cumu
                        
                        
                        if x[0]<x1 and x[1]>x2 and y[0]<y1 and y[1]>y2 :
                           coors.append(i)
                try:
                    for index in coors:
                        myLines[index]= '\t'.join(myLines[index].split("\t")[:4])+ "\t"+ data_type_num +"\t\n"
                except:
                    pass 
                my_txt = open(self.txtpath, "w")
                for item in myLines: 
                    my_txt.write(item)
                
                my_txt.close()
            
            self.canvas.delete("rects")
    
            
            self.draw_rectangles_from_txt(self.txtpath)
            pass    
        
        else: 
            pass 
        
    def on_type_button_press(self, event):
        if self.select_mode ==1: 
            global x_atclick, y_atclick
            x_atclick = self.canvas.canvasx(event.x)
            y_atclick = self.canvas.canvasy(event.y)
            print ("x0------------------------:  ",self.canvas.canvasx(0))
            print ("x_ev: ", self.canvas.canvasx(event.x))
            
            print ("y0: ",self.canvas.canvasy(0))
            print ("yevent: ",self.canvas.canvasy(event.y)) 
            # save mouse drag start position
    
            self.start_x = self.canvas.canvasx(event.x)
    
            self.start_y = self.canvas.canvasy(event.y)
    
            
            self.canvas.delete("select")
            self.rect = None 
    
            # create rectangle if not yet exist
    
            if not self.rect:
    
                self.rect = self.canvas.create_rectangle(self.x, self.y, 1, 1, outline='blue', tags ="select")
        else: 
            pass 
                                                     
                                            

if __name__ == "__main__":

    root=Tk()
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),root.winfo_screenheight()))
    app = Example(root)

    
    #toolbar_frame= Frame(root, bd =5 , height =50, width = 1000, relief = RAISED)
    #toolbar_frame.grid(row = 0, column =0)


    bar = Toolbar(root)
    bar.grid(row=0, column =0)
    app.grid(row =1, column =0)
    indicator_app = indicators(root)
    indicator_app.place(x =1670, y=100)

    root.mainloop()
        

