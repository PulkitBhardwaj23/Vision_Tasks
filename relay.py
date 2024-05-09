#!/usr/bin/env python

import rospy
from ackermann_msgs.msg import AckermannDriveStamped

def callback(data):
    speed = data.drive.speed * 3
    steering_angle = data.drive.steering_angle * 3
    
    pub = rospy.Publisher('drive_relay', AckermannDriveStamped, queue_size=10)
    ack_msg = AckermannDriveStamped()
    ack_msg.drive.speed = speed
    ack_msg.drive.steering_angle = steering_angle
    pub.publish(ack_msg)

def relay():
    rospy.init_node('relay', anonymous=True)
    
    rospy.Subscriber('drive', AckermannDriveStamped, callback)
    
    rospy.spin()

if __name__ == '__main__':
    relay()
