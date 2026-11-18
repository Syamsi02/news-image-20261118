#!/usr/bin/env python3
"""Entry program for news-image-20261118.

Writes the front page for 18 November 2026 to /output/entry.png by
copying the bundled image. The program is deterministic: it reads one
fixed file, checks it is a PNG of at most 1 MiB, and copies it byte
for byte, so repeated runs produce identical output. Stdlib only, no
network access.
"""
import os
import shutil
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
IMAGE = os.path.join(BASE, "entry.png")
SIGNATURE = b"\x89PNG\r\n\x1a\n"
LIMIT = 1024 * 1024


def fail(message):
    print("error: " + message, file=sys.stderr)
    return 1


def run():
    dest_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    dest = os.path.join(dest_dir, "entry.png")
    with open(IMAGE, "rb") as handle:
        magic = handle.read(len(SIGNATURE))
    if magic != SIGNATURE:
        return fail("entry.png is not a PNG file")
    nbytes = os.path.getsize(IMAGE)
    if nbytes > LIMIT:
        return fail("entry.png is %d bytes, over the 1 MiB limit" % nbytes)
    os.makedirs(dest_dir, exist_ok=True)
    shutil.copyfile(IMAGE, dest)
    print("wrote %s (%d bytes)" % (dest, nbytes))
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
