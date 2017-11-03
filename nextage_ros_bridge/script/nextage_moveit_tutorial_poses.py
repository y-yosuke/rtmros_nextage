#!/usr/bin/env python

import rospy, geometry_msgs.msg, copy

from moveit_commander import MoveGroupCommander

if __name__ == '__main__':
    
    rospy.init_node('commander_example', anonymous=True)
    group = MoveGroupCommander("right_arm")
    
    # Pose Target 1
    rospy.loginfo( "Start Pose Target 1")
    pose_target_1 = geometry_msgs.msg.Pose()
        
    pose_target_1.position.x = 0.4
    pose_target_1.position.y = -0.4
    pose_target_1.position.z = 0.15
    pose_target_1.orientation.x = 0.0
    pose_target_1.orientation.y = -0.707
    pose_target_1.orientation.z = 0.0
    pose_target_1.orientation.w = 0.707
    
    rospy.loginfo( "Set Target to Pose:\n{}".format( pose_target_1 ) )
    
    group.set_pose_target( pose_target_1 )
    group.plan()
    group.go()
    
    # Pose Target 2
    rospy.loginfo( "Start Pose Target 2")
    pose_target_2 = geometry_msgs.msg.Pose()
    
    pose_target_2.position.x = 0.3
    pose_target_2.position.y = -0.3
    pose_target_2.position.z = 0.5
    pose_target_2.orientation.y = -1.0
    
    rospy.loginfo( "Set Target to Pose:\n{}".format( pose_target_2 ) )
    
    group.set_pose_target( pose_target_2 )
    group.plan()
    group.go()
    
    
    # Waypoints Motion
    rospy.loginfo( "Start Waypoints Motion")
    
    waypoints = []
    
    # 1st Pose
    waypoints.append( pose_target_1 )
    rospy.loginfo( "Append 1st Pose to waypoints[] - Pose:\n{}".format( pose_target_1 ) )
    
    # 2nd Pose
    pose_target_3 = copy.deepcopy( pose_target_1 )
    pose_target_3.position.y = -0.2
    
    waypoints.append( pose_target_3 )
    rospy.loginfo( "Append 2nd Pose to waypoints[] - Pose:\n{}".format( pose_target_3 ) )
    
    # 3rd Pose
    waypoints.append( pose_target_2 )
    rospy.loginfo( "Append 3rd Pose to waypoints[] - Pose:\n{}".format( pose_target_2 ) )
    
    # 4th Pose
    pose_target_4 = copy.deepcopy( pose_target_2 )
    pose_target_4.position.y = -0.5
    
    waypoints.append( pose_target_4 )
    rospy.loginfo( "Append 4th Pose to waypoints[] - Pose:\n{}".format( pose_target_4 ) )

    # Plan Waypoints Motion and Execute
    ( plan1, fraction ) = group.compute_cartesian_path( waypoints, 0.01, 0.0 )
    group.execute( plan1 )
    
