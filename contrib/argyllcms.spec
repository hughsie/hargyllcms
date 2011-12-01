Name:    argyllcms
Version: 1.3.5
Release: 1%{?dist}
Summary: ICC compatible color management system
Group:   User Interface/X
License: GPLv3 and MIT
URL:     http://gitorious.org/hargyllcms
Source0: http://people.freedesktop.org/~hughsient/releases/hargyllcms-%{version}.tar.xz
BuildRequires: libtiff-devel
BuildRequires: libusb1-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libXinerama-devel
BuildRequires: libXScrnSaver-devel
BuildRequires: libXrandr-devel
Requires: udev

%description
The Argyll color management system supports accurate ICC profile creation for
acquisition devices, CMYK printers, film recorders and calibration and profiling
of displays.

Spectral sample data is supported, allowing a selection of illuminants observer
types, and paper fluorescent whitener additive compensation. Profiles can also
incorporate source specific gamut mappings for perceptual and saturation
intents. Gamut mapping and profile linking uses the CIECAM02 appearance model,
a unique gamut mapping algorithm, and a wide selection of rendering intents. It
also includes code for the fastest portable 8 bit raster color conversion
engine available anywhere, as well as support for fast, fully accurate 16 bit
conversion. Device color gamuts can also be viewed and compared using a VRML
viewer.

%package doc
Summary: Argyll CMS documentation
Group:   User Interface/X
# Does not really make sense without Argyll CMS itself
Requires: %{name} = %{version}-%{release}

%description doc
The Argyll color management system supports accurate ICC profile creation for
acquisition devices, CMYK printers, film recorders and calibration and profiling
of displays.

This package contains the Argyll color management system documentation.

%prep
%setup -q -n hargyllcms-%{version}
# we're not allowed to refer to acquisition devices as scanners
./legal.sh

%build
%configure
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc *.txt

%attr(0755,root,root) %{_bindir}/*
%{_datadir}/color/argyll
/lib/udev/rules.d/55-Argyll.rules

%exclude %{_datadir}/doc

%files doc
%defattr(0644,root,root,0755)
%doc doc/*.html doc/*.jpg doc/*.txt

%changelog
* Thu Dec 01 2011 Richard Hughes <rhughes@redhat.com> - 1.3.5-1
- Rebuild using the hargyll tarball name.
