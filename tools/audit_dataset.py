"""Find exact image overlap without loading model weights or requiring ML libraries."""
import argparse
import hashlib
import json
from pathlib import Path

def audit(root):
    root = Path(root)
    groups = {}
    for split in ('train', 'val'):
        folder = root / split / 'images'
        if not folder.is_dir():
            raise ValueError(f'Missing image directory: {folder}')
        groups[split] = {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in sorted(folder.rglob('*')) if p.suffix.lower() in {'.jpg','.jpeg','.png','.webp'}}
    known = set(groups['train'].values())
    return {'counts': {s: len(v) for s,v in groups.items()},
            'overlapping_validation_images': [p for p,h in groups['val'].items() if h in known]}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('dataset')
    result = audit(parser.parse_args().dataset)
    print(json.dumps(result, indent=2))
    raise SystemExit(1 if result['overlapping_validation_images'] else 0)
