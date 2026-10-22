import re

with open('lab5/lab-05-semantic-layout/assets/images/Logo.svg', 'r') as f:
    text = f.read()

m = re.search(r'<path d="(M377\.2[^"]+)"', text)
if m:
    d = m.group(1)
    nums = [float(x) for x in re.findall(r'[-+]?\d*\.?\d+', d)]
    xs = nums[0::2]
    ys = nums[1::2]
    print(f"X: {min(xs)} to {max(xs)}, width={max(xs)-min(xs)}")
    print(f"Y: {min(ys)} to {max(ys)}, height={max(ys)-min(ys)}")
