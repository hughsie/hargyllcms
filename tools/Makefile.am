
# Common CFLAGS for Argyll components
AM_CFLAGS = -DUNIX -I $(top_srcdir)/cgats -I$(top_srcdir)/gamut		\
    -I$(top_srcdir)/h -I$(top_srcdir)/icc				\
    -I$(top_srcdir)/numlib -I$(top_srcdir)/plot -I$(top_srcdir)/profile	\
    -I$(top_srcdir)/render -I$(top_srcdir)/rspl -I$(top_srcdir)/spectro	\
    -I$(top_srcdir)/target -I$(top_srcdir)/xicc	-I$(top_srcdir)/ucmm	\
    -DNATIVE_USB							\
    -DENABLE_USB							\
    -DENABLE_SERIAL							\
    $(PNG_CFLAGS)							\
    $(TIFF_CFLAGS)

bin_PROGRAMS =
check_PROGRAMS =

GAMUT_LDADD =  ../lib/libargyll.la ../icc/libargyllicc.la $(PNG_LIBS)

bin_PROGRAMS += viewgam
viewgam_SOURCES = ../gamut/viewgam.c
viewgam_LDADD = $(GAMUT_LDADD)

check_PROGRAMS += smthtest GenRMGam GenVisGam maptest surftest fakegam

smthtest_SOURCES = ../gamut/smthtest.c
smthtest_LDADD = $(GAMUT_LDADD)

GenRMGam_SOURCES = ../gamut/GenRMGam.c
GenRMGam_LDADD = $(GAMUT_LDADD)

GenVisGam_SOURCES = ../gamut/GenVisGam.c
GenVisGam_LDADD = $(GAMUT_LDADD)

maptest_SOURCES = ../gamut/maptest.c
maptest_LDADD = $(GAMUT_LDADD)

surftest_SOURCES = ../gamut/surftest.c
surftest_LDADD = $(GAMUT_LDADD)

fakegam_SOURCES = ../gamut/fakegam.c
fakegam_LDADD = $(GAMUT_LDADD)

PROFILE_LDADD = 					\
	../lib/libargyll.la ../icc/libargyllicc.la		\
	-lrt			\
	$(TIFF_LIBS) $(X_LIBS) $(PNG_LIBS)

bin_PROGRAMS += simpprof kodak2ti3 cb2ti3 txt2ti3 splitti3	\
	profcheck invprofcheck mppprof mppcheck colverify colprof printcal	\
	applycal
#sepgen

simpprof_SOURCES = ../profile/simpprof.c
simpprof_LDADD = $(PROFILE_LDADD)

kodak2ti3_SOURCES = ../profile/kodak2ti3.c
kodak2ti3_LDADD = $(PROFILE_LDADD)

cb2ti3_SOURCES = ../profile/cb2ti3.c
cb2ti3_LDADD = $(PROFILE_LDADD)

txt2ti3_SOURCES = ../profile/txt2ti3.c
txt2ti3_LDADD = $(PROFILE_LDADD)

splitti3_SOURCES = ../profile/splitti3.c
splitti3_LDADD = $(PROFILE_LDADD)

profcheck_SOURCES = ../profile/profcheck.c
profcheck_LDADD = $(PROFILE_LDADD)

invprofcheck_SOURCES = ../profile/invprofcheck.c
invprofcheck_LDADD = $(PROFILE_LDADD)

mppprof_SOURCES = ../profile/mppprof.c
mppprof_LDADD = $(PROFILE_LDADD)

mppcheck_SOURCES = ../profile/mppcheck.c
mppcheck_LDADD = $(PROFILE_LDADD)

colverify_SOURCES = ../profile/colverify.c
colverify_LDADD = $(PROFILE_LDADD)

colprof_SOURCES = ../profile/colprof.c
colprof_LDADD = $(PROFILE_LDADD)

printcal_SOURCES = ../profile/printcal.c
printcal_LDADD = $(PROFILE_LDADD)

applycal_SOURCES = ../profile/applycal.c
applycal_LDADD = $(PROFILE_LDADD)

#sepgen_SOURCES = ../profile/sepgen.c
#sepgen_LDADD = $(PROFILE_LDADD)


RENDER_LDADD =  ../lib/libargyll.la ../icc/libargyllicc.la $(TIFF_LIBS) $(PNG_LIBS)

check_PROGRAMS += timage

timage_SOURCES = ../render/timage.c
timage_LDADD = $(RENDER_LDADD)

RSPL_LDADD =  ../lib/libargyll.la 	\
	 $(X_LIBS) $(TIFF_LIBS) $(PNG_LIBS) ../icc/libargyllicc.la

check_PROGRAMS += revbench c1 c1df t2d t2ddf t3d t3ddf tnd trnd

