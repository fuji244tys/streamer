#-------------------------------------------------------------------------------
# Name:         streaming.py
# Purpose:      Win10_PC recieve video from Raspi4 using openCV
#               video streamer be maked by Flask run on Raspi4+USBcamera
#
# Author:       fujioka
#
# Created:     2021/10/20
# Copyright:   (c) T.F. 2021
#-------------------------------------------------------------------------------
import cv2
import time

url = "http://192.168.0.14:5000/video_feed"

#================================================
# func
#================================================
def stream():
    try:
        print('start:' + time.strftime('%Y/%m/%d %H:%M:%S'))
        video = cv2.VideoCapture(url)
        t2=0
        while(video.isOpened()):
            t1 = time.time()
            ret, frame = video.read()
            #------------------------------------------------------------------
            if ret is False:
                print('read error:' + time.strftime('%Y/%m/%d %H:%M:%S'))
                video.release()
                cv2.destroyAllWindows()
                time.sleep(1) #second
                stream()
                break
            #------------------------------------------------------------------
            #cv2.rectangle(frame, pt1, pt2, color, thickness=1
            #                   , lineType=cv2.LINE_8, shift=0)
            cv2.rectangle(frame , (0, 2), (140, 30), (255, 255, 0), -1)
            cv2.putText(frame   , '{:>5.1f} ms'.format((t1 - t2)*1000)
                                , (10, 25)
                                , cv2.FONT_HERSHEY_SIMPLEX
                                , 0.8
                                , (0, 0, 255)
                                , thickness=2)

            cv2.imshow('frame', frame)
            t2 = t1

            #------------------------------------------------------------------
            key = cv2.waitKey(1)
            if key == 27:
                video.release()
                cv2.destroyAllWindows()
                break

    except KeyboardInterrupt:
        pass

    finally:
        video.release()
        cv2.destroyAllWindows()


#================================================
# main
#================================================
stream()



