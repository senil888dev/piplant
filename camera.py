from picamera import PiCamera
import time
import schedule

camera = PiCamera()

def takePhoto():
    camera.start_preview()
    time.sleep(5)
    camera.capture('C:/Users/Sean/Downloads/ExtraExtra/PolyBridgeGIFs/photo.jpg')
    camera.stop_preview()
    
schedule.every().day.at('07:00').do(takePhoto()

while True:
                                    schedule.run_pending()
                                    time.sleep(1)