revbench_SOURCES = ../rspl/revbench.c
revbench_LDADD = $(RSPL_LDADD)

c1_SOURCES = ../rspl/c1.c
c1_LDADD = $(RSPL_LDADD)

c1df_SOURCES = ../rspl/c1df.c
c1df_LDADD = $(RSPL_LDADD)

t2d_SOURCES = ../rspl/t2d.c
t2d_LDADD = $(RSPL_LDADD)

t2ddf_SOURCES = ../rspl/t2ddf.c
t2ddf_LDADD = $(RSPL_LDADD)

t3d_SOURCES = ../rspl/t3d.c
t3d_LDADD = $(RSPL_LDADD)

t3ddf_SOURCES = ../rspl/t3ddf.c
t3ddf_LDADD = $(RSPL_LDADD)

tnd_SOURCES = ../rspl/tnd.c
tnd_LDADD = $(RSPL_LDADD)

trnd_SOURCES = ../rspl/trnd.c
trnd_LDADD = $(RSPL_LDADD)

SCANIN_LDADD =  ../lib/libargyll.la ../icc/libargyllicc.la	\
	  $(TIFF_LIBS) $(PNG_LIBS)

bin_PROGRAMS += scanin

scanin_SOURCES = ../scanin/scanin.c
scanin_LDADD = $(SCANIN_LDADD)

SPECTRO_LDADD =    	\
	 ../lib/libargyll.la $(X_LIBS) $(YAJL_LIBS)		\
	 ../icc/libargyllicc.la -lrt -ldl $(PNG_LIBS)


bin_PROGRAMS += synthcal dispwin dispread dispcal fakeread synthread	\
	chartread illumread spotread spec2cie average oeminst ccxxmake

synthcal_SOURCES = ../spectro/synthcal.c
synthcal_LDADD = $(SPECTRO_LDADD)

dispwin_SOURCES = ../spectro/dispwin.c
dispwin_CFLAGS = $(AM_CFLAGS) -DSTANDALONE_TEST
dispwin_LDADD = $(SPECTRO_LDADD)

dispread_SOURCES = ../spectro/dispread.c
dispread_LDADD = $(SPECTRO_LDADD)

dispcal_SOURCES = ../spectro/dispcal.c
dispcal_LDADD = $(SPECTRO_LDADD)

fakeread_SOURCES = ../spectro/fakeread.c
fakeread_LDADD = $(SPECTRO_LDADD)

synthread_SOURCES = ../spectro/synthread.c
synthread_LDADD = $(SPECTRO_LDADD)

chartread_SOURCES = ../spectro/chartread.c
chartread_LDADD = $(SPECTRO_LDADD)

illumread_SOURCES = ../spectro/illumread.c
illumread_LDADD = $(SPECTRO_LDADD)

spotread_SOURCES = ../spectro/spotread.c
spotread_LDADD = $(SPECTRO_LDADD)

spec2cie_SOURCES = ../spectro/spec2cie.c
spec2cie_LDADD = $(SPECTRO_LDADD)

average_SOURCES = ../spectro/average.c
average_LDADD = $(SPECTRO_LDADD)

oeminst_SOURCES =			\
	../spectro/LzmaDec.h		\
	../spectro/LzmaTypes.h		\
	../spectro/inflate.c		\
	../spectro/oemarch.c		\
	../spectro/oemarch.h		\
	../spectro/oeminst.c		\
	../spectro/spyd2.c		\
	../spectro/vinflate.c
oeminst_LDADD = $(SPECTRO_LDADD) -lz

ccxxmake_SOURCES = ../spectro/ccxxmake.c
ccxxmake_LDADD = $(SPECTRO_LDADD)

TARGET_LDADD =   	\
	../icc/libargyllicc.la  	\
	../lib/libargyll.la $(TIFF_LIBS) $(PNG_LIBS)

bin_PROGRAMS += targen printtarg

targen_DEPENDENCIES =
targen_SOURCES = ../target/targen.c ../target/targen.h ../target/ofps.c ../target/ofps.h ../target/ifarp.c ../target/ifarp.h	\
	../target/simplat.c ../target/simplat.h ../target/simdlat.c ../target/simdlat.h ../target/prand.c ../target/prand.h
targen_LDADD = $(TARGET_LDADD)

printtarg_SOURCES = ../target/printtarg.c
printtarg_LDADD = $(TARGET_LDADD)

XICC_LDADD =   					\
	../lib/libargyll.la 			\
	../icc/libargyllicc.la			\
	-lrt		\
	-lz		\
	$(TIFF_LIBS) $(JPEG_LIBS) $(X_LIBS) $(PNG_LIBS)

bin_PROGRAMS += fakeCMY iccgamut mpplu revfix tiffgamut xicclu	\
	extracticc extractttag specplot ccttest

