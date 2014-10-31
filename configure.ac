AC_INIT([hargyllcms], [1.7.0])
AC_CONFIG_HEADERS([config.h])
AC_CONFIG_AUX_DIR([build-aux])
AC_CONFIG_MACRO_DIR([m4])
AM_INIT_AUTOMAKE([1.11 -Wno-portability no-dist-gzip dist-xz tar-ustar])

AC_PROG_CC
AC_PROG_RANLIB
AC_PROG_INSTALL

AM_PROG_LIBTOOL
AC_PROG_LIBTOOL

AC_PATH_XTRA


# libtool versioning - this applies to libargyll, libargyllusb and libargyllicc
#
# See http://sources.redhat.com/autobook/autobook/autobook_91.html#SEC91 for details
#
# increment;
# CURRENT	If the API or ABI interface has changed (reset REVISION to 0)
# REVISION	If the API and ABI remains the same, but bugs are fixed.
# AGE		If libzif can be linked into executables which can be
# 		built with previous versions of this library. Don't use.
LT_CURRENT=0
LT_REVISION=0
LT_AGE=0
AC_SUBST(LT_CURRENT)
AC_SUBST(LT_REVISION)
AC_SUBST(LT_AGE)

PKG_CHECK_MODULES(PNG, [libpng])
PKG_CHECK_MODULES(USB, [libusb-1.0 >= 1.0.0])
AC_CHECK_LIB(m, sqrt)
AC_CHECK_LIB(z, inflate)
AC_CHECK_LIB(pthread, pthread_create)

AC_CHECK_LIB(tiff, TIFFOpen, TIFF_LIBS="-ltiff", , -lm)
AC_SUBST([TIFF_LIBS])

AC_CHECK_LIB(jpeg, jpeg_finish_decompress, JPEG_LIBS="-ljpeg", , -lm)
AC_SUBST([JPEG_LIBS])

AC_CHECK_FUNC([dlopen], [],
              AC_CHECK_LIB([dl], [dlopen], DLOPEN_LIBS="-ldl"))
AC_SUBST([DLOPEN_LIBS])

AC_CHECK_LIB(X11, XOpenDisplay, X_LIBS="$X_LIBS -lX11")
AC_CHECK_LIB(Xext, XextFindDisplay, X_LIBS="$X_LIBS -lXext",,-lX11)
AC_CHECK_LIB(Xrandr, XRRRootToScreen, X_LIBS="$X_LIBS -lXrandr",,-LXext -lX11)
AC_CHECK_LIB(Xinerama, XineramaQueryScreens, X_LIBS="$X_LIBS -lXinerama",,-LXext -lX11)
AC_CHECK_LIB(Xxf86vm, XF86VidModeGetGamma, X_LIBS="$X_LIBS -lXxf86vm",,-lXext -lX11)
AC_SUBST([X_LIBS])

# udev rules go in /lib, not /usr/lib
if test "$prefix" = "/usr" -o "$prefix" = "/usr/local" ; then
  slashlibdir=/lib
else
  slashlibdir=$prefix/lib
fi
AC_SUBST(slashlibdir)

AC_CONFIG_FILES([Makefile
                 lib/Makefile
                 jcnf/Makefile
                 cgats/Makefile
                 doc/Makefile
                 gamut/Makefile
                 h/Makefile
                 icc/Makefile
                 imdi/Makefile
                 link/Makefile
                 numlib/Makefile
                 plot/Makefile
                 profile/Makefile
                 ref/Makefile
                 render/Makefile
                 rspl/Makefile
                 scanin/Makefile
                 spectro/Makefile
                 target/Makefile
                 tweak/Makefile
                 xicc/Makefile
                 tools/Makefile])
AC_OUTPUT
