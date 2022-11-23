def IoU(boxA, boxB):
    a = boxA[2]*boxA[3]
    b = boxB[2]*boxB[3]
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2]+boxA[0], boxB[2]+boxB[0])
    yB = min(boxA[3]+boxA[1], boxB[3]+boxB[1])
    I = max(0, xB - xA) * max(0, yB - yA)
    return I/((a+b)-I)

def imgIoU(GT, predictions):
    tot_faces = max(len(GT), len(predictions))
    totIoU = 0
    for face in GT:
        predictions = sorted(predictions, key=lambda x: IoU(face, x), reverse=True)
        if len(predictions) > 0:
            totIoU += IoU(face, predictions[0])
            predictions = predictions[1:]
    return totIoU, tot_faces

def getmIoU(gt_boxes, pred_boxes):
    tot_IoU = 0
    tot_faces = 0
    for key in gt_boxes.keys():
        _IoU, _faces = imgIoU(gt_boxes[key], pred_boxes[key])
        tot_IoU += _IoU
        tot_faces += _faces
    return tot_IoU/tot_faces
