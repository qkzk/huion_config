#!/usr/bin/env python

"""
title: Limit stylus to a specific screen
author: qkzk
date: 2022/01/30

The command we need to input is 

$ xinput map-to-output $id_pen $screen_name

Where $id_pen can be found with `$ xinput`, looking to string "pen" in the output
And $screen_name can be found with `$ rander`, looking for the leftmost screen (I assume).

The script finds the $id pen, which change after reboot, and then input the command.
"""

import subprocess
import sys


response = """
⎡ Virtual core pointer                    	id=2	[master pointer  (3)]
⎜   ↳ Virtual core XTEST pointer              	id=4	[slave  pointer  (2)]
⎜   ↳ HID 256c:006d Dial                      	id=9	[slave  pointer  (2)]
⎜   ↳ AONE Varmilo Keyboard Consumer Control  	id=13	[slave  pointer  (2)]
⎜   ↳ SteelSeries SteelSeries Rival 100 Gaming Mouse	id=14	[slave  pointer  (2)]
⎜   ↳ HID 256c:006d Pen Pen (0)               	id=17	[slave  pointer  (2)]
⎣ Virtual core keyboard                   	id=3	[master keyboard (2)]
    ↳ Virtual core XTEST keyboard             	id=5	[slave  keyboard (3)]
    ↳ Power Button                            	id=6	[slave  keyboard (3)]
    ↳ Power Button                            	id=7	[slave  keyboard (3)]
    ↳ HID 256c:006d Pen                       	id=8	[slave  keyboard (3)]
    ↳ AONE Varmilo Keyboard                   	id=10	[slave  keyboard (3)]
    ↳ AONE Varmilo Keyboard Keyboard          	id=11	[slave  keyboard (3)]
    ↳ AONE Varmilo Keyboard System Control    	id=12	[slave  keyboard (3)]
    ↳ HID 256c:006d Dial                      	id=15	[slave  keyboard (3)]
    ↳ AONE Varmilo Keyboard Consumer Control  	id=16	[slave  keyboard (3)]

"""
PEN_INPUT_ID = "HID 256c:006d Pen"
SCREENS = {0: "HDMI-A-0", 1: "DisplayPort-2"}



def exec_command(cmd):
    print("executing :", cmd)
    output, error = subprocess.Popen(
        cmd,
        shell=True,
        executable="/bin/bash",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).communicate()
    return output, error


def get_pen_id():
    cmd = "xinput"
    output, error = exec_command(cmd)
    print(output.decode())
    print("---")
    print(error)

    try:
        response = output.decode()
        find_pen = response.find(PEN_INPUT_ID)
        find_id = response[find_pen:].find("id=")
        index_id = find_pen + find_id + 3
        pen_id = int(response[index_id : index_id + 2])
        return pen_id
    except Exception as e:
        print(dir(e))
        print(repr(e.args))
        raise


def set_tablet_left_screen(pen_id, monitor_id):
    monitor = SCREENS[monitor_id]
    cmd = f"xinput map-to-output {pen_id} {monitor}"
    output, error = exec_command(cmd)
    print(output)
    print("---")
    print(error)


def read_args():
    if len(sys.argv) > 1 and sys.argv[1] in ("right", "1"):
        return 1
    return 0


def main():
    monitor_id = read_args()
    pen_id = get_pen_id()
    set_tablet_left_screen(pen_id, monitor_id)


if __name__ == "__main__":
    main()
