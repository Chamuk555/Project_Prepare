from xml.etree.ElementInclude import default_loader
import cv2 #นำเข้า OpenCV ด้วยชื่อ cv2
import mediapipe as mp #นำเข้าMediapipe ด้วยชื่อ mp
import pyautogui

webcam = cv2.VideoCapture(1) #คำสั่งระบุกล้องที่ต้องการใช้งาน#นำค่าที่อ่านได้จากกล้อง มาเก็บไว้ในตัวแปร image
mp_hands = mp.solutions.hands #คำสั่งเตรียมข้อมูลสำหรับตรวจจับมือ และนำไปเก็บไว้ในตัวแปร mp_hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

while True:
  success, image = webcam.read() #ให้กล้องถ่ายรูปมาเรื่อยๆ โดยจะเก็บไว้ที่ตัวแปร success และ image
  image_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
  results = hands.process(image_rgb)
 
  print(results.multi_hand_landmarks)
 
  if results.multi_hand_landmarks:
    for landmark in results.multi_hand_landmarks:
      mp_draw.draw_landmarks(image, landmark, mp_hands.HAND_CONNECTIONS) #ให้แสดงผลรูปภาพแต่ละรูปมาต่อๆกันจนเป็นวิดีโอ และแสดงจุดแลนมาร์คแต่ละจุดบนฝ่ามือ และวาดเส้นเชื่อมจุด
    cv2.imshow("Hand Tracking",image)
    cv2.waitKey(1)