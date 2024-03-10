import tkinter as tk
from PIL import ImageTk, Image
import cv2
import csv
import os

picture_height=900
picture_width=780

pic_path="be_detected_screw.jpg"
global read_cover_pic


def auto_detected_screw_rules():
    ImageSlideshow(root, image_folder="D://measure_screw_detection//detected_screw_save_pic//")
    
    


class ImageSlideshow(tk.Frame):
    def __init__(self, master=None, image_folder=None):
        super().__init__(master)
        self.master = master
        self.image_folder = image_folder
        self.images = []
        self.save_image_pages_path=[]
        self.current_image = None
        self.load_images()
        self.create_widgets()
        
    def show_next_image(self):
        global read_cover_pic
        self.current_image += 1
        if self.current_image >= len(self.images):
            self.current_image = 0
        self.label.configure(image=self.images[self.current_image])
        print(self.save_image_pages_path[self.current_image])
        read_cover_pic=self.save_image_pages_path[self.current_image]
        cover_rule_screw()
        compare_screw_is_same_rule()
        self.after(3000, self.show_next_image)


    def load_images(self):
        global read_cover_pic
        for filename in os.listdir(self.image_folder):
            image_path = os.path.join(self.image_folder, filename)
            with Image.open(image_path) as img:
                self.save_image_pages_path.append(image_path)
                img = img.resize((300, 300), Image.Resampling.LANCZOS)
                self.images.append(ImageTk.PhotoImage(img))

        
                
    def create_widgets(self):
        self.label = tk.Label(self.master, image=self.images[0])
        self.label.pack()
        self.current_image = 0
        self.after(3000, self.show_next_image)
        
    




