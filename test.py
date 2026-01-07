import cv2
import mediapipe as mp
import pyautogui
import math

# Setup
cam_w, cam_h = 640, 480 # Camera size
frame_reduction = 100 # Limit the movement area 
smoothening = 5 # smoothing factor (The reaction speed of the mouse)

# Mediapipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)
mp_draw = mp.solutions.drawing_utils

screen_w, screen_h = pyautogui.size() # take the size of the screen
 
cap = cv2.VideoCapture(0) # start the camera
cap.set(3, cam_w) # set width
cap.set(4, cam_h) # set height

plocX, plocY = 0, 0  # Tọa độ cũ (Previous Location) để làm mượt
clocX, clocY = 0, 0  # Tọa độ hiện tại (Current Location)

print("Mouse is using. Bring your thumb and index finger together toClick.")

while True:
    success, img = cap.read()
    if not success: break
    
    # Find hand
    img = cv2.flip(img, 1) # Flip the image horizontally
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Convert to RGB
    results = hands.process(img_rgb) # Process the RGB image to find hands
    
    # Draw the boundary box 
    cv2.rectangle(img, (frame_reduction, frame_reduction), (cam_w - frame_reduction, cam_h - frame_reduction), 
                  (255, 0, 255), 2)

    if results.multi_hand_landmarks:
        for hand_lms in results.multi_hand_landmarks:
            lmList = [] # List to hold all landmarks's positions

            # Get the landmark positions and convert to pixel values
            for id, lm in enumerate(hand_lms.landmark): 
                h, w, c = img.shape # height, width, channel
                cx, cy = int(lm.x * w), int(lm.y * h) # Convert the landmark coordinates to pixel values
                lmList.append([id, cx, cy]) 

            if len(lmList) != 0: # make sure the list is not empty
                x1, y1 = lmList[8][1], lmList[8][2] # take the landmark of the index finger
                
                # Convert from  (Interpolation)
                # Make sure the coordinates are within the frame reduction area
                # Scale formula: take the landmark position minus the frame reduction, 
                # calculate the width/ height of the reduced area
                # devide by that calculation to get the ratio, then multiply by screen size to get the scaled position
                x3 = (x1 - frame_reduction) / (cam_w - 2 * frame_reduction) * screen_w 
                y3 = (y1 - frame_reduction) / (cam_h - 2 * frame_reduction) * screen_h  
                
                # Smoothen values
                clocX = plocX + (x3 - plocX) / smoothening
                clocY = plocY + (y3 - plocY) / smoothening
                
                # Move mouse 
                try:
                    pyautogui.moveTo(clocX, clocY) # move the mouse to the new position
                except:
                    pass # Mouse out of screen bounds

                plocX, plocY = clocX, clocY # Update the previous location
                cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED) # Draw a circle at the index finger tip

                # Click the mouse if the distance between index finger and thumb is close 
                x2, y2 = lmList[4][1], lmList[4][2] # take the landmark of the thumb tip
                
                length = math.hypot(x2 - x1, y2 - y1) # Calculate the distance between two points
                
                # if the distance is less than 30 pixeles, click
                if length < 30:
                    cv2.circle(img, (x1, y1), 10, (0, 255, 0), cv2.FILLED) # Change the circle color to green
                    pyautogui.click() # Click 
                    print("Click!")

            mp_draw.draw_landmarks(img, hand_lms, mp_hands.HAND_CONNECTIONS) # Draw hand landmarks

    cv2.imshow("Virtual Mouse", img) # Show the image
    if cv2.waitKey(1) & 0xFF == ord('q'): # press q to exit
        break

cap.release()
cv2.destroyAllWindows()