## Process this file with automake to produce Makefile.in

AM_CFLAGS = -I$(top_srcdir)/h

noinst_PROGRAMS = imdi_make

imdi_make_DEPENDENCIES = 
imdi_make_SOURCES = imdi_make.c imdi_gen.c cgen.c

BUILT_SOURCES = imdi_k.h

lib_LTLIBRARIES = libimdi.la

libimdi_la_SOURCES = imdi.h imdi.c imdi_arch.h imdi_gen.h imdi_tab.h imdi_tab.c imdi_utl.h refi.h

libimdi_la_LIBADD =					\
	../icc/libargyllicc.la

libimdi_la_LDFLAGS =					\
	-version-info $(LT_CURRENT):$(LT_REVISION):$(LT_AGE)	\
	-export-dynamic						\
	-no-undefined

EXTRA_DIST = License.txt Readme.txt

clean: clean-am
	rm imdi_k.*

imdi_k.h: imdi_make
	./imdi_make

uninstall: uninstall-am
	rm imdi_k.*
