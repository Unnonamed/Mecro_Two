import torch
import torchvision
import torchvision.transforms as transforms

import matplotlib.pyplot as plt
import numpy as np
import cv2

# CIFAR10 불러오고 정규화 하기
transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

trainset = torchvision.datasets.CIFAR10(root='./data', train=True,
                                        download=False, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=4,
                                          shuffle=True, num_workers=2)

# testset = torchvision.datasets.CIFAR10(root='./data', train=False,
#                                        download=True, transform=transform) #다운로드만 할때 train = False , download = True
# testloader = torch.utils.data.DataLoader(testset, batch_size=4,
#                                          shuffle=False, num_workers=2)
classes = ('plane', 'car', 'bird', 'cat',
           'deer', 'dog', 'frog', 'horse', 'ship', 'truck')


# 이미지를 보여주기 위한 함수
def imshow(img):
    img = img / 2 + 0.5     #정규화 해제(unnormalize)
    npimg = img.numpy() 
    print(img.shape) #(3, 36, 138)
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    #plt.imshow(cv2.resize(np.transpose(npimg, (1, 2, 0)), (4000, 1000)))

def checkCuda():
    # 학습에 사용할 CPU나 GPU 장치를 얻습니다.
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using {device} device")

    if torch.cuda.is_available():
        #tensor = torch.Tensor.to("cuda")
        #  Returns the index of a currently selected device.
        torch.cuda.current_device()
        #  0
        #  Returns the number of GPUs available.
        torch.cuda.device_count()
        #  1
        #  Gets the name of a device.
        torch.cuda.get_device_name(0)

    
def main():
    checkCuda()
    # 학습용 이미지를 무작위로 가져오기
    dataiter = iter(trainloader)
    images, labels = dataiter.next()

    # 이미지 보여주기
    imshow(torchvision.utils.make_grid(images))
    # 정답(label) 출력
    print(' '.join('%5s' % classes[labels[j]] for j in range(4)))
    
if __name__ == '__main__':
    main()
    plt.show()