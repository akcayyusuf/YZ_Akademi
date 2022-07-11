import cv2





def time2Frame(h=0,m=0,s=0,fr=30):
    frame = (h * 3600 + m * 60 + s) * fr
    return int(frame)


#Video file
vid = cv2.VideoCapture("bolt.mp4")

#Create Trackers
BOOSTING=cv2.legacy.TrackerBoosting_create()
MIL=cv2.TrackerMIL_create()
KCF=cv2.TrackerKCF_create()
TLD=cv2.legacy.TrackerTLD_create()
MEDIANFLOW=cv2.legacy.TrackerMedianFlow_create()
MOSSE=cv2.legacy.TrackerMOSSE_create()
CSRT=cv2.TrackerCSRT_create()

startFrame=time2Frame(0,0,2,vid.get(cv2.CAP_PROP_FPS))
vid.set(1,startFrame)
endFrame=time2Frame(0,0,18,vid.get(cv2.CAP_PROP_FPS))


ret,frame =vid.read()
box =(444, 220, 39, 83)




BOOSTING.init(frame, box)
MIL.init(frame, box)
KCF.init(frame, box)
TLD.init(frame, box)
MEDIANFLOW.init(frame, box)
MOSSE.init(frame,box)
CSRT.init(frame, box)

count=0
while True:

    # Read a new frame
    ret, frame = vid.read()
    if not ret:
        break

    # Start timer
    timer = cv2.getTickCount()

    # Update tracker
    okBOOST, boxBOOST = BOOSTING.update(frame)
    okMIL, boxMIL = MIL.update(frame)
    okKCF, boxKCF = KCF.update(frame)
    okTLD, boxTLD = TLD.update(frame)
    okMF, boxMF = MEDIANFLOW.update(frame)
    okMOSSE, boxMOSSE = MOSSE.update(frame)
    okCSRT, boxCSRT = CSRT.update(frame)


    # Calculate Frames per second (FPS)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);

    # Draw bounding box
    if okBOOST:
        # Tracking success
        p1 = (int(boxBOOST[0]), int(boxBOOST[1]))
        p2 = (int(boxBOOST[0] + boxBOOST[2]), int(boxBOOST[1] + boxBOOST[3]))
        cv2.rectangle(frame, p1, p2, (0, 0, 255), 2, 1)
    else:
        # Tracking failure
        cv2.putText(frame, "[BOOSTING]Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    if okMIL:
        # Tracking success
        p1 = (int(boxMIL[0]), int(boxMIL[1]))
        p2 = (int(boxMIL[0] + boxMIL[2]), int(boxMIL[1] + boxMIL[3]))
        cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
    else:
        # Tracking failure
        cv2.putText(frame, "[MIL] Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 0), 2)

    if okKCF:
        # Tracking success
        p1 = (int(boxKCF[0]), int(boxKCF[1]))
        p2 = (int(boxKCF[0] + boxKCF[2]), int(boxKCF[1] + boxKCF[3]))
        cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
    else:
        # Tracking failure
        cv2.putText(frame, "[KCF]Tracking failure detected", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255,255, 0), 2)

    if okTLD:
        # Tracking success
        p1 = (int(boxTLD[0]), int(boxTLD[1]))
        p2 = (int(boxTLD[0] + boxTLD[2]), int(boxTLD[1] + boxTLD[3]))
        cv2.rectangle(frame, p1, p2, (185,255, 63), 2, 1)
    else:
        # Tracking failure
        cv2.putText(frame, "[TLD]Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (185,255, 63), 2)

    if okMF:
        # Tracking success
        p1 = (int(boxMF[0]), int(boxMF[1]))
        p2 = (int(boxMF[0] + boxMF[2]), int(boxMF[1] + boxMF[3]))
        cv2.rectangle(frame, p1, p2, (0,13, 115), 2, 1)
    else:
        # Tracking failure
        cv2.putText(frame, "[MF]Tracking failure detected", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,13, 115), 2)

    if okMOSSE:
        # Tracking success
        p1 = (int(boxMOSSE[0]), int(boxMOSSE[1]))
        p2 = (int(boxMOSSE[0] + boxMOSSE[2]), int(boxMOSSE[1] + boxMOSSE[3]))
        cv2.rectangle(frame, p1, p2, (220,60, 227), 2, 1)
    else:
        # Tracking failure
        cv2.putText(frame, "[MOSSE]Tracking failure detected", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (220,60, 227), 2)


    if okCSRT:
        # Tracking success
        p1 = (int(boxCSRT[0]), int(boxCSRT[1]))
        p2 = (int(boxCSRT[0] + boxCSRT[2]), int(boxCSRT[1] + boxCSRT[3]))
        cv2.rectangle(frame, p1, p2, (0, 255, 0), 2, 1)
    else:
        # Tracking failure
        cv2.putText(frame, "Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)






    # Display tracker type on frame
    cv2.putText(frame, "BOOSTING", (10, 318), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2);
    cv2.putText(frame, "MIL", (10, 340), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 0), 2);
    cv2.putText(frame, "KCF", (10, 362), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255,255, 0), 2);
    cv2.putText(frame, "TLD", (10, 384), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (185,255, 63), 2);
    cv2.putText(frame, "MF", (10, 406), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,13, 115), 2);
    cv2.putText(frame, "MOSSE", (10, 428), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (220,60, 227), 2);
    cv2.putText(frame, "CSRT", (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2);





    # Display FPS on frame
    cv2.putText(frame, "FPS : " + str(int(fps)), (10, 24), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2);

    # Display result
    cv2.imshow("Tracking", frame)



    count+=1
    # Exit if ESC pressed
    k = cv2.waitKey(1) & 0xff
    if k == 27 or count==endFrame:
        break

