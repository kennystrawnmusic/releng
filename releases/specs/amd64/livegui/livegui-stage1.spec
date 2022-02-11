subarch: amd64
version_stamp: plasma-@TIMESTAMP@
target: livecd-stage1
rel_type: default
profile: default/linux/amd64/17.1/desktop/plasma
snapshot: @TIMESTAMP@
source_subpath: default/stage3-amd64-openrc-@TIMESTAMP@.tar.xz
compression_mode: pixz
portage_confdir: @REPO_DIR@/releases/portage/livegui

livecd/use:
	-aac
	compile-locales
	fbcon
	jpeg2k
	livecd
	modules
	networkmanager
	openexr
	opus
	postproc
	portaudio
	python
	theora
	vpx
	xetex

livecd/packages:
	app-accessibility/brltty
	app-accessibility/espeakup
	app-admin/hddtemp
	app-admin/sudo
	app-admin/syslog-ng
	app-admin/testdisk
	app-arch/deb2targz
	app-arch/p7zip
	app-arch/rpm
	app-arch/zip
	app-backup/fsarchiver
	app-cdr/dvd+rw-tools
	app-cdr/cdrtools
	app-crypt/chntpw
	app-crypt/gnupg
	app-editors/ghex
	app-editors/hexedit
	app-editors/joe
	app-editors/kile
	app-editors/mg
	app-editors/nano
	app-eselect/eselect-repository
	app-misc/livecd-tools
	app-misc/mc
	app-misc/screen
	app-misc/tmux
	app-misc/wipe
	app-office/libreoffice
	app-office/texstudio
	app-officeext/texmaths
	app-portage/genlop
	app-portage/gentoolkit
	app-portage/mirrorselect
	app-portage/pram
	app-portage/repoman
	app-portage/ufed
	app-text/bibutils
	app-text/ghostscript-gpl
	app-text/pdftk
	app-text/recode
	app-text/texlive
	app-text/wgetpaste
	app-text/xournalpp
	dev-vcs/git
	dev-vcs/kdesvn
	dev-vcs/subversion
	kde-apps/k3b
	kde-apps/kde-apps-meta
	kde-apps/kdenlive
	kde-apps/kdepim-meta
	kde-apps/kipi-plugins
	kde-apps/kompare
	kde-misc/kdiff3
	kde-plasma/plasma-meta
	media-gfx/digikam
	media-gfx/engauge
	media-gfx/gimp
	media-gfx/gnuclad
	media-gfx/graphviz
	media-gfx/hugin
	media-gfx/inkscape
	media-gfx/jhead
	media-gfx/pngcrush
	media-gfx/pngquant
	media-gfx/povray
	media-sound/alsa-utils
	media-video/kaffeine
	media-video/mplayer
	net-analyzer/nmap
	net-analyzer/tcpdump
	net-analyzer/traceroute
	net-dialup/minicom
	net-dialup/mingetty
	net-dialup/pptpclient
	net-dialup/rp-pppoe
	net-fs/cifs-utils
	net-fs/nfs-utils
	net-irc/irssi
	net-misc/chrony
	net-misc/dhcpcd
	net-misc/iputils
	net-misc/ntp
	net-misc/openssh
	net-misc/rdesktop
	net-misc/rsync
	net-misc/vconfig
	net-misc/wget
	net-wireless/b43-fwcutter
	net-wireless/iw
	net-wireless/wireless-tools
	net-wireless/wpa_supplicant
	sys-apps/busybox
	sys-apps/ethtool
	sys-apps/flashrom
	sys-apps/fxload
	sys-apps/gptfdisk
	sys-apps/hdparm
	sys-apps/hwinfo
	sys-apps/iproute2
	sys-apps/memtester
	sys-apps/netplug
	sys-apps/nvme-cli
	sys-apps/pciutils
	sys-apps/pcmciautils
	sys-apps/sdparm
	sys-apps/usbutils
	sys-apps/util-linux
	sys-block/gparted
	sys-block/parted
	sys-block/partimage
	sys-block/whdd
	sys-firmware/ipw2100-firmware
	sys-firmware/ipw2200-firmware
	sys-fs/bcache-tools
	sys-fs/btrfs-progs
	sys-fs/cryptsetup
	sys-fs/ddrescue
	sys-fs/dmraid
	sys-fs/dosfstools
	sys-fs/e2fsprogs
	sys-fs/exfat-utils
	sys-fs/fuse-exfat
	sys-fs/f2fs-tools
	sys-fs/growpart
	sys-fs/jfsutils
	sys-fs/lsscsi
	sys-fs/lvm2
	sys-fs/mac-fdisk
	sys-fs/mdadm
	sys-fs/multipath-tools
	sys-fs/ntfs3g
	sys-fs/reiserfsprogs
	sys-fs/xfsprogs
	sys-kernel/linux-firmware
	sys-libs/gpm
	sys-power/acpid
	www-client/firefox
	www-client/links
	x11-misc/sddm

