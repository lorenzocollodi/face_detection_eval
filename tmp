# SSD
detector_SSD = cv2.dnn.DetectionModel("res10_300x300_ssd_iter_140000_fp16.caffemodel", 
                                      "deploy.prototxt")

# MTCNN
detector_MTCNN = MTCNN()

# DSFD
detector_DSFD = face_detection.build_detector("DSFDDetector", 
                                              confidence_threshold=.5, 
                                              nms_iou_threshold=.3)

# Retina
detector_Retina = face_detection.build_detector("RetinaNetResNet50", 
                                                confidence_threshold=.5, 
                                                nms_iou_threshold=.3)

# MediaPipa
mp_face_detection = mp.solutions.face_detection
detector_MP = mp_face_detection.FaceDetection(model_selection=1, 
                                              min_detection_confidence=0.4)
