import asyncio
import time
import cozmo
import io
import os
# Imports the Google Cloud client library
from google.cloud import vision

def light_when_face(robot: cozmo.robot.Robot):
    '''The core of the light_when_face program'''

    # Move lift down and tilt the head up
    robot.move_lift(-3)
    robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()
    #robot.camera.color_image_enabled = True
    face = None

    print("Press CTRL-C to quit")
    while True:
        if face and face.is_visible:
            robot.set_all_backpack_lights(cozmo.lights.blue_light)
        else:
            robot.set_backpack_lights_off()

            # Wait until we we can see another face
            try:
                face = robot.world.wait_for_observed_face(timeout=30)
                take_photo(robot);
            except asyncio.TimeoutError:
                print("Didn't find a face.")
                return

        time.sleep(.1)


###### Taking photo ######
def take_photo(robot:cozmo.robot.Robot, cmd_args = None):
    robot.camera.image_stream_enabled = True
    #robot.camera.color_image_enabled = True
    print("taking a picture...")
    message = ""
    pic_filename = "cozmo_pic_" + str(int(time.time())) + ".png"
    robot.say_text("Take a photo!").wait_for_completed()
    latest_image = robot.world.latest_image
    if latest_image:
        latest_image.raw_image.convert('L').save('img/'+pic_filename)
        message =  "picture saved as: " + pic_filename
        path = os.path.join(
            os.path.dirname(__file__),
            'img/'+ pic_filename)
        detect_labels(robot,path)
    else:
        message = "no picture saved"
    robot.camera.image_stream_enabled = False
    return message

######## Object recognition ###########
def detect_labels(robot:cozmo.robot.Robot,path):
    """Detects labels in the file."""
    vision_client = vision.Client()
    robot.say_text("Sending to google cloud vision api!").wait_for_completed()
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision_client.image(content=content)

    labels = image.detect_labels()
    print('Labels:')

    for label in labels:
        print(label.description)

if __name__ == '__main__':
    cozmo.run_program(light_when_face, use_viewer=True, force_viewer_on_top=True)













path = os.path.join(
    os.path.dirname(__file__),
    'img/1.jpg')
