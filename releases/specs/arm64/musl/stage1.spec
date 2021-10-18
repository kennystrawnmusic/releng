subarch: arm64
target: stage1
version_stamp: musl-@TIMESTAMP@
rel_type: musl
profile: default/linux/arm64/17.0/musl
snapshot: @TIMESTAMP@
source_subpath: musl/stage3-arm64-musl-latest
compression_mode: pixz_x
update_seed: yes
update_seed_command: --update --deep --jobs=5 --newuse --complete-graph @world
portage_confdir: @REPO_DIR@/releases/portage/stages-musl
repos: /root/musl
portage_prefix: releng
chost: aarch64-gentoo-linux-musl