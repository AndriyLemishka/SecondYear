import math
import random
from PIL import Image, ImageDraw

def create_windows_cursor():
    # 32x32 transparent RGBA image
    img = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Standard Windows arrow cursor polygon
    # Hotspot is at (0, 0)
    polygon = [
        (0, 0),
        (0, 17),
        (4, 13),
        (7, 20),
        (10, 19),
        (7, 12),
        (12, 12)
    ]
    
    # Shadow offset (1, 1)
    shadow_polygon = [(x + 1, y + 1) for x, y in polygon]
    draw.polygon(shadow_polygon, fill=(0, 0, 0, 70), outline=(0, 0, 0, 100))
    
    # White body with dark outline
    draw.polygon(polygon, fill=(255, 255, 255, 255), outline=(20, 20, 20, 255))
    
    img.save("windows_cursor.png")
    print("Created windows_cursor.png")

if __name__ == '__main__':
    create_windows_cursor()
