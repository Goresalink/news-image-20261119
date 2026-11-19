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
"""

import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "news.png")
DST = "/output/entry.png"


def main() -> None:
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    with open(DST, "rb") as f:
        digest = hashlib.sha256(f.read()).hexdigest()
    size = os.path.getsize(DST)
    print(f"wrote {DST} ({size} bytes, sha256 {digest})")


if __name__ == "__main__":
    main()
