#!/usr/bin/env python
# -*- coding: utf-8 -*-

from beginner_tutorials.srv import *
import rospy

def handle_add_two_ints(req):
    print "Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b))
    return AddTwoIntsResponse(req.a + req.b)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)		#服务名称add_two_ints，服务类型AddTwoInts，服务回调handle_add_two_ints
    print "Ready to add two ints."
    rospy.spin()	#执行完后节点不会自动退出

if __name__ == "__main__":
    add_two_ints_server()
