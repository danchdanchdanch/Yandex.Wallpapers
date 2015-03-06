import win32api, win32con, win32gui, urllib.request, datetime, time, os, shutil

#----------------------------------------------------------------------
def getImageName():
    return 'Yandex-Images-' + datetime.date.today().strftime('%Y-%m-%d') + '.jpg'

def setImageAsWallpaper(filename):
    key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "0")
    win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, "C:/Yandex-Images/" + filename, 1+2)

def getImageAndSaveAs(filename):
    urllib.request.urlretrieve('http://yandex.ru/images/today?size=1920x1200',filename)

def moveImage(filename):
    shutil.move(filename, "C:/Yandex-Images/" + filename)

def getImagePath():
    return os.getcwd()

if __name__ == "__main__":
    getImageAndSaveAs(getImageName())
    moveImage(getImageName())
    setImageAsWallpaper(getImageName())