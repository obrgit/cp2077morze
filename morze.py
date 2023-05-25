import time
import cv2
import numpy

video = cv2.VideoCapture('cp2077.mp4')
flash = False
space_begin = 0
space_end = 0
start = None
end = None
result = ''

while video.isOpened():
    ret, frame = video.read()
    if ret:

        roi = frame[310:350, 510:620]
        avg_color_per_row = numpy.average(roi, axis=0)
        avg_color = numpy.average(avg_color_per_row, axis=0)
        num = int(avg_color[0]) - (int(avg_color[0]) % 10)

        if num >= 100:

            if flash == 0: 
                
                start = time.time()
                flash = True
                space_end = time.time()
                diff = space_end - space_begin
                if round(diff, 2) >= 0.14: result += ' '

        if flash and num < 100:

            end = time.time()
            flash_length = end - start
            if round(flash_length, 1) == 0.0: result += '.'    
            elif round(flash_length, 1) == 0.1: result += '-'
        
            flash = False
            start = None
            space_begin = time.time()

    else: break

    cv2.waitKey(1)

print(result.strip())