## Process this file with automake to produce Makefile.in

lib_LTLIBRARIES = libargyllicc.la

libargyllicc_la_SOURCES = icc.h iccV42.h icc.c iccstd.c

libargyllicc_la_LIBADD =					\
	$(NULL)

libargyllicc_la_LDFLAGS =					\
	-version-info $(LT_CURRENT):$(LT_REVISION):$(LT_AGE)	\
	-export-dynamic						\
	-no-undefined

bin_PROGRAMS = icctest iccdump icclu

icctest_SOURCES = icctest.c
icctest_LDADD = libargyllicc.la

iccdump_SOURCES = iccdump.c
iccdump_LDADD = libargyllicc.la

icclu_SOURCES = icclu.c
icclu_LDADD = libargyllicc.la

check_PROGRAMS = iccrw lutest

iccrw_SOURCES = iccrw.c
iccrw_LDADD = libargyllicc.la

lutest_SOURCES = lutest.c
lutest_LDADD = libargyllicc.la

EXTRA_DIST = License.txt Readme.txt
