AC_INIT([hargyllcms], [1.3.5])
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

PKG_CHECK_MODULES(USB, [libusb-1.0 >= 1.0.0])
AC_CHECK_LIB(m, sqrt)
AC_CHECK_LIB(pthread, pthread_create)

AC_CHECK_LIB(tiff, TIFFOpen, TIFF_LIBS="-ltiff", , -lm)
AC_SUBST([TIFF_LIBS])

AC_CHECK_LIB(X11, XOpenDisplay, X_LIBS="$X_LIBS -lX11")
AC_CHECK_LIB(Xext, XextFindDisplay, X_LIBS="$X_LIBS -lXext",,-lX11)
AC_CHECK_LIB(Xss, XScreenSaverSuspend, X_LIBS="$X_LIBS -lXss",,-lXext -lX11)
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
                 libusb/Makefile
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
