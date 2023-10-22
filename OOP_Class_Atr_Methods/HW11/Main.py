from Neiro import RecognizeImg

path = 'Img/Cat2.jpg'
winName = 'cat'
fileName = 'haarcascade_frontalcatface_extended.xml'

rec = RecognizeImg(path)
rec.GetCoordinates(fileName)


newPath = 'Img/glasses.png'
newPhotoPath = 'Img/cat_with_glasses.png'
rec.AddImage(newPath, newPhotoPath)
rec.ShowImg('AddImage Cat')