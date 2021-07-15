# 0. "resnet50_coco_best_v2.1.0.h5" 다운로드
1. 다음 링크에 접속 [keras_retinanet](https://github.com/fizyr/keras-retinanet/releases)
2. "resnet50_coco_best_v2.1.0.h5 다운로드

# 1. 데이터셋 변환 
(참고: https://www.tensorflow.org/tutorials/load_data/images?hl=ko)
1. google drive에 있는 pretrained 된 가구 이미지 데이터와 라벨를 다운
2. 가구 이미지 데이터와 라벨을 이용해 training dataset으로 변환 
   (이때, 512x512 해상도로 전처리, class = {"러그", "수납장", "침대"})
   
# 2. resnet 전이학습
(참고: https://www.tensorflow.org/tutorials/images/transfer_learning?hl=ko)

# 3. retinanet
이후 전이학습된 resnet을 "resnet50_coco_best_v2.1.0.h5" 대신 retinanet에 사용
