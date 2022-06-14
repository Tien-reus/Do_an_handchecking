from tkinter import *
import pygame
from cv2 import cv2
import time
import os
import hand as htm
from PIL import ImageTk, Image
from tkinter import messagebox

# import playsound

main = Tk()
main.title("Main chinh")
main.geometry("900x700")
main.resizable(False,False)
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        load_logo = Image.open("logo.jpg")
        render_logo = ImageTk.PhotoImage(load_logo)
        img_logo = Label(self, image=render_logo)
        img_logo.image = render_logo
        img_logo.place(x=690, y=10)

        load_hand = Image.open("hand.jpg")
        render_hand = ImageTk.PhotoImage(load_hand)
        img_hand = Label(self, image=render_hand)
        img_hand.image = render_hand
        img_hand.place(x=50, y=180)

        LB_tt = Label(main, text="NHAN DIEN ANH BANG NGON TAY", font="Calibri 25")
        LB_tt.place(x=50, y=20)
        #thong tin sv
        Nam = Label(main, text="Nguyễn Chí Nam : 01234567", font="Calibri 15")
        Nam.place(x=50,y=80)
        Hai = Label(main, text="Nguyễn Xuân Hải : 01234567", font="Calibri 15")
        Hai.place(x=50, y=110)
        Tien = Label(main, text="Nguyễn Văn Tiến : 01234567", font="Calibri 15")
        Tien.place(x=50, y=140)
        #guide
        LB_gd = Label(main,text="HƯỚNG DẪN",font="Calibri 15 bold").place(x=710,y=230)
        LB_nb1 = Label(main,text="MỞ ALBUM ẢNH",font="Calibri 12").place(x=710,y=280)
        LB_nb2 = Label(main,text="MỞ LIST NHẠC",font="Calibri 12").place(x=710,y=320)
        LB_nb3 = Label(main,text="CHƯA BIẾT",font="Calibri 12").place(x=710,y=360)

        #Bt_check = Button(main, text="CHECK", font="Calibri 20 bold",background="skyblue").place(x=735, y=500)

