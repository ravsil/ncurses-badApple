from PIL import Image
import json


def transformImage(img):
    image = Image.open(img)

    color1 = []
    color2 = []
    width, height = image.size
    i = 0
    n1 = 0
    n2 = 0
    first = True
    for y in range(height):
        for x in range(width):

            rgb = image.getpixel((x, y))
            rgb = (rgb[0], rgb[1], rgb[2])

            if i % 64 == 0:
                i = 0
                if first:
                    first = False
                else:
                    color1.append(n1)
                    color2.append(n2)
                    n1 = 0
                    n2 = 0
            i += 1

            if rgb == (0, 0, 0):
                pass
            elif rgb == (255, 255, 255):
                n1 = n1 + (1 << i - 1)
            else:
                n2 = n2 + (1 << (i - 1))

    color1.append(n1)
    color2.append(n2)
    output = [color1, color2]
    return output


frames = []
for i in range(6584):
    output = tranformImage(f"frames/{i}.png")
    frames.append(output)
    print(f"Done {i} images!")


with open(f"codes.json", "w") as f:
    f.write(json.dumps(frames))
