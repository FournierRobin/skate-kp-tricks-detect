from ultralytics import YOLO

model = YOLO('yolov8n-pose.pt') 
#model = YOLO('yolov8n-pose.yaml') # load a pretrained model (recommended for training)

results = model.train(data='yolo_config/config.yaml', epochs=50, imgsz=640)
#results = model(source="datasets/videos/SLS_only_skate_test.mov", conf=0.2, save=True)
