from tkinter import *
from PIL import Image, ImageTk
import cv2
import mysql.connector
from datetime import datetime
import os
import re
import numpy as np

class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x1080+0+0")
        self.root.title("Face Recognition System")
    
        t1 = Label(self.root, text="Face Recognition", font=("times new roman", 35, "bold"),
               bg="white", fg="darkblue")
        t1.place(x=0, y=0, width=1530, height=55)

        # First image
        imgtop = Image.open("D:\\Python\\Project\\image\\fd.png")
        imgtop = imgtop.resize((1550,710))
        self.photoimage_top = ImageTk.PhotoImage(imgtop)

        self.l2 = Label(self.root, image=self.photoimage_top)
        self.l2.place(x=0, y=55, width=1550, height=710)

        # # Second image
        # imgbot = Image.open("D:\\Python\\Project\\image\\fc2.jpg")
        # imgbot = imgbot.resize((950, 700))
        # self.photoimage_bot = ImageTk.PhotoImage(imgbot)

        # self.l2_bot = Label(self.root, image=self.photoimage_bot)
        # self.l2_bot.place(x=700, y=55, width=950, height=700)

        # Button
        b1_1 = Button(self.l2, text="Face Recognition", command=self.recognize, cursor="hand2",
                  font=("Raleway", 15, "bold"), bg="red", fg="white")
        b1_1.place(x=680, y=620, width=200, height=40)

        # Folder path for images
        self.folder_path = "D:\Python\Project\data"
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

        # Load images from the folder
        self.images, self.labels = self.load_images_from_folder()

        # LBPH Face Recognizer
        self.clf = cv2.face.LBPHFaceRecognizer_create()

        # Initialize videocap object
        self.videocap = cv2.VideoCapture(0)  # Change the argument to the camera index if necessary

        # Initialize faceCascade
        self.faceCascade = cv2.CascadeClassifier("D:\\Python\\Project\\Face Recognition System\\haarcascade_frontalface_default.xml")


        # Convert labels to NumPy array
        self.labels = np.array(self.labels)

        # Train the recognizer
        self.clf.train(self.images, self.labels)

    def load_images_from_folder(self):
        images = []
        labels = []
        for filename in os.listdir(self.folder_path):
            path = os.path.join(self.folder_path, filename)
            img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            images.append(img)

            # Extract numeric part from the filename using regular expression
            label_match = re.search(r'\d+', filename)
            if label_match:
                label = int(label_match.group())
                labels.append(label)
            else:
                print(f"Invalid filename format: {filename}")
        return images, labels

    def markattendance(self, id, name, department, rollno):
        try:
            with open("Attendances.csv", "a", newline="\n") as f:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtstring = now.strftime("%H:%M:%S")
                f.writelines(f"\n{id},{name},{department},{rollno},{dtstring},{d1},Present")
        except Exception as e:
            print(f"Error marking attendance: {e}")

    def draw_boundary(self, img, scaleFactor, minNeighbors, color, text):
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = self.faceCascade.detectMultiScale(gray_img, scaleFactor, minNeighbors)
        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            id, predict = self.clf.predict(gray_img[y:y + h, x:x + w])
            confidence = int((100 * (1 - predict / 300)))

            if confidence > 60:  # Check confidence level
                result = self.get_student_details(id)
                if result:
                    id, name, department, rollno = result
                    cv2.putText(img, f"ID: {id}", (x, y - 85), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {name}", (x, y - 60), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department: {department}", (x, y - 35), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll No: {rollno}", (x, y + h - 230), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.markattendance(id, name, department, rollno)
                else:
                    cv2.putText(img, "Details not found", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y + h + 25), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
            
           


    def get_student_details(self, student_id):
        try:
            conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="yash",
            database="python_project",
            )
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT id, name, department, rollno FROM student WHERE id = %s", (student_id,))
            result = my_cursor.fetchone()
            return result
        except Exception as e:
            print(f"Error Fetching Student Details: {e}")
        finally:
            conn.close()

    def recognize(self):
        ret, img = self.videocap.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        self.draw_boundary(img,1.1, 10, (255, 255, 255), "Face")

        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        self.l2.img = img
        self.l2.config(image=img)

        if cv2.waitKey(1) == 13:
            self.videocap.release()
            cv2.destroyAllWindows()
            return

        # Call the recognize function again after a delay
        self.root.after(10, self.recognize)

if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognition(root)
    root.mainloop()

