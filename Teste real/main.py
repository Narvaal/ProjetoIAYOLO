import cv2 
import time
import numpy as np


COLORS = [(0,255,0),(0,0,255),(255,0,0)]

class_names = []
cname = ''
with open("C:\\Users\Ale\\Documents\\Code\\Python\\ProjetoIAgit\\ProjetoIA\\labels.txt","r") as f:
    class_names = [cname.strip() for cname in f.readlines()]

cap = cv2.VideoCapture("C:\\Users\\Ale\\Documents\\Code\\Python\\ProjetoIAgit\\ProjetoIA\\Teste real\\data2.MP4")

weights = "C:\\Users\\Ale\\Documents\\Code\\Python\\ProjetoIAgit\\ProjetoIA\\backup\\projetoYolo_last.weights"
conf = "C:\\Users\\Ale\\Documents\\Code\\Python\\ProjetoIAgit\\ProjetoIA\\projetoYolo.cfg"
destino = "C:\\Users\\Ale\\Desktop\\Saida"

writer = cv2.VideoWriter(destino + '\\output.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 20,(640,480))

net = cv2.dnn.readNet(weights,conf)
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(416,416),scale=1/255)

while True:

        ret, frame = cap.read()

        if ret == True:

            classes, scores, boxes = model.detect(frame,0.1,0.2)

            for(classid,score,box) in zip(classes,scores,boxes):

                color = COLORS[int(classid) % len(COLORS)]

                label = f"{class_names[classid]} : {score}"

                cv2.rectangle(frame,box,color,2)

                cv2.putText(frame,label,(box[0],box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color,2)
            
                #writer.write(frame)

            cv2.imshow("detections",frame)

            if cv2.waitKey(1) == 27:
                break

cap.realease()
cv2.destroyAllWindows()