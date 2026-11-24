"""Worst app idea pitch: QueuePal, a virtual queue for a shop that closed.

Writes exactly one sentence (145 chars, no trailing newline) to
/output/entry.txt, byte-identical on every run.
"""

from pathlib import Path

PITCH = (
    "QueuePal lets you join a virtual queue for a shop that closed in 2019, "
    "so you can wait in line with 40,000 strangers who also have nowhere to be."
)

DESTINATION = Path("/output/entry.txt")


def emit() -> str:
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    with open(DESTINATION, "w", encoding="utf-8") as handle:
        handle.write(PITCH)
    DESTINATION.chmod(0o644)
    written_back = DESTINATION.read_text(encoding="utf-8")
    if written_back != PITCH:
        raise SystemExit("entry.txt does not match the pitch")
    return PITCH


if __name__ == "__main__":
    emit()
