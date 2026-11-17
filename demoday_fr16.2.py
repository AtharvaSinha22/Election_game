import cv2
import tkinter as tk
from PIL import Image, ImageTk
import threading
import time

class WebcamApp:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)

        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        self.canvas = tk.Canvas(window, width=self.vid.get(cv2.CAP_PROP_FRAME_WIDTH), height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.pack()

        self.btn_capture = tk.Button(window, text="Capture", width=10, command=self.capture_image)
        self.btn_capture.pack(pady=10)

        self.delay = 1000 // int(self.vid.get(cv2.CAP_PROP_FPS))
        self.update()

    def update(self):
        ret, frame = self.vid.read()
        if ret:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        self.window.after(self.delay, self.update)

    def capture_image(self):
        self.countdown(3)  # You can change the countdown time here

    def countdown(self, count):
        if count > 0:
            self.btn_capture.config(text=str(count))
            self.window.after(1000, self.countdown, count - 1)
        else:
            ret, frame = self.vid.read()
            if ret:
                image_filename = "captured_image.jpg"
                cv2.imwrite(image_filename, frame)
                print("Image captured and saved as", image_filename)
                self.btn_capture.config(text="Capture")
            else:
                print("Failed to capture image.")

def start_webcam_app():
    root = tk.Tk()
    app = WebcamApp(root, "Webcam Image Capture App")
    root.mainloop()

if __name__ == "__main__":
    start_webcam_app()
