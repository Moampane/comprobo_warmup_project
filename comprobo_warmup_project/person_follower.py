import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from visualization_msgs.msg import Marker
from math import cos, sin, radians

class PersonFollowerNode(Node):
    def __init__(self):
        super().__init__('person_follower')
        self.vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.pub_marker =  self.create_publisher(Marker, 'visualization_marker', 10)
        self.laser_sub = self.create_subscription(LaserScan, 'scan', self.handle_scan, 10)
        timer_period = 0.05
        self.timer = self.create_timer(timer_period, self.run_loop)
        self.idx = 0

    def handle_scan(self, msg:LaserScan):
        # Find and record shortest measured distance
        shortest_dist = 100.0
        for i in range(len(msg.ranges)):
            if msg.ranges[i] < shortest_dist and msg.ranges[i] > 0.15:
                shortest_dist = msg.ranges[i]
                self.idx = i
        self.handle_person_marker(msg.ranges[self.idx],self.idx)

    def run_loop(self):
        msg = Twist()

        # Turn towards where the shortest measured distance was recorded
        if 0 < self.idx < 10 or 350 < self.idx < 362:
            pass
        elif self.idx > 180:
            msg.angular.z = -0.3
        else:
            msg.angular.z = 0.3
        
        # If the shortest measured distance is within the front 90 degrees of the neato move forward
        if 0 < self.idx < 45 or 315 < self.idx < 361: 
            msg.linear.x = 0.1

        self.vel_pub.publish(msg)

    def handle_person_marker(self, distance, angle):
        # Make marker for person neato is following
        # Visualization
        marker = Marker()
        marker.header.frame_id = 'base_link'
        marker.header.stamp =  self.get_clock().now().to_msg()
        # Make ns unique per marker
        marker.ns = f"Spoint_{angle}"
        marker.id = 0
        marker.type = Marker.SPHERE
        marker.action = Marker.ADD
        # Polar to cartesian conversion
        marker.pose.position.x = distance*cos(radians(angle))
        marker.pose.position.y = distance*sin(radians(angle))
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
    node = PersonFollowerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()