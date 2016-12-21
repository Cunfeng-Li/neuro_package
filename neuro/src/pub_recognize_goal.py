#!/usr/bin/env python
# license removed for brevity
import rospy
import time

from std_msgs.msg import String
from geometry_msgs.msg import Pose, Point, Quaternion, Twist


def talker1():
    pub = rospy.Publisher('/comm/msg/control/recognize_goal', String, queue_size=10)
    rospy.init_node('pub_recognize_goal', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        # hello_str = "hello world %s" % rospy.get_time()
        # rospy.loginfo(hello_str)

        string = "bottle"
        pub.publish(string)
        # rate.sleep()
        # rospy.sleep(10)
        # time.sleep(5)
        # pose=Pose(Point(0.5, 3, 0.0), Quaternion(0.0, 0.0, 0.0, 1.0))
        # pub.publish(pose)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker1()
    except rospy.ROSInterruptException:
        pass
