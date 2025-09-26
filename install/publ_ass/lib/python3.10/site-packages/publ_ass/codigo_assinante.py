import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class AssiMinimo(Node):

    def __init__(self):
        super().__init__('little_ass')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)
        self.subscription

    def listener_callback(self, msg):
        self.get_logger().info('Mensagem enviada: "%s"' % msg.data)
    
def main(args=None):
    rclpy.init(args=args)

    little_ass = AssiMinimo()
    rclpy.spin(little_ass)

    little_ass .destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()