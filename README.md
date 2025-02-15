# **Flower Detection using Roboflow**

### Overview :

This project utilizes Roboflow's object detection API to detect flowers in images. The script loads a flower detection model from Roboflow, processes images from an input folder, and saves the predictions in an output folder.


### Features :

* Uses the Roboflow API for flower detection.

* Processes multiple images in a specified input directory.

* Saves detection results with confidence and overlap thresholds.

* Outputs predictions in JSON format.


### Prerequisites :

1. Python 3.x installed

2. Roboflow Python package installed (pip install roboflow)

3. API key for Roboflow


### Install dependencies:

      pip install roboflow

      
### Set up the input and output folders:


* Place images to be processed inside the input folder.

* The script will create an output folder if it does not exist.


### Configuration:
Modify the following variables in the script as needed:
    
* input_folder = "D:/Flower_Detection/input"

* output_folder = "D:/Flower_Detection/output"
      
* confidence_threshold = 40  # Confidence threshold for predictions
      
* overlap_threshold = 30  # Overlap threshold for multiple detections

### Output :

* The script prints the predictions for each image in JSON format.

* The predictions are also saved in the output folder with filenames prefixed by prediction_.
      

### Notes :

* Ensure that your Roboflow API key is correct and that you have access to the test1-5dpoy project.

* The script is set to use version 1 of the model. Update the script if a different version is needed.
