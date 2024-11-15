import cv2
import numpy as np
import time
import HandTracking as ht
import autopy
from tkinter import *
from PIL import ImageTk, Image
import pyautogui


class second(Toplevel):
    def __init__(self, window):
        self.window = window
        self.window.resizable(False, False)
        self.window.title('FEROUS')
        height = 500
        width = 511
        frame = Frame(window, width=511, height=500, bg="#010516")
        frame.place(x=0, y=0)
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.window.overrideredirect(1)
        background = Image.open('bg.jpg')
        background.save('new-image.png')
        photo = ImageTk.PhotoImage(background)
        bg_Label1 = Label(frame, image=photo)
        bg_Label1.image = photo
        bg_Label1.place(x=40, y=50)

        wlc_label = Label(frame, text="CREATE A USERNAME", font=('calisto mt', 13), bg='#010516', fg='white')
        wlc_label.place(x=40, y=20)
        wlc_label_entry = Entry(frame, font=('calisto mt', 13), fg='#010516', bg='white')
        wlc_label_entry.place(x=270, y=20)
        wlc_label.btn = Button(frame, width=10, font=('calisto mt', 13), text='ENTER', bg='#010516', fg='white',
                               command=lambda: ENTER())
        wlc_label.btn.place(x=350, y=465)

        def ENTER():
            if wlc_label_entry.get() != "":
                wlc_label.place_forget()
                wlc_label_entry.place_forget()
                wlc_label.btn.place_forget()
                tutorial_btn = Button(frame, width=10, font=('calisto mt', 13), text='TUTORIAL', bg='#010516',
                                      fg='white',
                                      command=lambda: TUTORIAL())
                tutorial_btn.place(x=350, y=10)
                wlc_label1 = Label(frame, text=f"Welcome {wlc_label_entry.get()}", font=('calisto mt', 13),
                                   bg='#010516', fg='white')
                wlc_label1.place(x=40, y=20)
                start = Label(text="To start >>>", font=('calisto mt', 13), bg='#010516', fg='white')
                start.place(x=40, y=465)
                START_btn = Button(frame, width=10, font=('calisto mt', 13), text='START', bg='#010516', fg='white',
                                   command=lambda: start())
                START_btn.place(x=350, y=465)

            def TUTORIAL():
                bg_Label1.place_forget()
                tutorial_btn.place_forget()
                wlc_label1.place_forget()

                tutorial = Label(frame, text="The Vision mouse 2023 is a virtual mouse that uses the \n help of "
                                             "the camera ,which reads the movement of the users finger \ninorder to "
                                             "virtually control the mouse\n \nit requires the index finger to control "
                                             "the mouse"
                                             "\n \n To Click: Tap the middle finger on the index then\n \n"
                                             "put the the middle finger down\n \n"
                                             "To Right Click: Tap the thumb on the index finger then put it down."
                                             "\n \n To Double Click: Tap the middle finger on the index finger"
                                             "\n \n twice then put the index finger down.\n \n To Move Right : Move "
                                             "finger right.\n"
                                             " \n To Move Left: Move "
                                             "finger left.\n \n To Move Up: Move finger up.\n \n To Move down: Move "
                                             "finger down",
                                 font=('calisto mt', 11), fg='white', bg="#010516")
                tutorial.place(x=25, y=60)
                tutorial1 = Label(frame, text="TUTORIAL", font=('calisto mt', 20), fg='white', bg="#010516")
                tutorial1.place(x=170, y=20)

            def mouse():
                ### Variables Declaration
                pTime = 0  # Used to calculate frame rate
                width = 640  # Width of Camera
                height = 480  # Height of Camera
                frameR = 100  # Frame Rate
                smoothening = 8  # Smoothening Factor
                prev_x, prev_y = 0, 0  # Previous coordinates
                curr_x, curr_y = 0, 0  # Current coordinates

                cap = cv2.VideoCapture(0)  # Getting video feed from the webcam
                cap.set(3, width)  # Adjusting size of camera
                cap.set(4, height)

                detector = ht.handDetector(maxHands=1)  # Detecting one hand at max
                screen_width, screen_height = autopy.screen.size()  # Getting the screen size
                while True:
                    success, img = cap.read()
                    img = detector.findHands(img)  # Finding the hand
                    lmlist, bbox = detector.findPosition(img)  # Getting position of hand

                    if len(lmlist) != 0:
                        x4, y4 = lmlist[4][1:]
                        x1, y1 = lmlist[8][1:]
                        x2, y2 = lmlist[12][1:]

                        fingers = detector.fingersUp()  # Checking if fingers are upwards
                        cv2.rectangle(img, (frameR, frameR), (width - frameR, height - frameR), (255, 0, 255),
                                      2)  # Creating boundary box
                        if fingers[1] == 1 and fingers[2] == 0:  # If fore finger is up and middle finger is down
                            x3 = np.interp(x1, (frameR, width - frameR), (0, screen_width))
                            y3 = np.interp(y1, (frameR, height - frameR), (0, screen_height))

                            curr_x = prev_x + (x3 - prev_x) / smoothening
                            curr_y = prev_y + (y3 - prev_y) / smoothening

                            autopy.mouse.move(screen_width - curr_x, curr_y)  # Moving the cursor
                            cv2.circle(img, (x1, y1), 7, (255, 0, 255), cv2.FILLED)
                            prev_x, prev_y = curr_x, curr_y

                        if fingers[1] == 1 and fingers[2] == 1:  # If fore finger & middle finger both are up
                            length, img, lineInfo = detector.findDistance(8, 12, img)

                            if length < 40:  # If both fingers are really close to each other
                                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                                autopy.mouse.click()  # Perform Click
                        if fingers[0] == 1 and fingers[1] == 1:
                            length1, img, lineinfo = detector.findDistance(4, 8, img)



                    cTime = time.time()
                    fps = 1 / (cTime - pTime)
                    pTime = cTime
                    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
                    cv2.imshow("Image", img)  # to run camera
                    cv2.waitKey(1)  # to run camera

            def start():
                mouse()


def page1():
    window = Tk()
    second(window)
    window.mainloop()


if __name__ == '__main__':
    page1()
