from PIL import Image
import os

# !! Access Path ONLY with Folders.
# * EDIT Path HERE
path = "."

files = os.listdir(path)
image_list = [f for f in files if f.endswith(('jpg','png'))]
webp_list = [f for f in files if f.endswith('webp')]

for i in range( len(webp_list) ):
    webp_list[i] = webp_list[i].split(".")[0]

def convert_image(path, image_path):
    im = Image.open(path + '/' + image_path)
    im = im.convert("RGB")

    split_path = image_path.split(".")
    image_name = split_path[0]
    old_suffix = split_path[1]

    new_im_path = path + '/' + image_name + ".webp"
    im.save(new_im_path, "webp")

    print(f"Convert '{image_name}.{old_suffix}' To '{image_name}.webp' : SUCCESS")

cnt = 0

for image in image_list:
    name = image.split(".")[0]
    ck = False
    for i in webp_list:
        # Convert Check
        if i == name:
            ck = True
            break

    # Already Convert: Skip
    if ck:
        continue
    # Not yet: Convert
    else:
        convert_image(path, image)
        cnt += 1

if cnt > 0:
    print("Finish")
else:
    print("Cannot Find PNG or JPG file \nOR Those files have been CONVERTED")