import tkinter as tk
from PIL import Image, ImageTk




def run():
    # 創建主視窗
    root = tk.Tk()
    root.title("顯示圖片")

    # 載入原始圖片
    original_image = Image.open("detected_screw.png")

    # 等比縮放圖片
    width, height = original_image.size
    if width > 800:
        scale = 800.0 / width
        width = int(width * scale)
        height = int(height * scale)
    if height > 600:
        scale = 600.0 / height
        width = int(width * scale)
        height = int(height * scale)
    resized_image = original_image.resize((width, height), Image.ANTIALIAS)

    # 再次縮小圖片
    new_width = int(width * 0.8)
    new_height = int(height * 0.8)
    resized_image = resized_image.resize((new_width, new_height), Image.ANTIALIAS)


    # 轉換圖片為Tkinter格式
    photo = ImageTk.PhotoImage(resized_image)

    # 創建Canvas小部件
    canvas = tk.Canvas(root, width=new_width, height=new_height)
    canvas.pack()

    # 在Canvas上繪製圖片
    canvas.create_image(0,0,image=photo, anchor=tk.NW)

    # 啟動主視窗事件迴圈
    root.mainloop()




