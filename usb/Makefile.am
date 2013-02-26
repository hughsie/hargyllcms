## Process this file with automake to produce Makefile.in

AM_CFLAGS = -DOS_LINUX -DAPI_EXPORTED="/**/" -D_GNU_SOURCE -I$(top_srcdir)/libusb1/libusb

lib_LTLIBRARIES = libargyllusb.la

libargyllusb_la_SOURCES =				\
	driver/abort_endpoint.c				\
	driver/claim_interface.c			\
	driver/clear_feature.c			\
	driver/dispatch.c			\
	driver/driver_api.h			\
	driver/driver_debug.c			\
	driver/driver_debug.h			\
	driver/driver_registry.c			\
	driver/get_configuration.c			\
	driver/get_descriptor.c			\
	driver/get_interface.c			\
	driver/get_status.c			\
	driver/ioctl.c			\
	driver/libusb_driver.c			\
	driver/libusb_driver.h			\
	driver/libusb_driver_rc.rc			\
	driver/lusb_defdi_guids.h			\
	driver/pnp.c			\
	driver/power.c			\
	driver/release_interface.c			\
	driver/reset_device.c			\
	driver/reset_endpoint.c			\
	driver/set_configuration.c			\
	driver/set_descriptor.c			\
	driver/set_feature.c			\
	driver/set_interface.c			\
	driver/transfer.c			\
	driver/usbd.def			\
	driver/usbdlib_gcc.h			\
	driver/vendor_request.c			\
	$(NULL)

libargyllusb_la_LIBADD =					\
	-lrt							\
	$(NULL)

libargyllusb_la_LDFLAGS =					\
	-version-info $(LT_CURRENT):$(LT_REVISION):$(LT_AGE)	\
	-export-dynamic						\
	-no-undefined
