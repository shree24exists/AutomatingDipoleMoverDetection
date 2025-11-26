import os
from PIL import Image

BOOKS_DIR = "books"
GIFS_DIR = "gifs"

os.makedirs(GIFS_DIR, exist_ok=True)

def process_one_book(book_path, book_name):
    # Accept ANY of these patterns:
    frames = sorted([
        f for f in os.listdir(book_path)
        if f.lower().endswith((".jpg", ".jpeg"))
        or f.lower().startswith("frame")
    ])

    if len(frames) != 4:
        print(f"❌ ERROR: {book_path} has {len(frames)} files (needs 4). Skipping.")
        return

    images = []
    for frame in frames:
        img_path = os.path.join(book_path, frame)
        images.append(Image.open(img_path))

    output_path = os.path.join(GIFS_DIR, f"{book_name}.gif")

    images[0].save(
        output_path,
        save_all=True,
        append_images=images[1:],
        duration=300,
        loop=0
    )

    print(f"✅ GIF created: {output_path}")

def process_all_books():
    for book_name in sorted(os.listdir(BOOKS_DIR)):
        book_path = os.path.join(BOOKS_DIR, book_name)

        if os.path.isdir(book_path):
            process_one_book(book_path, book_name)

if __name__ == "__main__":
    process_all_books()
