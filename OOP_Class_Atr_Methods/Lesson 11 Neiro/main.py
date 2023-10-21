from Recognizeimg import RecognizeImg
path = 'Img/cat.png'
winName = 'cat'
fileName = 'haarcascade_frontalcatface_extended.xml'
# 1
rec = RecognizeImg(path)
#rec.ShowImg(winName)
#2
rec.GetCoordinates(fileName)
#print(rec.MultiScale)
#3
#rec.HighLight()
#rec.ShowImg(winName)
#4
newPath = 'Img/glasses.png'
newPhotoPath = 'Img/cat_with_glasses.png'
rec.AddImage(newPath, newPhotoPath)
rec.ShowImg('AddImage Cat')