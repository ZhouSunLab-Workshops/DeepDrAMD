# DeepDrAMD
code for deep learning on color fundus photographs for early detection AMD performance, classifying dryAMD and wetAMD and distinguish wetAMD type1 or type2
notification
Here,we provide three trained model, the'pth' files are available at baidu pan https://pan.baidu.com/s/1oMZiPR6OXdRXDdMf4uvi8g 
Extracted code：1111

## Requirements
pip install -r requirements.txt
## data
WMUEH is available from the corresponding author upon reasonable request
ODIR Ocular Disease Intelligent Recognition.
ichallenge-AMD(ADAM cohorts)

## How to train/evalute models

The code we submitted is mainly for everyone to predict the images. If you want to train, you need to adjust the code
### train:
First, place the training test images in the dataset folder, then place the corresponding txt file in the data folder, modify the parameters in the model folder, and finally train the model through the command line 

> python tools/train.py models/swin_transformer/base_384.py


### evaluate：
If you want to evaluate a trained model, you need to first create the model's configuration file data in the model folder_ Change the path for test in cfg to the path where you want to evaluate 'pth'
for example:
> ckpt = 'logs/SwinTransformer/2022-08-25-08-13-31/Val_Epoch067-Acc95.411.pth'

finally,evaluate the model using the command line 

 > python tools/evaluation.py models/swin_transformer/base_384.py

Ensure that the images in the dataset correspond to the txt file in the datas, as examples have been provided in the folder，Test.txt may not provide a true label.The predicted results are in eval_results folder, you can open it and view it yourself
 ## Reproduction results
 If you want to reproduce the results of the article, you can copy the model configuration file in the log folder and replace it with the model configuration file in the models. Then, modify the corresponding CKPT path, dataset, and content in the data folder, and follow the evaluation process once again
 
 ## data augmentation methods:
 If you want to use image enhancement during training, you can copy the files in the data augmentation folder (choose one of two methods) to the utils folder instead of the train_ Utils. py. and rename the name to train_ utils.py.
 
 ## Acknowledgements
 The implementation of baseline was based on https://github.com/fafa-dl/awesome-backbones, We have made improvements using his main code.Thanks a lot for the author's open source
