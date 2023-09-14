import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class PersonFollowerNode(Node):
    def __init__(self):
        super().__init__('person_follower')
        self.vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.laser_sub = self.create_subscription(LaserScan, 'scan', self.handle_scan, 10)
        timer_period = 0.05
        self.timer = self.create_timer(timer_period, self.run_loop)
        self.idx = 0

    def handle_scan(self, msg:LaserScan):
        shortest_dist = 100.0
        for i in range(len(msg.ranges)):
            if msg.ranges[i] < shortest_dist and msg.ranges[i] > 0.15:
                shortest_dist = msg.ranges[i]
                self.idx = i
        print(shortest_dist)

    def run_loop(self):
        msg = Twist()

        if 0 < self.idx < 10 or 350 < self.idx < 362:
            pass
        elif self.idx > 180:
            msg.angular.z = -0.3
        else:
            msg.angular.z = 0.3
        
        if 0 < self.idx < 45 or 315 < self.idx < 361: 
            msg.linear.x = 0.1
        
        

        self.vel_pub.publish(msg)

def main():
    rclpy.init()
    node = PersonFollowerNode()
    rclpy.spin(node)
    rclpy.shutdown()
    print("works")

if __name__ == '__main__':
    main()