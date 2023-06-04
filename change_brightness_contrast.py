from PIL import Image, ImageEnhance
import os
import sys

if len(sys.argv) < 2:
    print('Please provide an argument.')
else:
    obj = sys.argv[1]
    print(f'The argument you provided is: {obj}')

    # define the input and output directories
    input_dir = obj
    output_dir = f'{obj}_modified'

    # create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # define the brightness and contrast values to use
    brightness = 0.5  # increase brightness by 50%
    contrast = 0.5  # increase contrast by 20%

    # loop through each image file in the input directory
    for filename in os.listdir(input_dir):
        # load the image and apply the brightness and contrast adjustments
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        with Image.open(input_path) as img:
            img = img.point(lambda x: x * brightness)  # adjust brightness
            img = ImageEnhance.Contrast(img).enhance(contrast)  # adjust contrast
            img.save(output_path)
            print(f'Saved image {output_path}')
