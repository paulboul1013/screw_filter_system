import cv2
import math
import csv
import numpy as np

points = []

pic_path="s.jpg"

pixel_to_cm_parameter=0.11

picture_height=900
picture_width=780

#範例 screw_4
#牙距:0.1cm  螺紋長度:2.8cm 外徑0.4cm


detect_count=0
pitch=0
thread_length=0
thread_width=0


# 畫偵測範圍方框
start_point = (50, 40)
end_point = (600, 450)
color = (0, 255, 0) # green color
thickness = 3


def click_event(event, x, y, flags, param):
    global points
    global detect_count
    global pitch
    global thread_length
    global thread_width
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        
        print(points)


        if len(points) == 2:
            dist = math.sqrt((points[1][0] - points[0][0]) ** 2 + (points[1][1] - points[0][1]) ** 2)
            #print("距離: {:.2f} 像素 ".format(dist))
            #print("距離: {:.2f} 公分".format((dist / 100)*pixel_to_cm_parameter))
            
            key = cv2.waitKey(1)

            cv2.line(img, points[0], points[1], (0, 255, 0), 20)
            cv2.imwrite("perfect_rule_screw.jpg", img)

            if key==ord('d'):
                if detect_count==0:
                    pass
                detect_count-=1

            if detect_count==0:
                with open('screw_data_point.csv', 'w', newline='') as file:
                    writer = csv.writer(file)

                    # 類別
                    writer.writerow(['螺絲牙距_A點','螺絲牙距_B點'])

                    # 寫入數據
                    writer.writerow([points[0], points[1]])

                pitch="{:.2f}".format((dist / 100)*pixel_to_cm_parameter)
                print("螺絲牙距:"+pitch+"cm")
                detect_count+=1

            elif detect_count==1:
                with open('screw_data_point_2.csv', 'w', newline='') as file:
                    writer = csv.writer(file)

                    # 類別
                    writer.writerow(['螺紋長度_A點','螺紋長度_B點'])

                    # 寫入數據
                    writer.writerow([points[0], points[1]])



                thread_length="{:.2f}".format((dist / 100)*pixel_to_cm_parameter)
                print("螺紋長度:"+thread_length+"cm")
                detect_count+=1

            elif detect_count==2:

                with open('screw_data_point_3.csv', 'w', newline='') as file:
                    writer = csv.writer(file)

                    # 類別
                    writer.writerow(['螺紋寬度_A點','螺紋寬度_B點'])

                    # 寫入數據
                    writer.writerow([points[0], points[1]])


                thread_width="{:.2f}".format((dist / 100)*pixel_to_cm_parameter)
                # print("螺紋寬度:"+thread_width+"cm")
                detect_count+=1
                
            elif detect_count==3:
                return


            """if points[0][0]>=250 and points[1][0]<=400 and points[0][1]>=40 and points[1][1]<=450: # 偵測方塊位置
                # 用pixel判斷是否等於規定的長度
                if float(pitch) >=0.1 and float(pitch) <=0.2:
                    print("deteced")"""
            

            


            with open('screw_data.csv', 'w', newline='') as file:
                writer = csv.writer(file)

                # 類別
                writer.writerow(['螺絲牙距', '螺紋長度', '螺紋寬度'])

                # 寫入數據
                writer.writerow([pitch,thread_length,thread_width])
                

            
            cv2.resizeWindow(pic_path, picture_height, picture_width)
            cv2.imshow(pic_path, img)
            
            points = []


img = cv2.imread(pic_path)
#img = cv2.rectangle(img, start_point, end_point, color, thickness)

thread_length_color=(255, 0, 0) 
start_point_thread_length=(250, 40)
end_point_thread_length=(400, 450)
#img = cv2.rectangle(img, start_point_thread_length, end_point_thread_length, thread_length_color, thickness)



global detect_rule_screw_count
while True:

    cv2.namedWindow(pic_path, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(pic_path, picture_height, picture_width)
    cv2.imshow(pic_path, img)

    detect_rule_screw_count=0

    key = cv2.waitKey(1)

    if key == ord('q'):
        break



    if detect_rule_screw_count==0:
        cv2.setMouseCallback(pic_path, click_event)
        detect_rule_screw_count+=1

   
    #cv2.waitKey(0)



cv2.destroyAllWindows()

