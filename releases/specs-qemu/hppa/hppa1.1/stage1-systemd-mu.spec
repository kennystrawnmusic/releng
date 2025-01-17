subarch: hppa1.1
target: stage1
version_stamp: systemd-mergedusr-@TIMESTAMP@
rel_type: mergedusr
profile: default/linux/hppa/17.0/systemd/merged-usr
snapshot: @TIMESTAMP@
source_subpath: mergedusr/stage3-hppa1.1-systemd-mergedusr-latest
update_seed: yes
interpreter: /usr/bin/qemu-hppa
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
compression_mode: pixz
decompressor_search_order: xz bzip2
update_seed_command: --update --deep --newuse @world
