# python-pahole-utility
A tool for dumping linux debug kernel structures using pahole

Pahole
======
Reference:
https://groups.google.com/forum/#!searchin/vmitools/pahole/vmitools/vZh5spoVN9g/byVCCvuLBwAJ

Do “Where to get Debug Symbols for X” at this address: https://wiki.ubuntu.com/Kernel/Systemtap
Install pahole sudo apt-get install dwarves
cd /usr/lib/debug/boot
Run pahole -C <name of offset> <name of kernel>
example: pahole -C task-struct vmlinux-3.13.0-79-generic
