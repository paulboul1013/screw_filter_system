import tkinter as tk
import cv2
from PIL import Image, ImageTk
from rembg import remove




#照片去背
def image_white_background(input_path,output_path):   
             
    input=Image.open(input_path)
    output=remove(input)
    output.save(output_path)


class App:
    def __init__(self, window, video_source=0):
        self.window = window
        self.window.title("OpenCV 拍照")
        window.config(bg="#323232") #背景顏色
        self.video_source = video_source
        self.snapshot_interval = 0 # 拍照間隔時間



        #顯示中間輸入文字
        show_center_side_text=tk.Label(fg="black",text="輸入自動拍照的間隔時間")
        show_center_side_text.pack(side=tk.TOP,anchor="center")



        #創建輸入時間框
        self.entry = tk.Entry(window)
        self.entry.insert(0, "0")
        self.entry.pack(side=tk.TOP,anchor="center", expand=False)


        self.input_the_interval_time= tk.Frame(window)
        self.input_the_interval_time.pack(side=tk.TOP)

        input_the_interval_time_btn=tk.Button(self.input_the_interval_time,text="輸入按鈕",command=self.input_time)
        input_the_interval_time_btn.pack(side=tk.TOP,anchor="s")

    

        #顯示右邊picture文字
        show_right_side_text=tk.Label(fg="black",text="拍照畫面")
        show_right_side_text.pack(side=tk.TOP,anchor="se")
        

        #顯示左邊camera文字
        show_left_side_text=tk.Label(fg="black",text="拍攝鏡頭畫面")
        show_left_side_text.pack(side=tk.TOP,anchor="nw")


        # 創建用于顯示camera
        self.canvas = tk.Canvas(window, width=640, height=480)
        self.canvas.pack(side=tk.LEFT,anchor="sw")

        
        

        #暫停按鈕
        self.stop_take_picture=tk.Frame(window)
        self.stop_take_picture.pack(side=tk.LEFT)
        
        #一般拍照按鈕
        self.normal_controls_take_picture = tk.Frame(window)
        self.normal_controls_take_picture.pack(side=tk.LEFT)


        #自動拍照按鈕
        self.controls_take_picture = tk.Frame(window)
        self.controls_take_picture.pack(side=tk.LEFT)

        

        #照片標籤
        self.take_picture=tk.Frame(window)
        self.take_picture.pack(side=tk.RIGHT)
        

        # 創建顯示照片的標籤
        self.photo_label = tk.Label(self.take_picture)
        self.photo_label.pack(side=tk.BOTTOM)


        
        #創建一般拍照按鈕
        self.btn_snapshot= tk.Button(self.normal_controls_take_picture, text="拍照", command=self.sanpshot)
        self.btn_snapshot.pack(side=tk.LEFT, anchor=tk.NW, expand=False)


        # 創建自動拍照按钮
        self.btn_snapshot_auto = tk.Button(self.controls_take_picture, text="自動拍照", command=self.auto_snapshot)
        self.btn_snapshot_auto.pack(side=tk.LEFT, anchor=tk.NW, expand=False)

        #創建暫停按鈕
        self.stop_snapshot_btn= tk.Button(self.stop_take_picture, text="暫停", command=self.stop_sanpshot)
        self.stop_snapshot_btn.pack(side=tk.BOTTOM,anchor=tk.S,expand=False)


        
        # 打開鏡頭
        self.cap = cv2.VideoCapture(self.video_source)
        
        # 一直抓取鏡頭影像
        self.update()



    #偵測圖片螺絲的頭部直徑
    def head_outer_diameter(self,input_image):

        #pic去背
        image_white_background(input_image,'out.png')

        #pixels轉換直徑變數
        pixels_to_diamter_parameter=0.001000

        #鏡頭離平面距離
        camera_and_ground_distance=12.7

        # Read the image
        #img = cv2.imread('5.png')
        img=cv2.imread('out.png')

        # Resize the image to double its size
        img = cv2.resize(img, (0,0), fx=2, fy=2)


        # Convert the image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Apply a Gaussian blur to reduce noise
        blur = cv2.GaussianBlur(gray, (5, 5), 0)

        # Detect edges using the Canny algorithm
        edges = cv2.Canny(blur, 50, 150)

        # Find contours in the image
        contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Find the contour with the largest area
        max_contour = max(contours, key=cv2.contourArea)

        # Get the bounding rectangle of the contour
        x, y, w, h = cv2.boundingRect(max_contour)

        # Calculate the diameter of the screw head
        diameter = w

        #print(diameter)

        diameter_transfer_to_cm=diameter*pixels_to_diamter_parameter*camera_and_ground_distance #pixels轉換真實直徑，有一點誤差，也會因為照片和鏡頭距離的大小影響pixels


        diameter_str = f'{diameter_transfer_to_cm:.2f}'


        # Draw the bounding rectangle on the original image
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Add text to the image with the diameter
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, f'Diameter: {diameter_str} cm', (50, 50), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

        cv2.imwrite("detected_screw.png", img)

        self.show_snapshot("detected_screw.png")


        #cv2.imshow('detected_screw', img)



    def input_time(self):
        num = int(self.entry.get())
        self.snapshot_interval = num # 輸入拍照間隔時間
        print("間隔時間:"+str(self.snapshot_interval))
    
    def update(self):
        # 讀取影像
        ret, frame = self.cap.read()
        
        if ret:
            #將圖像轉換tkinter photoImage格式
            self.photo = self.convert_frame(frame)
            
            #在畫布畫布顯示
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        
        #20毫秒毫秒更新一次
        self.window.after(20, self.update)
    
    def convert_frame(self, frame):
        
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(rgb_frame)
        photo = ImageTk.PhotoImage(image=pil_img)
        return photo
    

    #一般拍照
    def sanpshot(self):
        ret, frame = self.cap.read()
        if ret:
            
            cv2.imwrite("snapshot.png", frame)
            self.head_outer_diameter("snapshot.png")
            print("拍照成功！")
            #self.show_snapshot("snapshot.png")
        
    
    def auto_snapshot(self):
        print(self.snapshot_interval)
        if self.snapshot_interval > 0:
            print("自動拍照開啟！")
            ret, frame = self.cap.read()
            if ret:
                #一般拍照圖片
                cv2.imwrite("snapshot.png", frame)
                self.head_outer_diameter("snapshot.png")
                
               
            
            # 3秒鐘調秒鐘調用一次
            self.snapshot_state=self.window.after(self.snapshot_interval * 1000, self.auto_snapshot)
        
        else:
            print("請輸入>0秒的間隔時間")


    def stop_sanpshot(self):
        self.window.after_cancel(self.snapshot_state)
        print("暫停自動拍照!")

                
    
    def show_snapshot(self, file_path):
        # 打開拍照照片
        img = Image.open(file_path)

        # 縮小照片
        max_width = 640
        max_height = 480
        width, height = img.size
        if width > max_width or height > max_height:
            if width / max_width > height / max_height:
                new_width = max_width
                new_height = int(height / (width / max_width))
            else:
                new_height = max_height
                new_width = int(width / (height / max_height))
            img = img.resize((new_width, new_height), Image.ANTIALIAS)


        photo = ImageTk.PhotoImage(img)
        self.photo_label.configure(image=photo)
        self.photo_label.image = photo


    

    
    def __del__(self):
        # 關閉影片
        if self.cap.isOpened():
            self.cap.release()



target=App(tk.Tk()).window.mainloop()


    


