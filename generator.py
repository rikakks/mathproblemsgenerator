from PIL import Image
from random import randint

print("Hello, this program will give you a random problem from the past William Lowell Putnam mathematical competitions.")

Image.open('problems/' + str(randint(1, 24)) + '.png').show()
