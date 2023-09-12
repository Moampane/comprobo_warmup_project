import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class WallFollowerNode(Node):
    def __init__(self):
        super().__init__('wall_follower')
        self.pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.subscriber = self.create_subscription(LaserScan, 'scan', self.handle_scan, 10)
        timer_period = 0.05
        self.timer = self.create_timer(timer_period, self.run_loop)
        self.dist_45 =  0.0
        self.dist_135 = 0.0
        self.difference = 0.025

    def handle_scan(self, msg:LaserScan):

        self.dist_45 = msg.ranges[40:50]
        self.dist_135 = msg.ranges[127:137]

    def run_loop(self):
        msg = Twist()
        msg.angular.z = 0.0

        for i in range(len(self.dist_45)):
            if self.dist_45[i] - self.dist_135[i] > self.difference:
                msg.angular.z += 0.3/len(self.dist_45)

            if self.dist_135[i] - self.dist_45[i] > self.difference:
                msg.angular.z -= 0.3/len(self.dist_45)
        
        msg.linear.x = 0.1
        
        self.pub.publish(msg)

def main():
    rclpy.init()
    node = WallFollowerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()