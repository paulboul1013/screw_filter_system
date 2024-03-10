import cv2
import csv
import re

picture_height=900
picture_width=780
pic_path="be_detected_screw.jpg"


def cover_rule_screw():

    read_cover_pic="s.jpg" #按照規格畫線，確認是否為同樣規格螺絲


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
    print("cover_rules_screw_path:"+pic_path)


    # 顯示圖像
    cv2.namedWindow(pic_path, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(pic_path, picture_height, picture_width)
    cv2.imshow(pic_path, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# cover_rule_screw()