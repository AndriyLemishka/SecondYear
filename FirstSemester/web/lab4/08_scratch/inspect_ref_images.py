import pypdf

r = pypdf.PdfReader(r'C:\Users\andri_gxiil3v\.gemini\antigravity\brain\8b923188-aa44-470c-a9a2-49b2c3b66742\.user_uploaded\media_1791471127621_e26a7f88.pdf')
print("Reference PDF Images:")
for idx, page in enumerate(r.pages):
    imgs = page.images
    if imgs:
        img_info = [f"{name} {img.image.size}" for name, img in imgs.items()]
        print(f"Page {idx+1}: {', '.join(img_info)}")
    else:
        print(f"Page {idx+1}: (no images)")
