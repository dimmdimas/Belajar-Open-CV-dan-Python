import cv2

citraRGB = cv2.imread('./foto/individu.jpg')
citraAbu2 = cv2.cvtColor(citraRGB, cv2.COLOR_RGB2GRAY)

cv2.imshow('Gambar berwarna', citraRGB)
cv2.imshow('Gambar berskala keabu-abuan', citraAbu2)

cv2.waitKey(0)
cv2.destroyAllWindows()