def cmd():
    pTime = 0
    cap = cv2.VideoCapture(0)

    FolderPath = "Fingers"
    lst = os.listdir(FolderPath)
    lst_2 = []
    for i in lst:
        image = cv2.imread(f"{FolderPath}/{i}")
        print(f"{FolderPath}/{i}")
        lst_2.append(image)

    detector = htm.handDetector(detectionCon=1)

    fingerid = [4, 8, 12, 16, 20]
    while True:
        ret, frame = cap.read()
        frame = detector.findHands(frame)
        lmList = detector.findPosition(frame, draw=False)
        print(lmList)

        if len(lmList) != 0:
            fingers = []
            # ban tay trai
            # viet cho ngon cai so sanh chieu rong
            if lmList[fingerid[0]][1] < lmList[fingerid[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

                # viet ngon dai so sanh chieu cao
            for id in range(1, 5):
                if lmList[fingerid[id]][2] < lmList[fingerid[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            print(fingers)
            songontay = fingers.count(1)
            print(songontay)

            h, w, c = lst_2[songontay - 1].shape
            frame[0:h, 0:w] = lst_2[songontay - 1]

            # mo_anh
            # hàm mở ảnh

            if songontay == 1:
                messagebox.showinfo("SO 1","Ban vua yeu cau so 1")
                root_img = Tk()
                root_img.title("ALBUM")
                root_img.geometry("400x400")


                def seen():
                    img = cv2.imread('187161.jpg', 1)  # ham doc anh
                    img = cv2.resize(img, (400, 200))
                    # img = cv2.resize(img,(0,0),fx=0.3, fy=0.3)
                    cv2.imshow("hien thi", img)  # lenh show anh
                    time.sleep(5)
                    k = cv2.waitKey()
                my_img = Button(root_img, text="SEEN", font=("Helvetica", 32), command=seen)
                my_img.pack(pady=20)
                root_img.mainloop()

            
            elif songontay == 2:
                messagebox.showinfo("SO 2","Ban vua yeu cau so 2")
                root = Tk()
                root.title("MUSIC MP3")
                root.geometry("400x400")
                pygame.mixer.init()
                def play1():
                    pygame.mixer.music.load("mp3/msc.mp3")
                    pygame.mixer.music.play(loops=0)
                def play2():
                    pygame.mixer.music.load("mp3/bboom.mp3")
                    pygame.mixer.music.play(loops=0)
                def play3():
                    pygame.mixer.music.load("mp3/2mbetter.mp3")
                    pygame.mixer.music.play(loops=0)

                def stop():
                    pygame.mixer.music.stop()


                my_bt1 = Button(root, text="EM ko phai thuy kieu", font=("Helvetica", 15), command=play1)
                my_bt1.pack(pady=10)
                my_bt2 = Button(root, text="Bboom Bboom", font=("Helvetica", 15), command=play2)
                my_bt2.pack(pady=10)
                my_bt3 = Button(root, text="2 Phut Hon", font=("Helvetica", 15), command=play3)
                my_bt3.pack(pady=10)
                stop_bt = Button(root, text="STOP", command=stop)
                stop_bt.pack(pady=20)
                bt_quit_nb2 = Button(root, text="Quit",command=root.quit)
                bt_quit_nb2.pack(pady=20)
                root.mainloop()

            # if songontay == 3:
            #     root_rd = Tk()
            #     root_rd.title("ALL ALBUM")
            #     # root.geometry("400x600")
            #     # root.iconbitmap()
            #
            #     my_img1 = ImageTk.PhotoImage(Image.open("Fingerss/gaoden.jpg"))
            #     my_img2 = ImageTk.PhotoImage(Image.open("Fingerss/gaodo.jpg"))
            #     my_img3 = ImageTk.PhotoImage(Image.open("Fingerss/guku.jpg"))
            #     my_img4 = ImageTk.PhotoImage(Image.open("Fingerss/son.png"))
            #     my_img5 = ImageTk.PhotoImage(Image.open("Fingerss/sonku.jpg"))
            #
            #     image_lst = [my_img1, my_img2, my_img3, my_img4, my_img5]
            #
            #     my_lb = Label(image=my_img1)
            #     my_lb.grid(row=0, column=0, columnspan=3)
            #
            #
            #     def forward(image_number):
            #         global my_lb
            #         global bt_forward
            #         global bt_back
            #
            #         my_lb.grid_forget()
            #         my_lb = Label(image=image_lst[image_number - 1])
            #         bt_forward = Button(root_rd, text=">>", command=lambda: forward(image_number + 1))
            #         bt_back = Button(root_rd, text="<<", command=lambda: back(image_number - 1))
            #         my_lb.grid(row=0, column=0, columnspan=3)
            #
            #         if image_number == 5:
            #             bt_forward = Button(root_rd, text=">>", state=DISABLED)
            #
            #         bt_back.grid(row=1, column=0)
            #         # bt_exit.grid(row=1, column=1)
            #         bt_forward.grid(row=1, column=2)
            #
            #
            #     def back(image_number):
            #         global my_lb
            #         global bt_forward
            #         global bt_back
            #
            #         my_lb.grid_forget()
            #         my_lb = Label(image=image_lst[image_number - 1])
            #         bt_forward = Button(root_rd, text=">>", command=lambda: forward(image_number + 1))
            #         bt_back = Button(root_rd, text="<<", command=lambda: back(image_number - 1))
            #         my_lb.grid(row=0, column=0, columnspan=3)
            #
            #         if image_number == 1:
            #             bt_back = Button(root_rd, text="<<", state=DISABLED)
            #
            #         bt_back.grid(row=1, column=0)
            #         # bt_exit.grid(row=1, column=1)
            #         bt_forward.grid(row=1, column=2)
            #
            #
            #     bt_back = Button(root_rd, text="<<", command=back, state=DISABLED)
            #     bt_exit = Button(root_rd, text="EXIT", command=root_rd.quit)
            #     bt_forward = Button(root_rd, text=">>", command=lambda: forward(2))
            #
            #     bt_back.grid(row=1, column=0)
            #     bt_exit.grid(row=1, column=1)
            #     bt_forward.grid(row=1, column=2)
            #
            #     root_rd.mainloop()

            # ve hnc
            cv2.rectangle(frame, (0, 150), (200, 400), (0, 255, 0), -1)
            cv2.putText(frame, str(songontay), (10, 390), cv2.FONT_HERSHEY_PLAIN, 20, (255, 0, 0), 5)
        # viet fps
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        # print(type(fps))
        # show fps
        cv2.putText(frame, f"FPS : {int(fps)}", (150, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        cv2.imshow("dem ngon tay ", frame)

        if cv2.waitKey(1) == ord("q"):
            quit()

    cap.release()  # giai phong camera
    #cv2.destroyAllWindows()  # thoat tat ca
    cv2.destroyWindow(frame)


app = Window(main)
Bt_check = Button(main, text="CHECK", font="Calibri 20 bold",background="skyblue",command=cmd).place(x=735, y=500)
Bt_quit = Button(main, text="QUIT", font="Calibri 20 bold",background="skyblue",command=quit).place(x=735, y=580)

main.mainloop()