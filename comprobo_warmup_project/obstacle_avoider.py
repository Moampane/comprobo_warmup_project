import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from math import sin, cos, radians, atan, sqrt

class ObstacleAvoiderNode(Node):
    def __init__(self):
        super().__init__('obstacle_avoider')
        timer_period = 0.05
        self.timer = self.create_timer(timer_period, self.run_loop)
        self.scan = self.create_subscription(LaserScan, 'scan', self.handle_scan, 10)
        self.cmd_vel = self.create_publisher(Twist, 'cmd_vel', 10)
        self.obstacle_coi = 0.7
        self.delta_x = 0.0
        self.delta_y = 0.0
        self.smallest_dist = 0.0

    def handle_scan(self, msg:LaserScan):
        self.delta_x = 0.0
        self.delta_y = 0.0
        self.smallest_dist = 100.0
        for i in range(len(msg.ranges)):
            if msg.ranges[i] < self.obstacle_coi and msg.ranges[i]!=0:
                self.delta_x-=0.05*(self.obstacle_coi-msg.ranges[i])*cos(radians(i))
                self.delta_y-=0.05*(self.obstacle_coi-msg.ranges[i])*sin(radians(i))
        
        for dist in msg.ranges[0:45]:
            if dist < self.smallest_dist and dist > 0.0:
                self.smallest_dist = dist

        for dist in msg.ranges[315:360]:
            if dist < self.smallest_dist and dist > 0.0:
                self.smallest_dist = dist

    def run_loop(self):
        msg = Twist()
        msg.linear.x = 0.0

        if self.delta_x != 0.0:
            angular_speed = -6.0*(atan(radians(self.delta_y/self.delta_x)))
            if angular_speed > 3.0:
                msg.angular.z = 3.0
            elif angular_speed < -3.0:
                msg.angular.z = -3.0
            else:
                msg.angular.z = angular_speed
        else:
            msg.angular.z = 0.0

        linear_speed = 1.0*(self.smallest_dist-0.3)

        if linear_speed == 0.0 or linear_speed > 100:
            msg.linear.x = 0.05
        else:
            msg.linear.x = linear_speed

        self.cmd_vel.publish(msg)

def main():
    rclpy.init()
    node = ObstacleAvoiderNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()