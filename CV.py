import cv2 as cv
camera=cv.VideoCapture(0)
tracker=cv.TrackerMOSSE_create()
ret,frame=camera.read()
object=cv.selectROI("drone",frame,False)
tracker.init(frame,obj)

while True:
    timer=cv.getTickCount()
    ret,frame=camera.read()
    fps=cv.getTickFrequency()/(cv.getTickCount()-timer)
    cv.putText(frame,str(fps),(0,0),cv.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
    cv.imshow("tracking", frame)

    if(cv.waitKey(1)& 0xFF==ord("q")):
        print("kameradan cixildi")
        break


