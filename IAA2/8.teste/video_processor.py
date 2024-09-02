import matplotlib.pyplot as plt
from skimage import io
from skimage import color


from sklearn.cluster import KMeans

import joblib
import cv2
import numpy as np





def get_bg_mask(img, kmeans):
    mask = np.zeros_like(img[:,:,0])  # replace by your solution
    return np.logical_not(mask)  # np.logical_not only if fg==0 and bg==1


# For more OpenCV, check https://github.com/a-anjos/python-opencv/blob/master/cv2cheatsheet.pdf
# Expects the file name for the video, the kmeans model and the background image
def process_video(video_green_screen, kmeans, background_image):
    bg_original = cv2.imread(background_image)
    bg_image = bg_original.copy()  # create a copy of the original to work on
    y_s, y_e = 154, 546  # bit we want to crop
    cap = cv2.VideoCapture(video_green_screen)  # open the video
    fps = cap.get(cv2.CAP_PROP_FPS)  # record the number of fps

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # convert color space from BGR to RGB
        mask = get_bg_mask(img, kmeans)  # get the mask for the current frame
        #plt.imshow(mask); plt.show(); break  # uncomment for debugging
        mask = mask[y_s:y_e, :]   # crop 
        mask = np.dstack([mask] * 3)  # convert mask to 3 channels
        frame = frame[y_s:y_e, :] * (mask > 0)  # crop and apply mask
        mask_inv = mask == 0  # get the inverse mask
        bg_image = bg_original.copy()
        # position the frame on the background
        start_x = bg_image.shape[1] // 2 - frame.shape[1] // 2
        start_y = bg_image.shape[0] - frame.shape[0]
        bg_image[start_y:, start_x:start_x+frame.shape[1]] *= mask_inv  # apply inverse mask
        bg_image[start_y:, start_x:start_x+frame.shape[1]] += frame  # add frame to the background
        cv2.imshow('The monster!!!', bg_image)
        # milliseconds to wait between frames
        ms = int(1000/fps)
        #ms = 1  # if inference takes too long, comment above and uncomment this
        if cv2.waitKey(int(ms)) & 0xFF == ord('q'): # wait ms or press q to quit
            break
    cap.release()
    cv2.destroyAllWindows()                        


def test_play_video():
    bg = './obama.jpg'
    kmeans = joblib.load('./k2.pkl')  # replace by your model name
    process_video('./dog.mp4', kmeans, bg)


test_play_video()
