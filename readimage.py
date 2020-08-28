"""
使用opencv轉換成 tensorflow格式 [Batch index,Width,Height,Channel]
Aug 29 00:59 練習
"""
import numpy
import cv2
from os import listdir
from os.path import isfile, join
from matplotlib import pyplot as plt
"""
cv2.IMREAD_COLOR :
此為預設值，這種格式會讀取 RGB 三個 channels 的彩色圖片，而忽略透明度的 channel
cv2.IMREAD_GRAYSCALE :
以灰階的格式來讀取圖片
cv2.IMREAD_UNCHANGED :
讀取圖片中所有的 channels，包含透明度的 channel
"""
# 讀取單一文件
"""
img = cv2.imread("C:/Users/jimmy/Downloads/MNIST/output/training/0/1.jpg", cv2.IMREAD_GRAYSCALE)
print(img.shape)
print(type(img))
"""
# 顯示圖片
"""
cv2.imshow("ImageWindow", img)
cv2.waitKey(0)
"""
# 彙整機料夾(數字0)檔案成一個 numpy array
"""
mypath="C:/Users/jimmy/Downloads/MNIST/output/training/0/"
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
images = numpy.empty(len(onlyfiles), dtype=object)
for n in range(0, len(onlyfiles)):
  images[n] = cv2.imread(join(mypath, onlyfiles[n]))
numpy.save('images0_np', images)
"""
#讀取彙整.npy
"""
image_0 = numpy.load("images0_np.npy", allow_pickle=True)
print("images0_np.npy的shape: ", image_0.shape)
print("image_0[0] 的shape: ", image_0[0].shape)
# 使用 Matplotlib 顯示圖片
plt.imshow(image_0[0])
plt.show()
"""
# 轉換成tensorflow格式 [Batch index,Width,Height,Channel]
"""
image_0 = numpy.load("images0_np.npy", allow_pickle=True)
image_0np = numpy.zeros((len(image_0), 28, 28, 3))
for i in range(len(image_0)):
  image_0np[i, :, :, :] = image_0[i]
numpy.save("image_0np", image_0np)
"""
# 顯示tensorflow格式 [Batch index,Width,Height,Channel]
image_0List = numpy.load("image_0np.npy")
print(image_0List.shape)




