import time
from naoqi import ALProxy
import Ice
import sys
import PepperMove
from PIL import Image

# Connect to the NAOqi API
ip = "169.254.201.174"  # Replace this with your robot's IP address
port = 9559  # Default port for NAOqi


# Call define what function to call within the naoqi library and pass the IP address of the robot and the port number
motion = ALProxy("ALMotion", ip, port)

try:
  video_service = ALProxy("ALVideoDevice", ip, port)
  resolution = 2    # VGA
  colorSpace = 11   # RGB
  videoClient = video_service.subscribe("python_client", resolution, colorSpace, 5)
except Exception as e:
  print ("Error when creating ALPhotoCapture proxy:")
  print (e)
  exit(1)

def goAhead():
    motion.move(0.0, 0.0, 0.0)

def manualMove(fwd, sid, angle):
    motion.move(fwd, sid, angle)

#The following code was taken from the NAO documentation and adjusted for this project
def getImage():
    videoClient = video_service.subscribe("python_client", resolution, colorSpace, 5)
    naoImage = video_service.getImageRemote(videoClient)
    imageWidth = naoImage[0]
    imageHeight = naoImage[1]
    array = naoImage[6]
    image_string = str(bytearray(array))
    # Create a PIL Image from our pixel array.
    im = Image.frombytes("RGB", (imageWidth, imageHeight), image_string)
    # Save the image to a file
    image_filename = "LiveFeed.jpg"
    im.save(image_filename)
    video_service.unsubscribe(videoClient)
    
#The following code was taken from the NAO documentation and adjusted for this project    
def leftArm(lspitch, lsroll, lelbowyaw,lelbowroll):
    motion.setStiffnesses("LArm", 1.0)
    names = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll"]
    angles = [lspitch, lsroll, lelbowyaw,lelbowroll]
    fractionMaxSpeed = 0.2
    motion.setAngles(names, angles, fractionMaxSpeed)
    time.sleep(3.0)
    motion.setStiffnesses("LArm", 0.0)

#The following code was taken from the NAO documentation and adjusted for this project
def rightArm(rspitch, rsroll, relbowyaw,relbowroll):
    motion.setStiffnesses("RArm", 1.0)
    names = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll"]
    angles = [rspitch, rsroll, relbowyaw,relbowroll]
    fractionMaxSpeed = 0.2
    motion.setAngles(names, angles, fractionMaxSpeed)
    time.sleep(3.0)
    motion.setStiffnesses("RArm", 0.0)

class MovementI(PepperMove.Movement):
    def moveForward(self, current=None):
        print("moving forward")
        goAhead()

    def moveLeftArm(self,lspitch, lsroll, lelbowyaw,lelbowroll, current=None):
        print("Left arm is moving", lspitch, lsroll, lelbowyaw,lelbowroll)
        leftArm(lspitch, lsroll, lelbowyaw,lelbowroll)

    def moveRightArm(self,rspitch, rsroll, relbowyaw,relbowroll,current=None):
        print("Right arm is moving",)
        rightArm(rspitch, rsroll, relbowyaw,relbowroll)

    def mMove(self, fwd, sid, angle, current=None):
        print("moving", fwd, sid, angle)
        manualMove(fwd, sid, angle)

    def returnImage(self, current=None):
        print("Printing Images")
        getImage()


def main():
    # Initialize ICE communicator
    communicator = Ice.initialize(sys.argv)

    adapter = communicator.createObjectAdapterWithEndpoints("MovementAdapter", "default -h localhost -p 10000")
    movement_servant = MovementI()
    adapter.add(movement_servant, Ice.stringToIdentity("Movement"))
    adapter.activate()

    print("ICE server is running.")
    communicator.waitForShutdown()

    # Clean up ICE resources
    if communicator:
        try:
            communicator.destroy()
        except Ice.Exception as e:
            print("Error during communicator destruction:", e)

if __name__ == "__main__":
    main()
