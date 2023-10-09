from ultralytics import YOLO

model = YOLO('yolov8n-pose.pt') 
#model = YOLO('yolov8n-pose.yaml') # create model from scratch

results = model.train(data='yolo_config/config.yaml', epochs=50, imgsz=640)
