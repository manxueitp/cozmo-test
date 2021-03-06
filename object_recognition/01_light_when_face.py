#!/usr/bin/env python3

# Copyright (c) 2016 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''Wait for Cozmo to see a face, and then turn on his backpack light.

This is a script to show off faces, and how they are easy to use.
It waits for a face, and then will light up his backpack when that face is visible.
'''

import asyncio
import time
import cozmo


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
    else:
        message = "no picture saved"
    robot.camera.image_stream_enabled = False
    return message

######## Object recognition ###########

cozmo.run_program(light_when_face, use_viewer=True, force_viewer_on_top=True)
