from statistics import median
from numpy import average


# Import Image from wand.image module
from wand.image import Image

# Read image using Image() function
with Image(filename="desktop.jpg") as img:

    # Generate noise image using spread() function
    # Here it generated poisson noise
    img.noise("poisson", attenuate=0.9)
    img.save(filename="noisedesktop.jpg")


# Read image using Image() function
with Image(filename="desktop.jpg") as img:

    # Generate noise image using spread() function
    # Here it generated laplacian noise
    img.noise("laplacian", attenuate=2.0)
    img.save(filename="noisedesktop2.jpg")
