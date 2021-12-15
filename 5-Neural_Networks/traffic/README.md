# 5 - Neural Networks - Traffic

## Explanations

To start with a base, I try with the same model we used for the MNIST handwrited digits and the result was bad. Then I have read about the popular model LeNet-5 and implement it, the result was very good. With this good base, I tried some modifications on the model (details below).

My observations on these experimentations was : The single 128 units hidden layer wasn't the problem on the handwriting model and the relu activation function was also good. The problem was primarly the convolution/pooling steps, the average pooling is way better then max pooling and 2 convolution + 2 pooling seems to be better then 1.

So, I tried and found a good model with these specifications :

- Convolutional 32 filters, 3x3 kernel, relu
- Average-pooling 2x2
- Convolutional 32 filters, 3x3 kernel, relu
- Average-pooling 2x2
- Flatten
- Hidden Dense 128 - relu
- Dropout 0.5
- Output Dense NUM_CATEGORIES - softmax

The accuracy on the evaluation step is : 0.9835.

Better then classic LeNet-5.

All my experimentations steps are below in the Model section.

## Model

### First, start with the same as handwriting :

- Convolutional 32 filters, 3x3 kernel
- Max-pooling 2x2
- Flatten
- Hidden Dense 128 - relu
- Dropout 0.5
- Output Dense NUM_CATEGORIES - softmax

10th Epoch accuracy : 0.0558
Evaluation accuracy : 0.0549

Very bad. Try with replacing relu activation by tanh, the difference is ridiculous:

10th Epoch accuracy : 0.0514
Evaluation accuracy : 0.0545


### Try with LeNet - 5 :

https://datahacker.rs/deep-learning-lenet-5-architecture/

- Convolutional 6 filters, 5x5 kernel
- Average-pooling 2x2
- Convolutional 16 filters, 5x5 kernel
- Average-pooling 2x2
- Flatten
- Hidden Dense 120 - tanh
- Hidden Dense 84 - tanh
- Dropout 0.5
- Output Dense NUM_CATEGORIES - softmax

10th Epoch accuracy : 0.9525
Evaluation accuracy : 0.9561

Try with relu instead of tanh :

10th Epoch accuracy : 0.9253
Evaluation accuracy : 0.9679

Little difference, we can keep relu

### LeNet convolution/pooling - 1 hidden 128 units :

- Convolutional 6 filters, 5x5 kernel
- Average-pooling 2x2
- Convolutional 16 filters, 5x5 kernel
- Average-pooling 2x2
- Flatten
- Hidden Dense 128 - relu
- Dropout 0.5
- Output Dense NUM_CATEGORIES - softmax

10th Epoch accuracy : 0.9506
Evaluation accuracy : 0.9825

Good. The difference seems to be in the convolution/pooling

### LeNet convolution- 1 hidden 128 units - MaxPooling:

- Convolutional 6 filters, 5x5 kernel
- Max-pooling 2x2
- Convolutional 16 filters, 5x5 kernel
- Max-pooling 2x2
- Flatten
- Hidden Dense 128 - relu
- Dropout 0.5
- Output Dense NUM_CATEGORIES - softmax

10th Epoch accuracy : 0.8569
Evaluation accuracy : 0.9224

The AveragePooling is better then MaxPooling

### Average pooling - Convolutional 32x2 3x3 - 1 hidden 128 units :

- Convolutional 32 filters, 3x3 kernel
- Average-pooling 2x2
- Convolutional 32 filters, 3x3 kernel
- Average-pooling 2x2
- Flatten
- Hidden Dense 128 - relu
- Dropout 0.5
- Output Dense NUM_CATEGORIES - softmax

10th Epoch accuracy : 0.9443
Evaluation accuracy : 0.9835

Little better, the important seems to be 2 convolution and 2 pooling instead of 1 in the base model

### LeNet - 1 hidden 128 units - Convolutional 32x3 3x3:

- Convolutional 32 filters, 3x3 kernel
- Average-pooling 2x2
- Convolutional 32 filters, 3x3 kernel
- Average-pooling 2x2
- Convolutional 32 filters, 3x3 kernel
- Average-pooling 2x2
- Flatten
- Hidden Dense 128 - relu
- Dropout 0.5
- Output Dense NUM_CATEGORIES - softmax

Just to try what happens if we add more convolution and pooling

10th Epoch accuracy : 0.9469
Evaluation accuracy : 0.9758

Not big difference

### LeNet - 1 hidden 128 units - Mixed Average + Max pooling :

- Convolutional 32 filters, 3x3 kernel
- Average-pooling 2x2
- Convolutional 32 filters, 3x3 kernel
- Max-pooling 2x2
- Flatten
- Hidden Dense 128 - relu
- Dropout 0.5
- Output Dense NUM_CATEGORIES - softmax

10th Epoch accuracy : 0.9250
Evaluation accuracy : 0.9558

Not big difference