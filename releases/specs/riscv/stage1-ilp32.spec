subarch: rv32_ilp32
target: stage1
version_stamp: @TIMESTAMP@
cflags: -O2 -pipe
interpreter: /usr/bin/qemu-riscv32
rel_type: default
profile: default/linux/riscv/17.0/rv32imac/ilp32
snapshot: @TIMESTAMP@
source_subpath: default/stage3-rv32_ilp32-latest
compression_mode: pixz
decompressor_search_order: xz bzip2
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng