from example_interfaces.srv import AddTwoInts
import rclpy
from rclpy.node import Node

class ServMinimo(Node):

    def __init__(self):
        super().__init__('little_ser')
        self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.add_two_ints_callback)

    def add_two_ints_callback(self, chamado, resposta):
        resposta.sum = chamado.a + chamado.b
        self.get_logger().info('Números encaminhados: (A = %d B = %d)' % (chamado.a, chamado.b))

        return resposta

def main():
    rclpy.init()

    little_ser = ServMinimo()
    rclpy.spin(little_ser)
    rclpy.shutdown()

if __name__ == '__main__':
    main()