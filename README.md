# README.md

Data preparing
-------------
```bash
$ git clone https://github.com/cghero-fi/HW2_yolov5.git
$ cd HW2_yolov5
```
download train.zip and test.zip and unzip it in HW2_yolov5/
convert the labels to yolo-txt format
```bash
python mat2yolo.py
```
all the label will save in HW2_yolov5/labels/

Training
-------------
```bash
$ git clone https://github.com/ultralytics/yolov5
$ cd yolov5
$ pip install -r requirements.txt
```
put all the images and labels in the format below
also need to copy the file HW2_yolov5/data.yaml into this folder

```bash
├── yolov5
	  ├── train.py
  	├── detect.py
  	├── ...
	
├── train
  	├── images
		 ├── 1.png
		 ├── ...
		
  	└── labels
		 ├── 1.txt
		 ├── ...
├── valid
  	├── images
		 ├── 28000.png
		 ├── ...
		
  	└── labels
		 ├── 28000.txt
		 ├── ...
├── test
  	└── images
		 ├── 117.png
		 ├── ...
└──data.yaml

```

and use the train.py to training
```bash
$ cd yolov5
$ python train.py --img 512 --batch 32 --epochs 00 --data '../data.yaml' --cfg ./models/yolov5s.yaml --weights '' --name yolov5s --cache
$ python train.py --img 512 --batch 32 --epochs 00 --data '../data.yaml' --cfg ./models/yolov5x.yaml --weights '' --name yolov5x --cache
```
the weights will be saved in "yolov5/runs/train/yolov5s/weights/best.pt" and "yolov5/runs/train/yolov5x/weights/best.pt" 

Testing (detecting)
-------------
```bash
$ cd yolov5
$ python detect.py --weights runs/train/yolov5s/weights/best.pt --img 512 --source ../test/images --save-txt --save-conf --name yolov5s
$ python detect.py --weights runs/train/yolov5x/weights/best.pt --img 512 --source ../test/images --save-txt --save-conf --name yolov5x
```
the labels will be saved in "yolov5/runs/detect/yolov5s/labels/" and "yolov5/runs/detect/yolov5x/labels/" 

see more details in colab 
https://colab.research.google.com/drive/1tnQbcZ0CpAIrBDii7-_HOfW7_zF-LoQM?authuser=1#scrollTo=otPgm84G8usO
