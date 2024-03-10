import cv2
import tkinter as tk


# img1 = cv2.imread("r1.jpg")
# img2 = cv2.imread("r3.jpg")

def compare_screw_is_same_rule():

    img1 = cv2.imread("perfect_rule_screw.jpg")
    img2 = cv2.imread("be_detected_screw.jpg")


    # 將圖像調整為相同的大小
    img1 = cv2.resize(img1, (800, 600))
    img2 = cv2.resize(img2, (800, 600))

    # 將圖像轉換為灰度圖像
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)


    # 比較兩張圖像的差異
    diff = cv2.absdiff(gray1, gray2)

    resImg = cv2.absdiff(gray1, gray2)
    cv2.imshow("resImg ", resImg )
    cv2.waitKey(0)

    # 將差異圖像二值化
    thresh = cv2.threshold(diff, 100, 255, cv2.THRESH_BINARY)[1]

    # 腐蝕圖像，進一步消除差異
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    erode = cv2.erode(thresh, kernel)


    #判斷結果，如果 erode 為一個空圖像，則表示兩張圖像相同
    if cv2.countNonZero(erode) == 0:
        label_compare_text.config(text="兩張螺絲規格相同")
        print("兩張圖像相同")
    else:
        label_compare_text.config(text="兩張螺絲規格不同")
        print("兩張圖像不同")


# compare_screw_is_same_rule(img1,img2)