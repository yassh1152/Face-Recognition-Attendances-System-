from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np
import re

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x1080+0+0")
        self.root.title("Face Recognition System")

        t1 = Label(self.root, text="Train Data Set", font=("times new roman", 35, "bold"),
                   bg="white", fg="darkblue")
        t1.place(x=0, y=0, width=1530, height=55)

        imgtop = Image.open("D:\\Python\\Project\\image\\fo.jpg")
        imgtop = imgtop.resize((1530, 700))
        self.photoimage_top = ImageTk.PhotoImage(imgtop)

        l2 = Label(self.root, image=self.photoimage_top)
        l2.place(x=0, y=55, width=1530, height=700)

        # button
        b1_1 = Button(self.root, text="Train Data", command=self.train_classifier, cursor="hand2",
                      font=("Raleway", 15, "bold"), bg="red", fg="white")
        b1_1.place(x=0, y=700, width=1530, height=60)

        # imgbot = Image.open("D:\\Python\\Project\\image\\photo.jpeg")
        # imgbot = imgbot.resize((1530, 325))
        # self.photoimage_bot = ImageTk.PhotoImage(imgbot)

        # l2 = Label(self.root, image=self.photoimage_bot)
        # l2.place(x=0, y=440, width=1530, height=325)

    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert("L")  # Gray Scale Image
            imgnp = np.array(img, 'uint8')  # datatype
            # Extract numeric part from the file name using regular expressions
            id_match = re.search(r'\d+', os.path.splitext(os.path.basename(image))[0])

            if id_match:
                id = int(id_match.group())
                faces.append(imgnp)
                ids.append(id)
                cv2.imshow("Training", imgnp)
                cv2.waitKey(500)  # Add a delay of 500 milliseconds (adjust as needed)
                if cv2.waitKey(1) & 0xFF == 13:
                    break

        id = np.array(ids)

        # ======================Train The Classifier=================
        classifier_folder = "classifier"

        # Check if the "classifier" folder exists, and create it if not
        if not os.path.exists(classifier_folder):
            os.makedirs(classifier_folder)

        classifier_path = os.path.join(classifier_folder, "classifier.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, id)
        clf.write(classifier_path)
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training DataSet Completed")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
