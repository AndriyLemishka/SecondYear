# -*- coding: utf-8 -*-
import subprocess, os, time
from PIL import Image

html_path = os.path.abspath(r"lab4\08_scratch\html_boards\fig21_inputs_controls.html")
out_png = os.path.abspath(r"lab4\screenshots\fig21_inputs_controls.png")
chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

url = "file:///" + html_path.replace("\\", "/")

cmd = [
    chrome,
    "--headless=new",
    "--window-size=1250,560",
    "--hide-scrollbars",
    "--force-device-scale-factor=1.5",
    f"--screenshot={out_png}",
    url
]
subprocess.run(cmd, check=True)

im = Image.open(out_png)
print("Updated fig21:", im.size, time.ctime(os.path.getmtime(out_png)))
