import cv2
import numpy as np

def detect_fire(img_array, sensitivity):

    img_bgr = cv2.cvtColor(
        img_array,
        cv2.COLOR_RGB2BGR
    )

    hsv = cv2.cvtColor(
        img_bgr,
        cv2.COLOR_BGR2HSV
    )

    lower_fire = np.array([5,150,150])
    upper_fire = np.array([25,255,255])

    fire_mask = cv2.inRange(
        hsv,
        lower_fire,
        upper_fire
    )

    h,s,v = cv2.split(hsv)

    bright_mask = cv2.inRange(v,180,255)

    mask = cv2.bitwise_and(
        fire_mask,
        bright_mask
    )

    contours,_ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    detected = img_bgr.copy()

    fire_pixels = 0

    for contour in contours:

        area = cv2.contourArea(contour)

        if area > sensitivity:

            fire_pixels += area

            x,y,w,h = cv2.boundingRect(contour)

            cv2.rectangle(
                detected,
                (x,y),
                (x+w,y+h),
                (0,0,255),
                3
            )

    heatmap = cv2.applyColorMap(
        mask,
        cv2.COLORMAP_JET
    )

    overlay = cv2.addWeighted(
        img_bgr,
        0.7,
        heatmap,
        0.6,
        0
    )

    detected_rgb = cv2.cvtColor(
        detected,
        cv2.COLOR_BGR2RGB
    )

    overlay_rgb = cv2.cvtColor(
        overlay,
        cv2.COLOR_BGR2RGB
    )

    total_pixels = (
        img_array.shape[0] *
        img_array.shape[1]
    )

    risk = min(
        (fire_pixels / total_pixels) * 1000,
        100
    )

    return detected_rgb, overlay_rgb, risk