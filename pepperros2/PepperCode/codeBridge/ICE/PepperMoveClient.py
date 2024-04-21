import Ice
import PepperMove 
import rclpy
from std_msgs.msg import String

# Import your PepperMove class from the PepperMove.py file

def main():
    # Initialize ICE communicator
    Ice.loadSlice("PepperMove.ice")
    communicator = Ice.initialize()

    try:
        # Get proxy to the Movement interface
        base = communicator.stringToProxy("Movement:tcp -h localhost -p 10000")
        movement = PepperMove.MovementPrx.checkedCast(base)

        # Initialize ROS2 node
        rclpy.init()
        node = rclpy.create_node('ice_to_ros_bridge')

        # ROS2 subscriber for moving the robot with the joystick
        def callback_move(msg):
            # Callback function to receive messages from ROS_TOPIC
            print("move_topic activated", msg.data)

            # Split the message data into command and values

                # Parse the message data to extract fwd, sid, and angle values
            try:
                data = msg.data.split(',')
                fwd = float(data[0].strip())
                sid = float(data[1].strip())
                angle = float(data[2].strip())
                # Call the mMove method with extracted values
                movement.mMove(fwd, sid, angle)
            except ValueError:
                print("Format not supported")

        def callback_rightarm(msg):
            # Callback function to receive messages from ROS_TOPIC
            print("rightarm_topic activated:", msg.data)
            # Split the message data into command and values
            try:
                data = msg.data.split(',')
                rspitch = float(data[0].strip())
                rsroll = float(data[1].strip())
                relbowyaw = float(data[2].strip())
                relbowroll = float(data[3].strip())
                movement.moveRightArm(rspitch, rsroll, relbowyaw,relbowroll)
            except ValueError:
                print("Something went wrong with the command")


        def callback_leftarm(msg):
            # Callback function to receive messages from ROS_TOPIC
            print("leftarm_topic activated:", msg.data)

            # Split the message data into command and values
            try:
                data = msg.data.split(',')
                lspitch = float(data[0].strip())
                lsroll = float(data[1].strip())
                lelbowyaw = float(data[2].strip())
                lelbowroll = float(data[3].strip())
                movement.moveLeftArm(lspitch, lsroll, lelbowyaw,lelbowroll)
            except ValueError:
                    print("Something went wrong with the command")

        def callback_image(msg):
            # Callback function to receive messages from ROS_TOPIC
            print("image_topic activated:", msg.data)

            # Split the message data into command and values
            # data = msg.data.lower().split()
            # command = data[0].strip()

            if msg.data == 'image':
                # If the command is 'image', call the returnImage method
                movement.returnImage()

            else:
                print("Command not found")

        #Subscribe to ROS2 topics when published  
        sub_move = node.create_subscription(String, 'move_topic', callback_move, 10)
        sub_rightarm = node.create_subscription(String, 'rightarm_topic', callback_rightarm, 10)
        sub_leftarm = node.create_subscription(String, 'leftarm_topic', callback_leftarm, 10)
        sub_image = node.create_subscription(String, 'image_topic', callback_image, 10)

        print("ICE client and ROS2 bridge initialized.")
        rclpy.spin(node)

    except Ice.Exception as e:
        print("Error:", e)

    finally:
        # Clean up ICE resources
        if communicator:
            try:
                communicator.destroy()
            except Ice.Exception as e:
                print("Error during communicator destruction:", e)

        # Clean up ROS2 resources
        rclpy.shutdown()

if __name__ == "__main__":
    main()
