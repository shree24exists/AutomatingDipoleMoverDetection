import os
import shutil

RAW = r"D:\Shreerang_Drive\College\SELF PROJECTS\Automated Zooniverse\Dataset\Images"
OUT = r"D:\Shreerang_Drive\College\SELF PROJECTS\Automated Zooniverse\Dataset\books"

os.makedirs(OUT, exist_ok=True)

files = sorted(
    [f for f in os.listdir(RAW) if f.lower().endswith(".jpeg")],
    key=lambda x: int(x.split('.')[0])
)

book_num = 1
for i in range(0, len(files), 4):
    group = files[i:i+4]
    if len(group) < 4:
        break

    folder_name = f"book_{book_num:03d}"
    folder_path = os.path.join(OUT, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    for idx, filename in enumerate(group):
        src = os.path.join(RAW, filename)
        dst = os.path.join(folder_path, f"frame{idx}.jpg")
        shutil.copy(src, dst)

    print(f"Created {folder_name}")
    book_num += 1
