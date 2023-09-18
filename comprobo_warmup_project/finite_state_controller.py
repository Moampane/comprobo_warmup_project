import rclpy
from rclpy.node import Node, Publisher
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
from neato2_interfaces.msg import Bump


class WallFollowerNode(Node):
    def __init__(self):
        super().__init__('finite_state_controller')
        # Setup Wall Follower Behaviour
        self.pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.subscriber = self.create_subscription(LaserScan, 'scan', self.handle_scan, 10)
        timer_period = 0.05
        self.timer = self.create_timer(timer_period, self.run_loop)
        self.dist_45 =  0.0
        self.dist_135 = 0.0
        self.difference = 0.025

        # Setup Bump Behaviour
        self.bump_sub = self.create_subscription(Bump, 'bump', self.bump_obstacle, 10)
        self.state = 'wall_follower'
        self.counter = 0

   def handle_scan(self, msg:LaserScan):
        self.dist_45 = msg.ranges[40:50]
        self.dist_135 = msg.ranges[127:137]
     
    def bump_obstacle(self, bump: Bump):
        if bump.left_front or bump.right_front:
            self.state = 'obstacle_hit'

    def run_loop(self):
        # Implement Wall Follower Behaviour
        if self.state == 'wall_follower':
            msg = Twist()
        msg.angular.z = 0.0
        for i in range(len(self.dist_45)):
            if self.dist_45[i] - self.dist_135[i] > self.difference:
                msg.angular.z += 0.3/len(self.dist_45)
            if self.dist_135[i] - self.dist_45[i] > self.difference:
                msg.angular.z -= 0.3/len(self.dist_45)        
        msg.linear.x = 0.1        
        self.pub.publish(msg)
      
        # Implement Bump Behaviour
        if self.state == 'obstacle_hit':
            if self.counter < 5:
                msg: Twist = Twist(
                    angular=Vector3(x=0.0, y=0.0, z=0.0),
                    linear=Vector3(x=-0.5, y=0.0, z=0.0),
                )
                self.pub.publish(msg)
                self.counter += 1
            elif self.counter >= 5 and self.counter < 20:
                msg: Twist = Twist(
                    angular=Vector3(x=0.0, y=0.0, z=1.0),
                    linear=Vector3(x=0.0, y=0.0, z=0.0),
                )
                self.pub.publish(msg)
                self.counter += 1
            else:
                self.state = 'wall_follower'
                self.counter = 0


def main():
    rclpy.init()
    node = WallFollowerNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
