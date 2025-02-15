import os
from roboflow import Roboflow

rf = Roboflow(api_key="0BFh7BExBxN900JOWa0e")
project = rf.workspace().project("test1-5dpoy")
model = project.version(1).model

input_folder = "D:/Flower_Detection/input"
output_folder = "D:/Flower_Detection/output" 

input_files = os.listdir(input_folder)

for i in input_files:
    input_path = os.path.join(input_folder, i)
    output_path = os.path.join(output_folder, f"prediction_{i}")

    print(model.predict(input_path, confidence=40, overlap=30).json())

    prediction = model.predict(input_path, confidence=40, overlap=30)

    prediction.save(output_path)
    print(i)
