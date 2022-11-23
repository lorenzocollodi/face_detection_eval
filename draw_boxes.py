from read_utils import read_file_key
from random import shuffle, choice
import cv2 as cv

models = ["MP", "DSFD", "Retina", "YuNet"]
keys = [("Accessories/Yes", "annotated_accessories"), ("Accessories/No", "annotated_accessories"), ("Expression/Normal", "annotated_expression"), ("Expression/Extreme", "annotated_expression"), ("Ethnics/Asian", "annotated_ethnics"), ("Ethnics/African", "annotated_ethnics"), ("Ethnics/Caucasian", "annotated_ethnics"), ("Light/Regular", "annotated_light"), ("Light/Irregular", "annotated_light"), ("Pose/Normal", "annotated_pose"), ("Pose/Extreme", "annotated_pose")]
keys = [("Accessories/Yes", "annotated_accessories")]
if __name__ == "__main__":
    for key, file_gt in keys:
        file_gt = f"/Users/lorenzocollodi/Desktop/Tesi Sant'Anna/Eval/Data/{file_gt}.txt"
        gt_boxes = read_file_key(file_gt, key)
        boxes_list = list(gt_boxes.keys())
        k = 0
        while not k == (ord('s')):
            random_img = choice(boxes_list)
            img = cv.imread(random_img)
            cv.imshow("Window", img)
            k = cv.waitKey(-1)
        for model in models:
            file_pred = f"/Users/lorenzocollodi/Desktop/Tesi Sant'Anna/Eval/Data/{model}_predictions.txt"
            pred_boxes = read_file_key(file_pred, key)
            img = cv.imread(random_img)
            for face in gt_boxes[random_img]:
                img = cv.rectangle(img, face, (0,255,0), 2)
            for face in pred_boxes[random_img]:
                img = cv.rectangle(img, face, (0,0,255), 2)
            cv.imwrite(f"/Users/lorenzocollodi/Desktop/Tesi Sant'Anna/Eval/Data/Drawn/{model}_{key.replace('/', '_')}.jpg", img)
