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
    #print(img.shape) #(3, 36, 138)
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
        #  Returns the number of GPUs available.
        torch.cuda.device_count()
        #  Gets the name of a device.
        torch.cuda.get_device_name(0)


class Net(torch.nn.Module):
    def __init__(self):
        super(Net, self).__init__()

        #input = 3, output = 6, kernal = 5
        self.conv1 = torch.nn.Conv2d(3, 6, 5)
        #kernal = 2, stride = 2, padding = 0 (default)
        self.pool = torch.nn.MaxPool2d(2, 2)
        self.conv2 = torch.nn.Conv2d(6, 16, 5)
        #input feature, output feature
        self.fc1 = torch.nn.Linear(16 * 5 * 5, 120)
        self.fc2 = torch.nn.Linear(120, 84)
        self.fc3 = torch.nn.Linear(84, 10)

    # 값 계산
    def forward(self, x):
        x = self.pool(torch.nn.functional.relu(self.conv1(x)))
        x = self.pool(torch.nn.functional.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = torch.nn.functional.relu(self.fc1(x))
        x = torch.nn.functional.relu(self.fc2(x))
        x = self.fc3(x)
        return x


net = Net()


def train():
    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(net.parameters(), lr=0.001, momentum=0.9)
    
    for epoch in range(10):  #데이터셋 2번 받기

        running_loss = 0.0
    
        for i, data in enumerate(trainloader, 0):
            # 입력 받기 (데이터 [입력, 라벨(정답)]으로 이루어짐)
            inputs, labels = data

            #학습
            optimizer.zero_grad()
            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            # 결과 출력
            running_loss += loss.item()
            if i % 2000 == 1999:    # print every 2000개마다
                print('[%d, %5d] loss: %.3f' %
                    (epoch + 1, i + 1, running_loss / 2000))
                running_loss = 0.0

    print('Finished Training')

    #여기에 학습한 모델 저장
    PATH = './cifar_net.pth'
    torch.save(net.state_dict(), PATH)

def main():
    checkCuda()
    # 학습용 이미지를 무작위로 가져오기
    dataiter = iter(trainloader)
    images, labels = dataiter.next()

    # 이미지 보여주기
    imshow(torchvision.utils.make_grid(images))
    # 정답(label) 출력
    print(' '.join('%5s' % classes[labels[j]] for j in range(4)))
    
    #train()
    # 학습한 모델로 예측값 뽑아보기
    net = Net()
    net.load_state_dict(torch.load('./cifar_net.pth'))
    outputs = net(images)
    _, predicted = torch.max(outputs, 1)

    print('Predicted: ', ' '.join('%5s' % classes[predicted[j]]for j in range(4)))

    correct = 0
    total = 0
    with torch.no_grad():
        for data in trainloader:
            images, labels = data
            outputs = net(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    print('Accuracy of the network on the 10000 test images: %d %%' % (
        100 * correct / total))
if __name__ == '__main__':
    main()
    plt.show()