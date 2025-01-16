from ultralytics import YOLO

model = YOLO("path/to/your.pt")

results = model.train(data="path/to/your/data.yaml", epochs=300, device=0, batch = 16)