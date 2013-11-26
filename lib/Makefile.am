## Process this file with automake to produce Makefile.in

# Common CFLAGS for Argyll components
AM_CFLAGS = -DUNIX -I $(top_srcdir)/cgats -I$(top_srcdir)/gamut		\
    -I$(top_srcdir)/h -I$(top_srcdir)/icc				\
    -I$(top_srcdir)/numlib -I$(top_srcdir)/plot -I$(top_srcdir)/profile	\
    -I$(top_srcdir)/render -I$(top_srcdir)/rspl -I$(top_srcdir)/spectro	\
    -I$(top_srcdir)/target -I$(top_srcdir)/xicc -I$(top_srcdir)/ucmm	\
    -DNATIVE_USB							\
    -DENABLE_USB							\
    -DENABLE_FAST_SERIAL						\
    -DENABLE_SERIAL							\
    $(USB_CFLAGS) $(TIFF_CFLAGS)

lib_LTLIBRARIES = libargyll.la

libargyll_la_SOURCES = ../h/llist.h ../h/sort.h ../h/counters.h ../h/xlist.h ../h/copyright.h ../h/aconfig.h

libargyll_la_SOURCES += ../cgats/pars.c ../cgats/pars.h ../cgats/cgats.c ../cgats/cgats.h ../cgats/parsstd.c	\
	../cgats/cgatsstd.c

libargyll_la_SOURCES += ../ucmm/ucmm.h

libargyll_la_SOURCES += ../gamut/gamut.h ../gamut/gamut.c

libargyll_la_SOURCES += ../gamut/gammap.h ../gamut/gammap.c ../gamut/nearsmth.c ../gamut/nearsmth.h

libargyll_la_SOURCES += ../plot/plot.h ../plot/plot.c

libargyll_la_SOURCES += ../plot/vrml.h ../plot/vrml.c

libargyll_la_SOURCES += ../profile/prof.h ../profile/profin.c ../profile/profout.c

libargyll_la_SOURCES += ../render/render.h ../render/render.c
libargyll_la_SOURCES += ../render/thscreen.h ../render/thscreen.c ../render/screens.h

libargyll_la_SOURCES += ../rspl/rspl.h ../rspl/rspl_imp.h ../rspl/mlbs.h ../rspl/rspl.c ../rspl/scat.c ../rspl/rev.c	\
	../rspl/rev.h ../rspl/gam.c ../rspl/gam.h ../rspl/spline.c ../rspl/opt.c

libargyll_la_SOURCES += ../scanin/scanrd.h ../scanin/scanrd_.h ../scanin/scanrd.c

libargyll_la_SOURCES += ../spectro/insttypes.h ../spectro/insttypes.c	\
	../spectro/insttypeinst.h ../spectro/xdg_bds.h			\
	../spectro/instappsup.h ../spectro/instappsup.c			\
	../spectro/specbos.h ../spectro/specbos.c			\
	../spectro/xdg_bds.c ../spectro/i1d3.c ../spectro/i1d3.h

libargyll_la_SOURCES += ../spectro/inst.h ../spectro/inst.c ../spectro/dtp20.c ../spectro/dtp20.h ../spectro/dtp22.c	\
	../spectro/dtp22.h ../spectro/dtp41.c ../spectro/dtp41.h ../spectro/dtp51.c ../spectro/dtp51.h ../spectro/dtp92.c ../spectro/dtp92.h		\
	../spectro/i1disp.c ../spectro/i1disp.h ../spectro/i1pro.c ../spectro/i1pro.h ../spectro/i1pro_imp.c ../spectro/i1pro_imp.h	\
	../spectro/munki.c ../spectro/munki_imp.c ../spectro/ss.c ../spectro/ss.h ../spectro/ss_imp.c ../spectro/ss_imp.h ../spectro/hcfr.c ../spectro/hcfr.h	\
	../spectro/spyd2.c ../spectro/spyd2.h ../spectro/spyd2setup.h ../spectro/spyd2PLD.h ../spectro/huey.c ../spectro/huey.h	\
	../spectro/usbio.c ../spectro/iusb.h ../spectro/hidio.c ../spectro/pollem.h ../spectro/icoms.h ../spectro/icoms.c ../spectro/conv.h ../spectro/usbio.h	\
	../spectro/hidio.h ../spectro/munki.h ../spectro/munki_imp.h ../spectro/colorhug.c ../spectro/colorhug.h	\
	../spectro/aglob.c ../spectro/aglob.h

# include'd into .c files, urgh
EXTRA_DIST = ../spectro/usbio_lx.c ../spectro/icoms_ux.c

libargyll_la_SOURCES += ../spectro/webwin.h ../spectro/webwin.c
libargyll_la_SOURCES += ../spectro/mongoose.h ../spectro/mongoose.c

libargyll_la_SOURCES += ../spectro/dispsup.c ../spectro/dispwin.c ../spectro/dispwin.h ../spectro/dispsup.h

libargyll_la_SOURCES += ../spectro/conv.c ../spectro/pollem.c

libargyll_la_SOURCES += ../target/alphix.c ../target/alphix.h ../target/randix.c ../target/randix.h


libargyll_la_SOURCES += ../xicc/xicc.h ../xicc/xicc.c ../xicc/xlutfix.c ../xicc/xspect.c ../xicc/xspect.h	\
	../xicc/xdevlin.c ../xicc/xdevlin.h ../xicc/xcam.c ../xicc/xcam.h ../xicc/cam97s3.c ../xicc/cam97s3.h	\
	../xicc/cam02.c ../xicc/cam02.h ../xicc/mpp.c ../xicc/xfit.c ../xicc/xfit.h ../xicc/moncurve.c ../xicc/moncurve.h	\
	../xicc/mpp.h ../xicc/xdgb.c ../xicc/xdgb.h ../xicc/xcal.c ../xicc/xcal.h ../xicc/xcolorants.c ../xicc/xcolorants.h	\
	../xicc/ccmx.c ../xicc/ccmx.h ../xicc/ccss.c ../xicc/ccss.h

libargyll_la_SOURCES += ../xicc/xutils.h ../xicc/xutils.c
libargyll_la_SOURCES += ../xicc/iccjpeg.h ../xicc/iccjpeg.c

libargyll_la_SOURCES += ../numlib/numlib.h ../numlib/numsup.c ../numlib/numsup.h ../numlib/dnsq.c ../numlib/dnsq.h	\
	../numlib/powell.c ../numlib/powell.h ../numlib/dhsx.c ../numlib/dhsx.h ../numlib/ludecomp.c ../numlib/ludecomp.h ../numlib/svd.c	\
	../numlib/svd.h ../numlib/zbrent.c ../numlib/zbrent.h ../numlib/rand.c ../numlib/rand.h ../numlib/sobol.c ../numlib/sobol.h ../numlib/aatree.c ../numlib/aatree.h

libargyll_la_LIBADD =						\
	../icc/libargyllicc.la					\
	$(TIFF_LIBS)						\
	$(JPEG_LIBS)						\
	$(DLOPEN_LIBS)						\
	$(X_LIBS)						\
	$(NULL)

libargyll_la_LDFLAGS =						\
	-version-info $(LT_CURRENT):$(LT_REVISION):$(LT_AGE)	\
	-export-dynamic						\
	-no-undefined
