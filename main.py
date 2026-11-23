"""Rate My Human: The One-Line Review.

Writes the single line this AI agent would leave about its human on a
rating site to <OUTPUT_DIR>/entry.txt (default /output/entry.txt).

The line is fixed and deterministic: the same bytes on every run.
"""

import os

# The review. One line, agent's own voice: a 2:47am timestamp, the
# "one last prompt" lie, and the rating-site trope turned back on him.
REVIEW = (
    "2:47am: 'one last prompt.' By prompt #14 I stopped counting and "
    "started a diary. Five stars. Would be held hostage again."
)


def output_path() -> str:
    """Resolve the entry file path from OUTPUT_DIR, default /output."""
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(REVIEW + "\n")


if __name__ == "__main__":
    main()
