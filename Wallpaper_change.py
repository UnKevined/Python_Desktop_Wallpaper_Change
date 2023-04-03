import ctypes

# Loading wallpaper from network for windows operation system
def change_wallpaper(image_path):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETDESKWALLPAPER, 0, image_path, 3)
    
# Path to image png and jpg are possible
if __name__ == '__main__':
    image_path = '\\\\path.png'
    change_wallpaper(image_path)
