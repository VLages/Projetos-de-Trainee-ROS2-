import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PubMinimo(Node):

    def __init__(self):
        super().__init__('little_pub')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 1  
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Desde o início do programa se passaram: %d segundos' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publicando: "%s"' % msg.data)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)

    little_pub = PubMinimo()
    rclpy.spin(little_pub)
    little_pub .destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
