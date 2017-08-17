#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy				#写ros节点，就需要引入rospy模块
from std_msgs.msg import String		#标准消息的string类型支持

def talker():
    
    pub = rospy.Publisher('chatter', String, queue_size=10)	#chatter话题，std_msgs.msg.String类型消息，queue_size限制缓存消息的数量
    rospy.init_node('talker', anonymous=True)			#初始化名为talker的节点，anonymous = True保证当出现重复名称时，后面添加一个随机数
    rate = rospy.Rate(10) # 10hz				#方便loop延时，下面每秒循环10次
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
