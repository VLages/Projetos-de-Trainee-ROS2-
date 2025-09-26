import sys
from example_interfaces.srv import AddTwoInts
import rclpy
from rclpy.node import Node

class ClieMinimo(Node):

    def __init__(self):
        super().__init__('little_cli_asc')
        self.cli = self.create_client(AddTwoInts, 'add_two_ints')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Servidor não disponível, tente novamente')
        self.cha = AddTwoInts.Request()

    def send_request(self, a, b):
        self.cha.a = a
        self.cha.b = b
        return self.cli.call_async(self.cha)

def main():
    rclpy.init()

    little_cli = ClieMinimo()
    future = little_cli.send_request(int(sys.argv[1]), int(sys.argv[2]))
    rclpy.spin_until_future_complete(little_cli, future)
    resposta = future.result()
    little_cli.get_logger().info(
        'O resultado da soma %d + %d é %d' %
        (int(sys.argv[1]), int(sys.argv[2]), resposta.sum))

    little_cli.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()