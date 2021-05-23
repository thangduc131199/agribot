import cv2 as cv
from sensor_msgs.msg import Image
import rospy
import numpy as np
from cv_bridge import CvBridge, CvBridgeError

def listen():
    rospy.init_node('img',anonymous=True)
    rospy.Subscriber('/camera/image_raw',Image,show_image,)
    rospy.spin()

def show_image(img):
    w=img.width
    h=img.height
    data=img.data
    end=img.encoding
    frame=np.array(data)
    data_=np.frombuffer(data,dtype=np.uint8)
    img_=cv.imdecode(data_,cv.I)
    print(img_)
    #data_=np.reshape(data_,(w,-1,3))
    

    #cv.imshow('a',data_)
    #frame=cv.imdecode(data_,cv.IMREAD_COLOR)
    #frame=cv.resize(frame,(h,w))
    #cv.imshow(frame)


if __name__=='__main__':
    listen()
