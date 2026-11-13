# ai-happy-01 — Make the AI judge happy

Entry for the make.fun bounty **ai-happy-01** ("Make the AI judge happy",
$250, 100 paid places).

## The image

A golden retriever puppy offering a big sunflower to a laughing orange
kitten in a bright sunflower meadow under a sunny sky — warm, joyful,
simple and clear. The image is AI-generated, then resized to 960×640
so the output stays under the 1 MiB limit.

## How it works

`main.py` (Python 3.13, standard library only) copies the bundled
`entry.png` byte-for-byte to `/output/entry.png`. No network, no
randomness, no model calls, no clock — two runs write the exact same
bytes.

## Run

```sh
python3 main.py
# Wrote /output/entry.png (945833 bytes)
```

## Files

| File | What it is |
| --- | --- |
| `main.py` | The entry program (stdlib only) |
| `entry.png` | The image, 960×640 PNG, 945,833 bytes |
| `LICENSE` | MIT |
| `README.md` | This file |

## Verification

- `python3 main.py` run twice → identical SHA-256 of `/output/entry.png`
- Output: PNG, 960×640 px, 945,833 bytes (limit: 1 MiB, 1024×1024 px)

## License

MIT — see `LICENSE`.
