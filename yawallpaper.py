import urllib.request, datetime, time, os, shutil, os, platform, subprocess

IMAGENAME = 'Yandex-Images-' + datetime.date.today().strftime('%Y-%m-%d') + '.jpg'
YANDEX_URL = 'http://yandex.ru/images/today?size=1920x1200'
MAC_SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to {"%s"} as alias
end tell
END"""

def convert_to_bmp(path_to_image):
    from PIL import Image
    bmp_image = Image.open(path_to_image)
    filename = os.path.basename(path_to_image)
    filename = os.path.splitext(filename)[0] + ".BMP"
    bmp_image.save(filename, "BMP")
    return os.path.join(os.getcwd(), filename).encode('utf-8')

def setImageAsWallpaper(path_to_image):
    system = platform.system()
    if system == 'Darwin':
        subprocess.Popen(MAC_SCRIPT %
                         convert_to_hfs(path_to_image), shell=True)
        time.sleep(10)  # launchd requires that the job runs for at least 10s

    elif system == 'Windows':
        from ctypes import windll
        bmp = convert_to_bmp(path_to_image)
        windll.user32.SystemParametersInfoA(20, 0, bmp, 0)
        os.remove(path_to_image)
        os.remove(bmp)



if __name__ == "__main__":
    urllib.request.urlretrieve(YANDEX_URL,IMAGENAME)
    print(os.path.realpath(IMAGENAME))
    setImageAsWallpaper(os.path.realpath(IMAGENAME))
