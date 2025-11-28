import os
from PIL import Image

input_folder = '.'
output_folder = './output_images'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

files = os.listdir(input_folder)

image_extensions = ['.jpg', '.jpeg', '.png', '.bmp']
image_files = [f for f in files if os.path.splitext(f)[1].lower() in image_extensions]

max_resolution = 768

for index, image_file in enumerate(image_files):
    image_path = os.path.join(input_folder, image_file)
    image = Image.open(image_path)
    width, height = image.size
    if width > max_resolution or height > max_resolution:
        ratio = min(max_resolution / width, max_resolution / height)
        new_width = int(width * ratio)
        new_height = int(height * ratio)
        image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    output_filename = f'{index + 1}.png'
    output_path = os.path.join(output_folder, output_filename)
    image.save(output_path, 'PNG')
    print(f'Converted {image_file} to {output_filename} (Resolution: {image.size[0]}x{image.size[1]})')

print('All done')