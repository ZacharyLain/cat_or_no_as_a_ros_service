#!/usr/bin/env python3

import rclpy, random, requests
from rclpy.node import Node

from cat_or_no_as_a_ros_service.srv import CatOrNo
from sensor_msgs.msg import CompressedImage

class CatOrNoAsARosServiceNode(Node):
    def __init__(self):
        super().__init__('cat_or_no_as_a_ros_service')
        self.srv = self.create_service(CatOrNo, 'cat_or_no', self.cat_or_no_callback)
        self.get_logger().info('Server started.')
    
    def cat_or_no_callback(self, request: CatOrNo, response: CatOrNo):
        choice = random.randint(0, 1)
        response.result_type = choice
        if choice == 1: # cat
            res = requests.get('https://cataas.com/cat', headers={'accept': 'application/json'})
            img_url = res.json()['url']
            res = requests.get(img_url)
            img_bytes = res.raw.data
            response.cat.image = CompressedImage()
            response.cat.image.header.stamp = self.get_clock().now().to_msg()
            response.cat.image.header.frame_id = 'cat'
            response.cat.image.data = img_bytes
            response.cat.url = img_url
        else: # no
            res = requests.get('https://naas.isalman.dev/no')
            reason = res.json()['reason']
            response.no = reason

        return response


def main(args=None):
    rclpy.init(args=args)

    node = CatOrNoAsARosServiceNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()