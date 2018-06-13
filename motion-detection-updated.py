import cv2

while True:
  camera = cv2.VideoCapture(0)
  return_value, image = camera.read()
  return_value, image2 = camera.read()
  cv2.imwrite('opencv.png', image)
  cv2.imwrite('opencv1.png', image2)
  file1 = open('opencv.png','rb')
  f1 =  file1.read()
  file2 = open('opencv1.png','rb')
  f2 = file2.read()
  if f1 != f2:
    print('dont move!')
  else:
    print("nothing is moving")
  del(camera)
  
  file1.close()
  file2.close()
