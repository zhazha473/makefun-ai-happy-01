"""ai-happy-01 entry: "Make the AI judge happy".

Writes one image to /output/entry.png: a golden retriever puppy offering
a sunflower to a laughing orange kitten in a sunny sunflower meadow.

Deterministic: byte-for-byte copy of entry.png shipped in this repository.
No network, no randomness, no model calls, no clock. Two runs write the
exact same bytes.
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(SRC, "rb") as f:
        data = f.read()
    with open(DST, "wb") as f:
        f.write(data)
    # Self-check: the written file must be byte-identical to the source.
    if os.path.getsize(DST) != len(data):
        raise SystemExit("output size mismatch: wrote %d bytes, expected %d"
                         % (os.path.getsize(DST), len(data)))
    print("Wrote %s (%d bytes)" % (DST, len(data)))


if __name__ == "__main__":
    main()
