#!/usr/bin/env python

import rospy
from ackermann_msgs.msg import AckermannDriveStamped

def talker():
    rospy.init_node('talker', anonymous=True)
    
    # Get ROS parameters v and d
    v = rospy.get_param('~v', 0.0)
    d = rospy.get_param('~d', 0.0)
    
    pub = rospy.Publisher('drive', AckermannDriveStamped, queue_size=10)
    
    rate = rospy.Rate(10)  # 10hz
    
    while not rospy.is_shutdown():
        ack_msg = AckermannDriveStamped()
        ack_msg.drive.speed = v
        ack_msg.drive.steering_angle = d
        pub.publish(ack_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