def cover_rule_screw():

    #read_cover_pic="s.jpg" #按照規格畫線，確認是否為同樣規格螺絲


    global length_point_a_1
    global length_point_a_2
    global length_point_b_1
    global length_point_b_2


    # 牙距
    global point_a1
    global point_a2
    global point_b1
    global point_b2

    #螺紋長度
    global point_c1
    global point_c2
    global point_d1
    global point_d2

    #螺絲底部直徑
    global point_e1
    global point_e2
    global point_f1
    global point_f2

    with open('screw_data_point.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        # 跳過標題行
        next(csv_reader)

        numbers1 = []
        numbers2 = []
        numbers3 = []
        numbers4 = []
        flag=0
        for row in csv_reader:
        #print(row)

            for char in row[0]:
                if char.isdigit() and flag==0:
                    numbers1.append(char)

                elif char.isspace():
                    flag=1

                elif char.isdigit() and flag==1:
                    numbers2.append(char)


            flag=0

            for char in row[1]:
                if char.isdigit() and flag==0:
                    numbers3.append(char)

                elif char.isspace():
                    flag=1

                elif char.isdigit() and flag==1:
                    numbers4.append(char)

            flag=0

            num_str = "".join(str(num) for num in numbers1)
            num = int(num_str)
            point_a1=num

            num_str = "".join(str(num) for num in numbers2)
            num = int(num_str)
            point_a2=num


            num_str = "".join(str(num) for num in numbers3)
            num = int(num_str)
            point_b1=num

            num_str = "".join(str(num) for num in numbers4)
            num = int(num_str)
            point_b2=num
        

    with open('screw_data_point_2.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        # 跳過標題行
        next(csv_reader)

        numbers1 = []
        numbers2 = []
        numbers3 = []
        numbers4 = []
        flag=0
        for row in csv_reader:
        #print(row)



            for char in row[0]:
                if char.isdigit() and flag==0:
                    numbers1.append(char)

                elif char.isspace():
                    flag=1

                elif char.isdigit() and flag==1:
                    numbers2.append(char)


            flag=0

            for char in row[1]:
                if char.isdigit() and flag==0:
                    numbers3.append(char)

                elif char.isspace():
                    flag=1

                elif char.isdigit() and flag==1:
                    numbers4.append(char)

            flag=0

            num_str = "".join(str(num) for num in numbers1)
            num = int(num_str)
            point_c1=num

            num_str = "".join(str(num) for num in numbers2)
            num = int(num_str)
            point_c2=num


            num_str = "".join(str(num) for num in numbers3)
            num = int(num_str)
            point_d1=num

            num_str = "".join(str(num) for num in numbers4)
            num = int(num_str)
            point_d2=num

    with open('screw_data_point_3.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        # 跳過標題行
        next(csv_reader)

        numbers1 = []
        numbers2 = []
        numbers3 = []
        numbers4 = []
        flag=0
        for row in csv_reader:
        #print(row)

            for char in row[0]:
                if char.isdigit() and flag==0:
                    numbers1.append(char)

                elif char.isspace():
                    flag=1

                elif char.isdigit() and flag==1:
                    numbers2.append(char)


            flag=0

            for char in row[1]:
                if char.isdigit() and flag==0:
                    numbers3.append(char)

                elif char.isspace():
                    flag=1

                elif char.isdigit() and flag==1:
                    numbers4.append(char)

            flag=0

            num_str = "".join(str(num) for num in numbers1)
            num = int(num_str)
            point_e1=num

            num_str = "".join(str(num) for num in numbers2)
            num = int(num_str)
            point_e2=num


            num_str = "".join(str(num) for num in numbers3)
            num = int(num_str)
            point_f1=num

            num_str = "".join(str(num) for num in numbers4)
            num = int(num_str)
            point_f2=num

    # print(point_a1)
    # print(point_a2)
    # print(point_b1)
    # print(point_b2)


    # print(point_c1)
    # print(point_c2)
    # print(point_d1)
    # print(point_d2)


    # print(point_e1)
    # print(point_e2)
    # print(point_f1)
    # print(point_f2)



    # 讀取圖像
    img = cv2.imread(read_cover_pic)

    detect_length_1=[point_a1,point_a2]
    detect_length_2=[point_b1,point_b2]

    detect_thread_1=[point_c1,point_c2]
    detect_thread_2=[point_d1,point_d2]

    detect_bottom_1=[point_e1,point_e2]
    detect_bottom_2=[point_f1,point_f2]


    # print(detect_length_1)
    # print(detect_length_2)

    cv2.line(img, detect_length_1,detect_length_2, (0, 0, 255), 20)
    cv2.line(img, detect_thread_1,detect_thread_2, (0, 0, 255), 20)
    cv2.line(img, detect_bottom_1,detect_bottom_2, (0, 0, 255), 20)

    cv2.imwrite(pic_path, img)
    # print("cover_rules_screw_path:"+pic_path)

    canvas1.delete('all')

 
    img = Image.open(pic_path)
    img = img.resize((300, 300), Image.Resampling.LANCZOS)
    # 將圖片轉換為tkinter可用的格式
    img_tk = ImageTk.PhotoImage(img)
    # 在canvas上創建新圖片
    canvas1.create_image(0, 0, image=img_tk, anchor=tk.NW)
    # 記得保留對img_tk的引用，否則會被垃圾回收機制回收，導致圖片不顯示
    canvas1.image = img_tk

    canvas1.pack()


    # global img_label
    # img = Image.open(pic_path)
    # img = img.resize((300, 300), Image.ANTIALIAS)
    # img = ImageTk.PhotoImage(img)
    # img_label.configure(image=img)
    # img_label.image = img


    #顯示圖像
    # cv2.namedWindow(pic_path, cv2.WINDOW_NORMAL)
    # cv2.resizeWindow(pic_path, picture_height, picture_width)
    # cv2.imshow(pic_path, img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


def get_input():
    global read_cover_pic
    text = entry.get()
    if not text:
        text = "3.jpg"

    read_cover_pic=text
    # print(read_cover_pic)
    # print(text)


def compare_screw_is_same_rule():


    img1 = cv2.imread("perfect_rule_screw.jpg")
    img2 = cv2.imread(pic_path)


    # 將圖像調整為相同的大小
    img1 = cv2.resize(img1, (800, 600))
    img2 = cv2.resize(img2, (800, 600))

    # 將圖像轉換為灰度圖像
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)


    # 比較兩張圖像的差異
    diff = cv2.absdiff(gray1, gray2)

    

    # resImg = cv2.absdiff(gray1, gray2)
    # cv2.imwrite("show_resImg",resImg)
    # cv2.imshow("resImg ", resImg )
    # cv2.waitKey(0)

    # 將差異圖像二值化
    thresh = cv2.threshold(diff, 100, 255, cv2.THRESH_BINARY)[1]

    # 腐蝕圖像，進一步消除差異
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    erode = cv2.erode(thresh, kernel)


    #判斷結果，如果 erode 為一個空圖像，則表示兩張圖像相同
    if cv2.countNonZero(erode) == 0:
        label_compare_text.config(text="兩個螺絲規格相同",bg="green")
        print("兩張圖像相同")
    else:
        label_compare_text.config(text="兩個螺絲規格不同",bg="red")
        print("兩張圖像不同")



root = tk.Tk()
root.geometry("800x800")

# 加載圖片

image1 = Image.open(pic_path)
image2 = Image.open("perfect_rule_screw.jpg")


# 縮小圖片
image1 = image1.resize((300, 300))
image2 = image2.resize((300, 300))

# 轉換為PhotoImage對象
img1 = ImageTk.PhotoImage(image1)
img2 = ImageTk.PhotoImage(image2)



#比較螺絲規格按鈕
compare_button = tk.Button(root, text="比較螺絲規格", command=compare_screw_is_same_rule)

#把螺絲規格套在帶偵測的螺絲，檢查是否符合
cover_rules_button = tk.Button(root, text="套入待偵測螺絲規格", command=cover_rule_screw)

#自動把螺絲規格套在帶偵測的螺絲，之後檢查是否符合
auto_cover_rules_button=tk.Button(root,text="自動偵測螺絲規格和比較螺絲規格",command=auto_detected_screw_rules)


#輸入待偵測圖片路徑
entry = tk.Entry(root)
entry.pack()

button_input = tk.Button(root, text="輸入待檢測圖片路徑", command=get_input)
button_input.pack()


# 創建Frame
frame = tk.Frame(root)
frame.pack(expand=True, fill=tk.BOTH)


label_compare_text = tk.Label(root, text="")
label_compare_text.pack(side=tk.TOP,anchor=tk.N)


# 在Frame中創建Canvas
compare_button.pack(side=tk.TOP,anchor=tk.N)
cover_rules_button.pack(side=tk.TOP,anchor=tk.N)
auto_cover_rules_button.pack(side=tk.TOP,anchor=tk.N)


canvas1 = tk.Canvas(frame, width=300, height=300)
canvas1.pack(side=tk.LEFT)
canvas2 = tk.Canvas(frame, width=300, height=300)
canvas2.pack(side=tk.RIGHT)


# 在Canvas上繪製圖片
canvas1.create_image(0, 0, image=img1, anchor=tk.NW)
canvas2.create_image(0, 0, image=img2, anchor=tk.NW)


root.mainloop()
