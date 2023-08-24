#!/usr/bin/env python

# COMMENT 
# COMMENT 1
# COMMENT +
# COMMENT 2+

import rospy
from std_msgs.msg import String

def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + 'Te escucho %s', data.data)
    print('Te escucho',data.data)

def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('chatter', String, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
