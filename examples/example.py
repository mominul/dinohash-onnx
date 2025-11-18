"""Example usage of the DINOHash ONNX library."""

import os
import sys
from PIL import Image
from dinohash_onnx import DINOHash


def main():
    if len(sys.argv) < 2:
        print("Usage: python example.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]

    hash = DINOHash()
    hash_hex = hash.hash(image_path)
    print(f"Image: {image_path}")
    print(f"  Hex: {hash_hex}")


if __name__ == '__main__':
    main()
