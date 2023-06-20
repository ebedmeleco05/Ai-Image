import cv2
import numpy as np

# Charger l'image et la convertir en niveaux de gris
image = cv2.imread('image.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Créer un masque binaire du corps humain en utilisant la soustraction de fond
_, mask = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Créer une silhouette du corps humain en mettant tous les pixels de premier plan en noir
silhouette = image.copy()
silhouette[np.where(mask == 255)] = 0

# Enregistrer la silhouette résultante
cv2.imwrite('silhouette.png', silhouette)
