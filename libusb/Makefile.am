## Process this file with automake to produce Makefile.in

udevrulesdir = $(slashlibdir)/udev/rules.d/

udevrules_DATA = 55-Argyll.rules

EXTRA_DIST =							\
	$(udevrules_DATA)

AM_CFLAGS = -DOS_LINUX -DAPI_EXPORTED="/**/" -D_GNU_SOURCE -I$(top_srcdir)/libusb1/libusb

lib_LTLIBRARIES = libargyllusb.la

libargyllusb_la_SOURCES =					\
	../libusb1/libusb/core.c				\
	../libusb1/libusb/sync.c				\
	../libusb1/libusb/descriptor.c				\
	../libusb1/libusb/io.c					\
	../libusb1/libusb/libusb.h				\
	../libusb1/libusb/libusbi.h				\
	../libusb1/libusb/os/threads_posix.h			\
	../libusb1/libusb/os/linux_usbfs.c			\
	../libusb1/libusb/os/linux_usbfs.h			\
	../libusb1/libusb/os/poll_posix.h			\
	$(NULL)

libargyllusb_la_LIBADD =					\
	-lrt							\
	$(NULL)

libargyllusb_la_LDFLAGS =					\
	-version-info $(LT_CURRENT):$(LT_REVISION):$(LT_AGE)	\
	-export-dynamic						\
	-no-undefined
