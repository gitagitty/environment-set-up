import onnx
from onnxsim import simplify

def simplify_onnx_model(input_model_path, output_model_path):
    # 加载原始 ONNX 模型
    model = onnx.load(input_model_path)
    
    # 使用 onnx-simplifier 简化模型
    model_simplified, check = simplify(model)
    
    # 检查简化是否成功
    if check:
        print("模型简化成功！")
    else:
        print("模型简化失败，可能存在问题。")
    
    # 保存简化后的模型
    onnx.save(model_simplified, output_model_path)
    print(f"简化后的模型已保存为 {output_model_path}")

if __name__ == "__main__":
    input_model = '/home/evan/yolotrain/runs/detect/robocon2025yolov8s v1/weights/best.onnx'  # 输入模型路径
    output_model = '/home/evan/yolotrain/runs/detect/robocon2025yolov8s v1/weights/best_sim.onnx'  # 输出简化后的模型路径
    
    simplify_onnx_model(input_model, output_model)
