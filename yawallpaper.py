#!/usr/local/bin/python3
import urllib.request, datetime, time, os, shutil, os, platform, subprocess, tkinter as tk

IMAGENAME = 'Yandex-Images-' + datetime.date.today().strftime('%Y-%m-%d') + '.jpg'
YANDEX_URL = 'http://yandex.ru/images/today?size='

MAC_SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""

def convert_to_bmp(path_to_image):
    from PIL import Image
    bmp_image = Image.open(path_to_image)
    filename = os.path.basename(path_to_image)
    filename = os.path.splitext(filename)[0] + ".BMP"
    bmp_image.save(filename, "BMP")
    return os.path.join(os.getcwd(), filename).encode('utf-8')

def set_image_as_wallpaper(path_to_image):
    system = platform.system()
    if system == 'Darwin':
        subprocess.Popen(MAC_SCRIPT % path_to_image, shell=True)
       # time.sleep(10)  # launchd requires that the job runs for at least 10s

    elif system == 'Windows':
        from ctypes import windll
        bmp = convert_to_bmp(path_to_image)
        windll.user32.SystemParametersInfoA(20, 0, bmp, 0)
        os.remove(path_to_image)
        os.remove(bmp)

def convert_to_hfs(path):
    hfs_path = subprocess.check_output(
        ['/usr/bin/osascript', '-e', 'return posix file "%s"' % path])
    return hfs_path.replace(b'file',b'').strip()

def get_screen_resolution():
    root = tk.Tk()
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    return str(w) + "x" + str(h)

if __name__ == "__main__":
    print('Downloading image...')
    urllib.request.urlretrieve(YANDEX_URL + get_screen_resolution(),IMAGENAME)
    print('Setting image as wallpaper...')
    set_image_as_wallpaper(os.path.realpath(IMAGENAME))
    print('Okay. Bye!')
