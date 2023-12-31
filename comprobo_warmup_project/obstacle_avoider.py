import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class ObstacleAvoiderNode(Node):
    def __init__(self):
        super().__init__('obstacle_avoider')
        timer_period = 0.05
        self.timer = self.create_timer(timer_period, self.run_loop)
        self.scan = self.create_subscription(LaserScan, 'scan', self.handle_scan, 10)
        self.cmd_vel = self.create_publisher(Twist, 'cmd_vel', 10)
        self.inner_left = [0.0]
        self.inner_right = [0.0]
        self.smallest_dist = 100.0
        self.trapped = False

    def handle_scan(self, msg:LaserScan):
        self.smallest_dist = 100.0
        self.inner_left = msg.ranges[0:30]
        self.inner_right = msg.ranges[330:360]

        for i in range(len(self.inner_left)):
            if self.inner_left[i] != 0.0 and self.inner_left[i] < self.smallest_dist:
                self.smallest_dist = self.inner_left[i]
            if self.inner_right[i] != 0.0 and self.inner_right[i] < self.smallest_dist:
                self.smallest_dist = self.inner_right[i]

    def run_loop(self):
        msg = Twist()
        msg.angular.z = 0.0
        msg.linear.x = 0.0
        self.turn_input = 0.0

        for i in range(len(self.inner_left)):
            if self.inner_right[i] != 0.0 and self.inner_right[i] < 0.6:
                self.turn_input += 1/(2*len(self.inner_left)*self.inner_right[i])

            if self.inner_left[i] != 0.0 and self.inner_left[i] < 0.6:
                self.turn_input -= 1/(2*len(self.inner_left)*self.inner_left[i])

        
            
        if self.smallest_dist < 0.4:
            self.trapped = True
            msg.linear.x = -self.smallest_dist*0.1
            msg.angular.z = -self.turn_input
        elif not self.trapped:
            msg.linear.x = self.smallest_dist*0.1
            msg.angular.z = self.turn_input
        elif self.smallest_dist > 0.5:
            self.trapped = False
        else: 
            msg.linear.x = -self.smallest_dist*0.1
            msg.angular.z = -self.turn_input

        # print(self.smallest_dist)
        
        self.cmd_vel.publish(msg)

def main():
    rclpy.init()
    node = ObstacleAvoiderNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()