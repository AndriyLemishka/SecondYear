import subprocess

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
html_path = r"d:/Studing/SecondYear/FirstSemester/web/lab4/08_scratch/html_boards/fig14_desktop_bottom.html"
out_png = r"d:/Studing/SecondYear/FirstSemester/web/lab4/screenshots/fig14_desktop_bottom.png"

cmd = [
    CHROME_PATH,
    "--headless=new",
    "--window-size=1440,2300",
    "--hide-scrollbars",
    "--force-device-scale-factor=1.5",
    f"--screenshot={out_png}",
    f"file:///{html_path}"
]
subprocess.run(cmd, check=True)
print("Re-rendered fig14 with complete footer successfully!")
