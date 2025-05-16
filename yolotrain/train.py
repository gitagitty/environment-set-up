from ultralytics import YOLO

model = YOLO("/home/evan/tutorial-2024.10/yolotrain/yolov8s.pt")

results = model.train(data="/home/evan/tutorial-2024.10/yolotrain/dc/data.yaml", 
                      epochs=300, 
                      device=0, 
                      batch = 16
                      resume=False, #是否继续训练
                      project='runs/detect', # save_dir='project/name',
                      name='train',
                      )

