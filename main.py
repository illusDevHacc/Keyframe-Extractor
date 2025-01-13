import cv2,glob
from sys import exit
import utils.compress as compress
from colorama import Fore
from os import mkdir,path
from shutil import rmtree, move

for i in glob.glob(r"MP4s-For-Keyframe\*.mp4"):
    video = cv2.VideoCapture(i)
    if not video.isOpened():
        print(Fore.RED+"FİLE NOT OPENED")
        exit()
    framecount=0
    keyframecount=0
    print(Fore.BLUE + "Starting...")
    mkdir("Keyframe-pngs")
    while True:
        ret, frame= video.read()
        if not ret:
            break
        if keyframecount %1 ==0:
            keyframepath = path.join("Keyframe-pngs", f"keyframe_{keyframecount:04d}.png")
            cv2.imwrite(keyframepath,frame)
            keyframecount +=1
            print(f"{keyframecount-1} keyframe extracted")
        framecount+=1
    print(Fore.BLUE+"Keyframes is Compressing")
    compress.compress(glob.glob(r"Keyframe-pngs\*.png"), i+".zip")
    print(Fore.BLUE+"Compression Successful. Removing source files")

    for png in glob.glob(".\Keyframe-pngs"):
        rmtree(png)
        print(f"All soruce files deleted")
    move(f".\\{i}.zip", ".\\Keyframe-zip")
    print(Fore.GREEN+f"all done. keyframes saved Keyframe-zip folder")
video.release()
print(Fore.BLUE+f"total frame : {keyframecount}")