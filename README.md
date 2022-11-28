
# Thesis SSSUP December 2022
The repositories contains files to run the experiments descripted in the thesis wrote by Lorenzo Collodi for the final exam for the II level diploma at Sant'Anna School of Advanced Studies.
## Structure
The repository contains several folders as follows:
Annotation: contains the .txt filts with the annotated data for benchmark
Data: the data from UFDD and WIDER organized in subfolders
make_datasets: files used to label and move files from UFDD and WIDER
Predictions: the predictions obtained with the models used for evaluation
scripts: scripts for useful operations
utils: the actual files for evaluation

## Dependencies
The environment relies on installation opencv-python for drawing the images, but the tests are run on colab, so the dependencies are resolved in the notebook.

## How to use:
Clone the repository locally with `git clone https://github.com/lorenzocollodi/face_detection_eval.git`.
Open the colab notebook (.ipynb file) in Google Colab. Then run all the cells to run the speed tests and extract the predictions.
There is no way to run locally at the moment.
To get the final mIoU values, download the predictions, put them in the Predictions folder and run `python scripts/calculate_mIoU.py` and the scores will be printed. In case you want to evaluate your own model extract a predictions file in the same format as those provided and add your model in the evaluation file (calculate_mIoU.py).


The code is adapted from [LearnOpenCV](https://github.com/spmallick/learnopencv/blob/master/Face-Detection-Ultimate-Guide/face_detection_inference_combined.ipynb)
