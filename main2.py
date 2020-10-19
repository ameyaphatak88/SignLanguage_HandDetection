import cv2
import os
import sys
import Recognizer
from flask import Flask

def get_output_filename(ipfilename):
  a = str(ipfilename)
  a = a[:-4]
  return a


def read_and_write(filepath):
  assert os.path.isfile(filepath), 'Invalid filepath as argument'

  video1 = cv2.VideoCapture(filepath)

  frame_width  = int(video1.get(3)) # float
  frame_height = int(video1.get(4)) # float

  s = (frame_width, frame_height)

  outfile = "outp"
  out1 = cv2.VideoWriter(outfile + '_out.mkv',
                        cv2.VideoWriter_fourcc('M','J','P','G'), 
                        100, 
                        (frame_width, frame_height))

  while(True):
    ret, frame = video1.read()

    if ret == True: 
      
      # Write the frame into the file 'output.avi'
      out1.write(frame)

      frame = Recognizer.predict_and_rectangle(frame)

      # Display the resulting frame    
      cv2.imshow('frame',frame)

      # Press Q on keyboard to stop recording
      if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Break the loop
    else:
      break  

  out1.release()



if __name__ == "__main__":
  assert (len(sys.argv) == 2), 'Required number of arguments not passed'
  filepath = sys.argv[1]
  read_and_write(filepath)
