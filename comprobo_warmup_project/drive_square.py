import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Quaternion
from nav_msgs.msg import Odometry
import math

class DriveSquareNode(Node):
    def __init__(self):
        super().__init__('drive_square')
        self.twist_pub = self.create_publisher(Twist, "cmd_vel", 10)
        self.odom_sub = self.create_subscription(Odometry, 'odom', self.handle_odometry, 10)
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.run_loop)
        self.x = 0.0
        self.y = 0.0
        self.angle = 0.0

    def handle_odometry(self, msg:Odometry):
        self.x = msg.pose.pose.position.x
        self.y = msg.pose.pose.position.y
        self.angle = quaternion_to_yaw(msg.pose.pose.orientation)

    def run_loop(self):
        msg = Twist()
        if self.y < 0 and 1 < self.angle < 2:
            msg.linear.x = 0.0
        elif self.x < 0 and 0 < self.angle < 1.57:
            msg.angular.z = 0.3
        elif self.y > 1 and 4.71 < self.angle < 6.28:
            msg.angular.z = 0.3 
        elif self.x > 1 and 3.14 < self.angle < 4.71:
            msg.angular.z = 0.3
        else: 
            msg.linear.x = 0.1
            print("working")
        self.twist_pub.publish(msg)
        

def quaternion_to_yaw(quat: Quaternion):
    x = quat.x
    y = quat.y
    z = quat.z
    w = quat.w

    t1 = 2.0 * (w * z + x * y)
    t2 = 1.0 - 2.0 * (y * y + z * z)
    yaw_z = math.atan2(t1, t2)

    return yaw_z + math.pi

def main():
    rclpy.init()
    node = DriveSquareNode()
    rclpy.spin(node)
    rclpy.shutdown()
    print('this works')

if __name__ == "__main__":
    main()