"""Integration tests. Uses the `moss_decoder` package from python and allows benchmarks."""
from pathlib import Path
import moss_decoder

FILE_PATH = Path("tests/moss_noise.raw")


def read_bytes_from_file(file_path: Path) -> bytes:
    """Open file at `file_path` and read as binary, return `bytes`"""
    with open(file_path, "rb") as readout_file:
        raw_bytes = readout_file.read()

    return raw_bytes


def decode_multi_event(raw_bytes: bytes) -> tuple[list["MossPacket"], int]:
    """Takes `bytes` and decodes it as `MossPacket`s.
    returns a tuple of `list[MossPackets]` and an int that indicates the
    index where the last MOSS trailer was seen
    """
    packets, last_trailer_idx = moss_decoder.decode_multiple_events_alt(b)

    return packets, last_trailer_idx


if __name__ == "__main__":
    b = read_bytes_from_file(FILE_PATH)
    byte_count = len(b)
    last_byte_idx = byte_count - 1

    print(f"Read {byte_count} bytes")

    packets, last_trailer_idx = decode_multi_event(raw_bytes=b)

    print(f"Decoded {len(packets)} packets")

    print(f"Last trailer at index: {last_trailer_idx}/{last_byte_idx}")
    remainder_count = last_byte_idx - last_trailer_idx
    print(f"Remainder: {last_byte_idx-last_trailer_idx} byte(s)")

    if byte_count > last_trailer_idx:
        print(f"Remainder byte(s): {b[last_trailer_idx+1:]}")