fakeCMY_SOURCES = ../xicc/fakeCMY.c

fakeCMY_LDADD = $(XICC_LDADD)

iccgamut_SOURCES = ../xicc/iccgamut.c
iccgamut_LDADD = $(XICC_LDADD)

mpplu_SOURCES = ../xicc/mpplu.c
mpplu_LDADD = $(XICC_LDADD)

revfix_SOURCES = ../xicc/revfix.c
revfix_LDADD = $(XICC_LDADD)

tiffgamut_SOURCES = ../xicc/tiffgamut.c
tiffgamut_LDADD = $(XICC_LDADD)

xicclu_SOURCES = ../xicc/xicclu.c
xicclu_LDADD = $(XICC_LDADD)

extracticc_SOURCES = ../xicc/extracticc.c
extracticc_LDADD = $(XICC_LDADD)

extractttag_SOURCES = ../xicc/extractttag.c
extractttag_LDADD = $(XICC_LDADD)

specplot_SOURCES = ../xicc/specplot.c
specplot_LDADD = $(XICC_LDADD)

ccttest_SOURCES = ../xicc/ccttest.c
ccttest_LDADD = $(XICC_LDADD)

LINK_LDADD =  			\
	 ../icc/libargyllicc.la 	\
	../lib/libargyll.la $(X_LIBS) $(TIFF_LIBS) $(PNG_LIBS)

bin_PROGRAMS += collink pathplot

collink_SOURCES = ../link/collink.c
collink_LDADD = $(LINK_LDADD)

pathplot_SOURCES = ../link/pathplot.c
pathplot_LDADD = $(LINK_LDADD)

TWEAK_LDADD =  			\
	 ../icc/libargyllicc.la 	\
	../lib/libargyll.la $(TIFF_LIBS) $(PNG_LIBS)

bin_PROGRAMS += refine

refine_SOURCES = ../tweak/refine.c
refine_LDADD = $(TWEAK_LDADD)

NUMLIB_LDADD = ../lib/libargyll.la ../icc/libargyllicc.la $(PNG_LIBS)

check_PROGRAMS += dnsqtest tpowell tdhsx LUtest svdtest zbrenttest	\
	soboltest

dnsqtest_SOURCES = ../numlib/dnsqtest.c
dnsqtest_LDADD = $(NUMLIB_LDADD)

tpowell_SOURCES = ../numlib/tpowell.c
tpowell_LDADD = $(NUMLIB_LDADD)

tdhsx_SOURCES = ../numlib/tdhsx.c
tdhsx_LDADD = $(NUMLIB_LDADD)

LUtest_SOURCES = ../numlib/LUtest.c
LUtest_LDADD = $(NUMLIB_LDADD)

svdtest_SOURCES = ../numlib/svdtest.c
svdtest_LDADD = $(NUMLIB_LDADD)

zbrenttest_SOURCES = ../numlib/zbrenttest.c
zbrenttest_LDADD = $(NUMLIB_LDADD)

soboltest_SOURCES = ../numlib/soboltest.c
soboltest_LDADD = $(NUMLIB_LDADD)

bin_PROGRAMS += iccdump icclu
noinst_PROGRAMS = icctest

iccdump_DEPENDENCIES =
iccdump_SOURCES = ../icc/iccdump.c
iccdump_LDADD = ../icc/libargyllicc.la

icclu_DEPENDENCIES =
icclu_SOURCES = ../icc/icclu.c
icclu_LDADD = ../icc/libargyllicc.la

icctest_DEPENDENCIES =
icctest_SOURCES = ../icc/icctest.c
icctest_LDADD = ../icc/libargyllicc.la

bin_PROGRAMS += cctiff greytiff
noinst_PROGRAMS += ctest itest

cctiff_SOURCES = ../imdi/cctiff.c
cctiff_LDADD =   					\
	../lib/libargyll.la 			\
	../icc/libargyllicc.la			\
	../imdi/libimdi.la				\
	$(TIFF_LIBS) $(JPEG_LIBS) $(PNG_LIBS)

greytiff_SOURCES = ../imdi/greytiff.c
greytiff_LDADD =   					\
	../lib/libargyll.la 			\
	../icc/libargyllicc.la			\
	../imdi/libimdi.la				\
	$(TIFF_LIBS) $(PNG_LIBS)

ctest_DEPENDENCIES =
ctest_SOURCES = ../imdi/ctest.c ../imdi/cgen.c
ctest_LDADD =   					\
	../imdi/libimdi.la

itest_DEPENDENCIES =
itest_SOURCES = ../imdi/itest.c ../imdi/refi.c
itest_LDADD =   					\
	../lib/libargyll.la   			\
	../imdi/libimdi.la $(PNG_LIBS)

