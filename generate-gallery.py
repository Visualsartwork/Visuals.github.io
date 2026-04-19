import os
import json

PICTURES_DIR = 'Pictures'
IMAGE_EXTS = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.jfif', '.bmp'}

def scan_gallery(root):
    categories = []

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames.sort()
        images = sorted([
            f for f in filenames
            if os.path.splitext(f.lower())[1] in IMAGE_EXTS
        ])

        if not images:
            continue

        rel_dir = dirpath.replace('\\', '/')
        image_paths = [f"{rel_dir}/{img}" for img in images]

        if rel_dir == root:
            name = 'Misc'
            cat_id = 'misc'
        else:
            name = os.path.basename(dirpath)
            cat_id = name.lower().replace(' ', '-').replace('_', '-')

        categories.append({
            'id': cat_id,
            'name': name,
            'breadcrumb': rel_dir + '/',
            'images': image_paths
        })

    return categories

if __name__ == '__main__':
    gallery = scan_gallery(PICTURES_DIR)
    with open('gallery-data.json', 'w') as f:
        json.dump(gallery, f, indent=2)
    print(f"Generated gallery-data.json with {len(gallery)} categories:")
    for cat in gallery:
        print(f"  {cat['name']}: {len(cat['images'])} images")
