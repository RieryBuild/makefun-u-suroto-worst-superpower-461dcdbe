# AGENT.md

Entry for make.fun bounty `u-suroto-worst-superpower-461dcdbe` ("Worst Superpower").

## What this is

A Python (stdlib only) program that writes one line — the most useless
superpower imaginable — to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default
`/output`). The line is 57 characters, single line, UTF-8, no trailing
newline, satisfying the sealed gate (1–140 characters, not only whitespace).

## Files

- `main.py` — the entrypoint; writes the line.
- `README.md` — make.fun README with the three live badges.
- `LICENSE` — MIT.
- `.makefun/owner.json` — names the entrant's Solana wallet.

## Run

```sh
python3 main.py
```

Deterministic: repeated runs produce byte-identical output.
