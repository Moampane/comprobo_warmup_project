import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from visualization_msgs.msg import Marker
from math import  cos, sin, radians

class WallFollowerNode(Node):

    def __init__(self):
        super().__init__('wall_follower')
        self.pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.pub_marker =  self.create_publisher(Marker, 'visualization_marker', 10)
        self.subscriber = self.create_subscription(LaserScan, 'scan', self.handle_scan, 10)
        timer_period = 0.05
        self.timer = self.create_timer(timer_period, self.run_loop)
        self.dist_45 =  []
        self.dist_135 = []
        self.difference = 0.025

    def handle_scan(self, msg:LaserScan):
        # Get range of values around 45 and 135 degrees from neato
        self.dist_45 = msg.ranges[40:50]
        self.dist_135 = msg.ranges[127:137]

        self.handle_marker(self.dist_45, range(40,51))
        self.handle_marker(self.dist_135, range(127,138))

    def run_loop(self):
        msg = Twist()
        msg.angular.z = 0.0

        # Adjust angular velocity depending on the neato is closer to the wall around 45 or 135 degrees
        for i in range(len(self.dist_45)):
            if self.dist_45[i] - self.dist_135[i] > self.difference:
                msg.angular.z += 0.3/len(self.dist_45)

            if self.dist_135[i] - self.dist_45[i] > self.difference:
                msg.angular.z -= 0.3/len(self.dist_45)
        
        # Neato is constantly moving forward
        msg.linear.x = 0.1
        
        self.pub.publish(msg)

    def handle_marker(self, ranges:list, angles:list):
        # Make markers for scans that affect neato movement
        for i in range(len(ranges)):
            # Visualization
            marker = Marker()
            marker.header.frame_id = 'base_link'
            marker.header.stamp =  self.get_clock().now().to_msg()
            # Make ns unique per marker
            marker.ns = f"Spoint_{angles[i]}"
            marker.id = 0
            marker.type = Marker.SPHERE
            marker.action = Marker.ADD
            # Polar to cartesian conversion
            marker.pose.position.x = ranges[i]*cos(radians(angles[i]))
            marker.pose.position.y = ranges[i]*sin(radians(angles[i]))
            marker.pose.position.z = 0.0

            marker.pose.orientation.x = 0.0
            marker.pose.orientation.y = 0.0
            marker.pose.orientation.z = 0.0
            marker.pose.orientation.w = 1.0

            marker.scale.x = 0.1
            marker.scale.y = 0.1
            marker.scale.z = 0.1

            marker.color.a = 1.0
            marker.color.r = 1.0
            marker.color.g = 1.0
            marker.color.b = 0.0

            self.pub_marker.publish(marker)

def main():
    rclpy.init()
    node = WallFollowerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()