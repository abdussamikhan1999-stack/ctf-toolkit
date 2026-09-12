# CTF / Security Practice Toolkit

Your own machine, your own practice — a setup for learning offensive
security concretely, via CTF wargames/challenges (per the recommendation
in [cyberpunk-privacy-notes](https://github.com/abdussamikhan1999-stack/cyberpunk-privacy-notes):
*"pick one CTF platform and just start"*).

## Already installed and verified on this machine (no `sudo` needed)

These were installed user-locally (`pip install --user`, no root) and
each one was actually tested, not just installed and assumed working:

- **GEF** (GDB Enhanced Features) — a GDB plugin for exploit development:
  disassembly context, register/stack views, a built-in `checksec`
  command (binary security properties: PIE, canary, NX, RELRO), heap
  inspection, and 415 commands total. Verified with a real `gdb -batch`
  invocation — loaded cleanly, correct version reported. Lives at
  `~/.gdbinit-gef.py`, auto-loads via `~/.gdbinit`.
- **ropgadget** — searches a binary for ROP gadgets (chains of
  instructions ending in `ret`, used to build exploits against
  non-executable-stack protections). `python3 -m ROPgadget --help`
- **capstone** — the disassembly engine GEF and many other tools build on.
- **pyelftools** (import name `elftools`) — parses ELF binaries
  programmatically; useful for writing your own analysis scripts.
- **requests** — for scripting against web-based CTF challenges/APIs.

**Not installed**: `pwntools` (the standard CTF exploit-dev framework) —
its `unicorn` dependency needs to compile a C extension, which needs
`cmake` (not present, needs `sudo`). Once you've run the `sudo dnf`
command below, retry with:
```
python3 -m pip install --user pwntools
```

## Needs your `sudo` password — run this yourself

I can't do this part — no passwordless `sudo` on this machine, and my
tools have no way to type a password interactively. This one command
covers everything else worth having:

```bash
sudo dnf install -y nmap wireshark hashcat john hydra aircrack-ng \
  radare2 binwalk strace ltrace socat cmake gcc gcc-c++
```

What each one is for:

| Tool | What it's for |
|---|---|
| `nmap` | Network/port scanning — the standard recon tool |
| `wireshark` / `tshark` | Packet capture and analysis (GUI / CLI) |
| `hashcat` | GPU-accelerated password/hash cracking |
| `john` (John the Ripper) | CPU-based password cracking, good for CTF-style hash challenges |
| `hydra` | Online login brute-forcing (only against targets you're authorized to test) |
| `aircrack-ng` | Wi-Fi security auditing (again, your own network/authorized targets only) |
| `radare2` | Reverse-engineering/disassembly framework (binwalk's heavier cousin) |
| `binwalk` | Extracts embedded files/firmware from binary blobs — common in CTF forensics challenges |
| `strace` / `ltrace` | Trace a running program's syscalls / library calls |
| `socat` | Swiss-army-knife for redirecting/relaying network connections — used constantly in CTF pwn challenges to connect to a remote service |
| `cmake`, `gcc`, `gcc-c++` | Build dependencies — unlocks `pwntools` (see above) and compiling your own exploit code |

## Where to actually practice

Per the notes: **start with [OverTheWire](https://overthewire.org/wargames/)**,
specifically the **Bandit** wargame — a sequence of ~30 levels teaching
basic Linux/security fundamentals via SSH, free, no signup. It's the
standard first stop; don't overthink where to begin.

Follow-ups once Bandit feels easy: **PentesterLab**, **VulnHub**,
**Root-Me** (all linked in cyberpunk-privacy-notes' Security section).

## A note on scope

Every tool here is dual-use — the same tools defenders and red-teamers
both use. Use them against CTF platforms (which exist specifically to be
tested against) and your own systems/networks. `hydra` and `aircrack-ng`
in particular are only legal/appropriate against systems and networks you
own or have explicit authorization to test.
