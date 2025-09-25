import rclpy
from rclpy.node import Node

#start on logic assume joystick input, x axis and y axis as float given to us, turn that into 4 motor values to spin them
class SeeKeys(Node):

    def __init__(self):
    
        super().__init__('see_keys')
        

        self.subscription = self.create_subscription(Int32, '/keyboard/keypress', self.key_pressed, 10)

    def key_pressed(self, message):
        return


                
    def action(self):
        
        msg = Twist()
        msg.linear.x = float(self.drive)
        msg.angular.z = float(self.turn)
        self.publisher_.publish(msg)
        self.turn = 0
        self.drive = 0



def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = SeeKeys()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()