#!/usr/bin/env python3
"""news-image-20261119: one image summing up the world news of
Thursday 19 November 2026.

The image is the entry.png beside this file, drawn by the first build
(a 1024x1024 newspaper front page). This program just copies it to
/output/entry.png (or $MAKEFUN_OUTPUT_DIR), standard library only:
nothing is installed before it runs, so no third-party imports.
Deterministic: a plain byte copy, no timestamps, no randomness,
no network. Running it twice writes byte-identical output.

Stories the image shows (all events of, or first reported on,
19 November 2026):
  1. Trump, Xi & Putin hold the first trilateral summit at APEC, Shenzhen.
  2. Anthropic debuts on Nasdaq in a record $81B IPO (ticker ANT).
  3. The Crimean Bridge is attacked again; traffic halted.
  4. Grand Theft Auto VI launches worldwide (rolling midnight release).
  5. NASA confirms Voyager 1 is one light-day from Earth.
  6. Australia, Canada, Italy & the UK urge aid access to flooded Gaza.
"""

import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main():
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    out = os.path.join(outdir, "entry.png")
    shutil.copyfile(SRC, out)
    return out


if __name__ == "__main__":
    print(main())
