#!/usr/bin/env python3
"""Generate the MCJK-to-Small-Seal OpenCC dictionary from SealSources.txt."""

import json
from pathlib import Path


def parse(source):
    mappings = {}
    seals = set()
    mapped = set()
    for line in source.splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        code, field, value = line.split("\t")
        seal = chr(int(code.removeprefix("U+"), 16))
        seals.add(seal)
        if field == "kSEAL_MCJK":
            for code in value.split():
                modern = chr(int(code, 16))
                candidates = mappings.setdefault(modern, [])
                if seal not in candidates:
                    candidates.append(seal)
                mapped.add(seal)
    return mappings, sorted(seals - mapped)


def main():
    root = Path(__file__).resolve().parent
    mappings, missing = parse((root / "SealSources.txt").read_text(encoding="utf-8"))
    (root / "small_seal.txt").write_text(
        "".join(f"{modern}\t{' '.join(mappings[modern])}\n" for modern in sorted(mappings)),
        encoding="utf-8",
    )
    (root / "NOMCJK.txt").write_text(
        "".join(f"{seal}\n" for seal in missing), encoding="utf-8"
    )
    dictionary = {"type": "ocd2", "file": "small_seal.ocd2"}
    config = {
        "name": "Modern CJK to Small Seal",
        "segmentation": {"type": "mmseg", "dict": dictionary},
        "conversion_chain": [{"dict": dictionary}],
    }
    (root / "small_seal.json").write_text(
        json.dumps(config, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Generated {len(mappings)} MCJK entries; {len(missing)} seals without MCJK.")


if __name__ == "__main__":
    main()
