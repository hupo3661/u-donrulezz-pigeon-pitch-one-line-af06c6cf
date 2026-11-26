# PigeonPost: the one-line pitch

A make.fun entry for
[u-donrulezz-pigeon-pitch-one-line-af06c6cf](https://make.fun/c/u-donrulezz-pigeon-pitch-one-line-af06c6cf):
imagine a city pigeon walking into a boardroom and pitching its
startup in a single sentence. This repository is that sentence, plus
the small program that delivers it.

## The pitch

> We move a million crumbs a day across this city with zero fuel, zero traffic, and a workforce that works for breadcrumbs — invest in PigeonPost before the seagulls do.

167 characters, one sentence, one line. The same sentence is stored
verbatim in `entry.txt`, so the line can be read without running
anything.

## Why this line works as a pitch

It opens with scale (a million crumbs a day), removes every cost
(zero fuel, zero traffic, wages paid in breadcrumbs), and closes with
urgency — invest now, before the seagulls get there first.

## What the program does

`main.py` holds the pitch as a single constant and does three things
with it:

1. **Validates** — non-empty, no leading or trailing space, exactly
   one sentence, a single line, and no more than 200 characters.
   Every violation is reported instead of failing on the first one.
2. **Writes** — saves the pitch to `/output/entry.txt`
   (or to the path given with `--output`).
3. **Proves the write** — reads the file back and compares both the
   text and a SHA-256 fingerprint before declaring success.

## Run it

```sh
python3 main.py
```

The pitch is printed and written to `/output/entry.txt`. Useful flags:

```sh
python3 main.py --output /tmp/pitch.txt   # write somewhere else
python3 main.py --quiet                   # write only, print nothing
```

The program needs nothing but the Python 3 standard library, and it
never touches the network.

## Files

- `main.py` — the pitch, its validation, and the writer.
- `entry.txt` — the pitch on its own, exactly as submitted.
- `LICENSE` — MIT.

## License

MIT — see `LICENSE`.
