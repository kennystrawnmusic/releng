subarch: ppc64
target: stage1
version_stamp: @TIMESTAMP@
rel_type: default
profile: default/linux/powerpc/ppc64/17.0/64bit-userland
snapshot: @TIMESTAMP@
source_subpath: default/stage3-ppc64-latest
compression_mode: pixz_x
update_seed: yes
update_seed_command: --update --deep --newuse @world --jobs 5 --load-average 5
portage_confdir: @REPO_DIR@/releases/portage/stages
