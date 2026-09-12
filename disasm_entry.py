#!/usr/bin/env python3
"""
A real, working example combining two of the tools this toolkit installed
(pyelftools + capstone) — not just "imports fine," an actual small binary
analysis task: find a binary's entry point and disassemble the first
instructions there.

Usage: python3 disasm_entry.py /path/to/binary
"""
import sys

from capstone import CS_ARCH_X86, CS_MODE_64, Cs
from elftools.elf.elffile import ELFFile


def disasm_entry(path, num_bytes=40):
    with open(path, "rb") as f:
        elf = ELFFile(f)
        entry = elf.header["e_entry"]

        section = None
        for candidate in elf.iter_sections():
            in_range = candidate["sh_addr"] <= entry < candidate["sh_addr"] + candidate["sh_size"]
            if in_range and candidate["sh_type"] == "SHT_PROGBITS":
                section = candidate
                break
        if section is None:
            raise RuntimeError(f"Couldn't find a section containing entry point {hex(entry)}")

        f.seek(section["sh_offset"] + (entry - section["sh_addr"]))
        code = f.read(num_bytes)

    print(f"{path}")
    print(f"entry point: {hex(entry)} (in section {section.name})\n")

    md = Cs(CS_ARCH_X86, CS_MODE_64)
    for insn in md.disasm(code, entry):
        print(f"  0x{insn.address:x}: {insn.mnemonic} {insn.op_str}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} /path/to/binary")
        sys.exit(1)
    disasm_entry(sys.argv[1])
