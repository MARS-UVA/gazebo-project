import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class SeeKeys(Node):


    def __init__(self):
    
        super().__init__('see_keys')
        turn = 0
        drive = 0
        self.publisher_ = self.create_publisher(Twist, '/cmd_vml', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.action)


        self.subscription = self.create_subscription(Int32, '/keyboard/keypress', key_pressed, 10)

    def key_pressed(self, message):
        match message.data:
            case 87:
                drive = 1
            case 65:
                turn = 1
            case 68:
                turn = -1
            case 83:
                drive = -1
            

                
    def action(self):
        
        msg = Twist()
        msg.linear.x = drive
        msg.angular.z = turn
        self.publisher_.publish(msg)
        turn = 0
        drive = 0






def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()