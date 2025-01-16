from ultralytics import YOLO

model = YOLO("path/to/your.pt", task="detect") # pt模型路径
path = model.export(format="onnx", simplify=True, device=0, opset=12, dynamic=False, imgsz=640)# 在原父目录生成onnx模型