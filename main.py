#!/usr/bin/env python3
"""news-image-20261119 -- write the entry image to /output/entry.png.

Entry for the make.fun bounty "Sum up 19 November's world news in one
image" (https://make.fun/bounty/news-image-20261119).

The image is a newspaper front page summing up Thursday 19 November 2026:
the Trump-Xi-Putin trilateral meeting at the APEC summit in Shenzhen leads,
with the fresh attack on the Crimea Bridge, Israel's rare ground operation
in Gaza, Anthropic's record $81.3 billion IPO, and the worldwide rollout
of Grand Theft Auto VI below, plus Voyager 1, the record Van Gogh sale,
Cyclone Akvan and the Myanmar verdict in the ticker.

Fully offline and deterministic: this program copies the bundled image
`news.png` to `/output/entry.png`. Running it twice writes identical bytes.
No network, no randomness, no environment dependence.

Before copying, the program validates the source image: it must exist next
to this file and must be at most 1 MiB (the make.fun entry size limit).
A missing or oversized source aborts with a clear error instead of
producing a partial or invalid entry.
"""

import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "news.png")
DST = "/output/entry.png"
MAX_BYTES = 1 * 1024 * 1024  # make.fun entry size limit: 1 MiB


def validate_source(path: str) -> int:
    """Check the bundled image exists and fits the 1 MiB limit.

    Returns the file size in bytes. Raises SystemExit with a clear
    message when the source is missing or oversized, so a broken
    bundle fails loudly instead of writing a bad entry.
    """
    if not os.path.isfile(path):
        raise SystemExit(
            f"error: source image not found: {path}\n"
            "expected news.png next to main.py; refusing to write an entry."
        )
    size = os.path.getsize(path)
    if size > MAX_BYTES:
        raise SystemExit(
            f"error: source image too large: {size} bytes "
            f"(limit {MAX_BYTES} bytes / 1 MiB): {path}"
        )
    return size


def main() -> None:
    validate_source(SRC)
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    with open(DST, "rb") as f:
        digest = hashlib.sha256(f.read()).hexdigest()
    size = os.path.getsize(DST)
    print(f"wrote {DST} ({size} bytes, sha256 {digest})")


if __name__ == "__main__":
    main()
