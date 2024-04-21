import time
import pygame
import rclpy
from std_msgs.msg import String

pygame.init()

# Initialize ROS2 node
rclpy.init()
node = rclpy.create_node('joystick_publisher')

# ROS2 publisher
pub = node.create_publisher(String, 'move_topic', 10)

def main():
    joysticks = {}
    done = False
    active = False
    while not done:
        time.sleep(0.05)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True  # Flag that we are done so we exit this loop.
            if event.type == pygame.JOYBUTTONDOWN:
                print(f"Joystick button {event.button} pressed.")
                print(type(event.button))
                if event.button == 0:
                    print('Active true!')
                    active = True
            if event.type == pygame.JOYBUTTONUP:
                print(f"Joystick button {event.button} released.")
                if event.button == 0:
                    print('Active false!')
                    active = False
            if event.type == pygame.JOYDEVICEADDED:
                joy = pygame.joystick.Joystick(event.device_index)
                joysticks[joy.get_instance_id()] = joy
                print(f"Joystick {joy.get_instance_id()} connencted")
            if event.type == pygame.JOYDEVICEREMOVED:
                del joysticks[event.instance_id]
                print(f"Joystick {event.instance_id} disconnected")

        # For each joystick:
        for joystick in joysticks.values():
            axes = joystick.get_numaxes()
            for i in range(axes):
                axis = joystick.get_axis(i)
                print(f"Axis {i} value: {axis:>6.3f}")
            ##
            ## PUBLISH ROS2 MESSAGE IF ACTIVE
            ##
            if active:
                fwd = -joystick.get_axis(1)  # Forward value from joystick
                sid = -joystick.get_axis(0)  # Sideways value from joystick
                angle = -joystick.get_axis(2)  # Angle value from joystick
            else:
                fwd = 0.0
                sid = 0.0
                angle = 0.0
            msg = String()
            msg.data = f'{fwd},{sid},{angle}'
            pub.publish(msg)

if __name__ == "__main__":
    main()
    pygame.quit()
    rclpy.shutdown()
