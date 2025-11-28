import os

waifu_exec = 'F:/waifu2x-ncnn-vulkan/waifu2x-ncnn-vulkan_waifu2xEX.exe'

def waifu_scale(input, output='', fmt='jpg', scale=2):
    if fmt[0] == '.':
        fmt = fmt[1:]
    cmd = """%s -i "%s" -s %d -f %s -o "%s" -v""" % (
        waifu_exec, input, scale, fmt, output)
    print(cmd)
    os.system(cmd)


def waifu_batch_current_dir(input_folder='./', output_folder='./output', scale=2, new_file_tail='_wf2'):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    files = os.listdir(input_folder)
    for filename in files:
        os.path.splitext(filename)[1].lower()
        image_ext = ['.jpg', '.jpeg', '.png']
        _, file_base_name, file_ext = split_path_file_ext(filename)
        if file_ext.lower() not in image_ext:
            continue
        new_filename = os.path.join(
            output_folder, file_base_name + new_file_tail + file_ext)
        new_filename = win_path_to_linux_path(new_filename)
        waifu_scale(filename, new_filename, file_ext, scale)


def win_path_to_linux_path(win_path):
    return win_path.replace('\\', '/')


def split_path_file_ext(path):
    path, filename = os.path.split(path)
    name, ext = os.path.splitext(filename)
    return path, name, ext


def path_with_tail(path, tail):
    p, name, ext = split_path_file_ext(path)
    if p == '':
        os_sep = ''
    else:
        os_sep = os.path.sep
    return p + os_sep + name + tail + ext


if __name__ == '__main__':
    input_dir = './'
    output_dir = './output'
    scale = 2
    waifu_batch_current_dir(input_dir, output_dir, scale)
