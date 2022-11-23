from eval_utils import getmIoU
from read_utils import read_file_key

models = ["DSFD", "Retina", "MP", "YuNet"]
keys = [("Accessories/Yes", "annotated_accessories"), ("Accessories/No", "annotated_accessories"), ("Expression/Normal", "annotated_expression"), ("Expression/Extreme", "annotated_expression"), ("Ethnics/Asian", "annotated_ethnics"), ("Ethnics/African", "annotated_ethnics"), ("Ethnics/Caucasian", "annotated_ethnics"), ("Light/Regular", "annotated_light"), ("Light/Irregular", "annotated_light"), ("Pose/Normal", "annotated_pose"), ("Pose/Extreme", "annotated_pose")]


if __name__ == "__main__":
    for key, file_gt in keys:
        file_gt = f"/Users/lorenzocollodi/Desktop/Tesi Sant'Anna/Eval/Data/{file_gt}.txt"
        for model in models:
            file_pred = f"/Users/lorenzocollodi/Desktop/Tesi Sant'Anna/Eval/Data/{model}_predictions.txt"
            gt_boxes = read_file_key(file_gt, key)
            pred_boxes = read_file_key(file_pred, key)
            mIoU = getmIoU(gt_boxes, pred_boxes)
            print(f"{model} scored {round(mIoU, 2)} on {key}")