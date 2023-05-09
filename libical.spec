#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
Name     : libical
Version  : 3.0.16
Release  : 32
URL      : https://github.com/libical/libical/archive/v3.0.16/libical-3.0.16.tar.gz
Source0  : https://github.com/libical/libical/archive/v3.0.16/libical-3.0.16.tar.gz
Summary  : An implementation of basic iCAL protocols
Group    : Development/Tools
License  : BSD-3-Clause LGPL-2.1 MPL-2.0 MPL-2.0-no-copyleft-exception
Requires: libical-data = %{version}-%{release}
Requires: libical-lib = %{version}-%{release}
Requires: libical-libexec = %{version}-%{release}
Requires: libical-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-gnome
BuildRequires : docbook-xml
BuildRequires : doxygen
BuildRequires : glib-dev
BuildRequires : gtk-doc
BuildRequires : icu4c-dev
BuildRequires : libxml2-dev
BuildRequires : perl
BuildRequires : pkg-config
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gobject-introspection-1.0)
BuildRequires : pkgconfig(gtk-doc)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pygobject
BuildRequires : tzdata
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Arnout Engelen pointed out, that you could create a php libical wrapper:
PHP currently seems to lack proper iCalendar libraries.
Since there already is a LibicalWrap.i for the Python
bindings, it's not very hard to make a libical .so that
can be accessed from PHP. Would be a valuable building
block in the practical adoption of the iCalendar
standard (imho).

%package data
Summary: data components for the libical package.
Group: Data

%description data
data components for the libical package.


%package dev
Summary: dev components for the libical package.
Group: Development
Requires: libical-lib = %{version}-%{release}
Requires: libical-data = %{version}-%{release}
Provides: libical-devel = %{version}-%{release}
Requires: libical = %{version}-%{release}

%description dev
dev components for the libical package.


%package doc
Summary: doc components for the libical package.
Group: Documentation

%description doc
doc components for the libical package.


%package lib
Summary: lib components for the libical package.
Group: Libraries
Requires: libical-data = %{version}-%{release}
Requires: libical-libexec = %{version}-%{release}
Requires: libical-license = %{version}-%{release}

%description lib
lib components for the libical package.


%package libexec
Summary: libexec components for the libical package.
Group: Default
Requires: libical-license = %{version}-%{release}

%description libexec
libexec components for the libical package.


%package license
Summary: license components for the libical package.
Group: Default

%description license
license components for the libical package.


%prep
%setup -q -n libical-3.0.16
cd %{_builddir}/libical-3.0.16

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1683655033
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake .. -DGOBJECT_INTROSPECTION=true -DICAL_GLIB_VAPI=true
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake .. -DGOBJECT_INTROSPECTION=true -DICAL_GLIB_VAPI=true
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test || :
cd ../clr-build-avx2;
make test || : || :

%install
export SOURCE_DATE_EPOCH=1683655033
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libical
cp %{_builddir}/libical-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libical/3bf3cf94d36c740565ea0b38105f1dc5ee25c695 || :
cp %{_builddir}/libical-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/libical/e06cc15cb9b44cb1aa2f5210a92baa95ceb2978e || :
cp %{_builddir}/libical-%{version}/LICENSE.LGPL21.txt %{buildroot}/usr/share/package-licenses/libical/3f96533507f18e90b0358965251430691823209a || :
cp %{_builddir}/libical-%{version}/LICENSE.MPL2.txt %{buildroot}/usr/share/package-licenses/libical/d7e3ed5ac149ac1e2d2e0f4daff081c1dafef1c0 || :
cp %{_builddir}/libical-%{version}/debian/copyright %{buildroot}/usr/share/package-licenses/libical/8c589624765e6a849a00a07166fafe0e2f8dd463 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/ICal-3.0.typelib
/usr/lib64/girepository-1.0/ICalGLib-3.0.typelib
/usr/share/gir-1.0/*.gir
/usr/share/vala/vapi/libical-glib.vapi

%files dev
%defattr(-,root,root,-)
/V3/usr/lib64/libical-glib.so
/V3/usr/lib64/libical.so
/V3/usr/lib64/libical_cxx.so
/V3/usr/lib64/libicalss.so
/V3/usr/lib64/libicalss_cxx.so
/V3/usr/lib64/libicalvcal.so
/usr/include/libical-glib/i-cal-array.h
/usr/include/libical-glib/i-cal-attach.h
/usr/include/libical-glib/i-cal-comp-iter.h
/usr/include/libical-glib/i-cal-component.h
/usr/include/libical-glib/i-cal-datetimeperiod.h
/usr/include/libical-glib/i-cal-derived-parameter.h
/usr/include/libical-glib/i-cal-derived-property.h
/usr/include/libical-glib/i-cal-derived-value.h
/usr/include/libical-glib/i-cal-duration.h
/usr/include/libical-glib/i-cal-enums.h
/usr/include/libical-glib/i-cal-error.h
/usr/include/libical-glib/i-cal-forward-declarations.h
/usr/include/libical-glib/i-cal-geo.h
/usr/include/libical-glib/i-cal-memory.h
/usr/include/libical-glib/i-cal-mime.h
/usr/include/libical-glib/i-cal-object.h
/usr/include/libical-glib/i-cal-parameter.h
/usr/include/libical-glib/i-cal-parser.h
/usr/include/libical-glib/i-cal-period.h
/usr/include/libical-glib/i-cal-property.h
/usr/include/libical-glib/i-cal-recur-iterator.h
/usr/include/libical-glib/i-cal-recur.h
/usr/include/libical-glib/i-cal-recurrence.h
/usr/include/libical-glib/i-cal-reqstat.h
/usr/include/libical-glib/i-cal-restriction.h
/usr/include/libical-glib/i-cal-time-span.h
/usr/include/libical-glib/i-cal-time.h
/usr/include/libical-glib/i-cal-timezone.h
/usr/include/libical-glib/i-cal-trigger.h
/usr/include/libical-glib/i-cal-unknowntokenhandling.h
/usr/include/libical-glib/i-cal-value.h
/usr/include/libical-glib/libical-glib.h
/usr/include/libical/ical.h
/usr/include/libical/icalarray.h
/usr/include/libical/icalattach.h
/usr/include/libical/icalcalendar.h
/usr/include/libical/icalclassify.h
/usr/include/libical/icalcluster.h
/usr/include/libical/icalcomponent.h
/usr/include/libical/icalderivedparameter.h
/usr/include/libical/icalderivedproperty.h
/usr/include/libical/icalderivedvalue.h
/usr/include/libical/icaldirset.h
/usr/include/libical/icaldirsetimpl.h
/usr/include/libical/icalduration.h
/usr/include/libical/icalenums.h
/usr/include/libical/icalerror.h
/usr/include/libical/icalfileset.h
/usr/include/libical/icalfilesetimpl.h
/usr/include/libical/icalgauge.h
/usr/include/libical/icalgaugeimpl.h
/usr/include/libical/icallangbind.h
/usr/include/libical/icalmemory.h
/usr/include/libical/icalmessage.h
/usr/include/libical/icalmime.h
/usr/include/libical/icalparameter.h
/usr/include/libical/icalparameter_cxx.h
/usr/include/libical/icalparser.h
/usr/include/libical/icalperiod.h
/usr/include/libical/icalproperty.h
/usr/include/libical/icalproperty_cxx.h
/usr/include/libical/icalrecur.h
/usr/include/libical/icalrestriction.h
/usr/include/libical/icalset.h
/usr/include/libical/icalspanlist.h
/usr/include/libical/icalspanlist_cxx.h
/usr/include/libical/icalss.h
/usr/include/libical/icalssyacc.h
/usr/include/libical/icaltime.h
/usr/include/libical/icaltimezone.h
/usr/include/libical/icaltypes.h
/usr/include/libical/icaltz-util.h
/usr/include/libical/icalvalue.h
/usr/include/libical/icalvalue_cxx.h
/usr/include/libical/icalvcal.h
/usr/include/libical/icptrholder_cxx.h
/usr/include/libical/libical_ical_export.h
/usr/include/libical/libical_icalss_export.h
/usr/include/libical/libical_vcal_export.h
/usr/include/libical/pvl.h
/usr/include/libical/sspm.h
/usr/include/libical/vcaltmp.h
/usr/include/libical/vcc.h
/usr/include/libical/vcomponent_cxx.h
/usr/include/libical/vobject.h
/usr/lib64/cmake/LibIcal/IcalGlibSrcGenerator-relwithdebinfo.cmake
/usr/lib64/cmake/LibIcal/IcalGlibSrcGenerator.cmake
/usr/lib64/cmake/LibIcal/LibIcalConfig.cmake
/usr/lib64/cmake/LibIcal/LibIcalConfigVersion.cmake
/usr/lib64/cmake/LibIcal/LibIcalTargets-relwithdebinfo.cmake
/usr/lib64/cmake/LibIcal/LibIcalTargets.cmake
/usr/lib64/libical-glib.so
/usr/lib64/libical.so
/usr/lib64/libical_cxx.so
/usr/lib64/libicalss.so
/usr/lib64/libicalss_cxx.so
/usr/lib64/libicalvcal.so
/usr/lib64/pkgconfig/libical-glib.pc
/usr/lib64/pkgconfig/libical.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/libical-glib/ICalArray.html
/usr/share/gtk-doc/html/libical-glib/ICalAttach.html
/usr/share/gtk-doc/html/libical-glib/ICalCompIter.html
/usr/share/gtk-doc/html/libical-glib/ICalComponent.html
/usr/share/gtk-doc/html/libical-glib/ICalDatetimeperiod.html
/usr/share/gtk-doc/html/libical-glib/ICalDuration.html
/usr/share/gtk-doc/html/libical-glib/ICalGeo.html
/usr/share/gtk-doc/html/libical-glib/ICalObject.html
/usr/share/gtk-doc/html/libical-glib/ICalParameter.html
/usr/share/gtk-doc/html/libical-glib/ICalParser.html
/usr/share/gtk-doc/html/libical-glib/ICalPeriod.html
/usr/share/gtk-doc/html/libical-glib/ICalProperty.html
/usr/share/gtk-doc/html/libical-glib/ICalRecurIterator.html
/usr/share/gtk-doc/html/libical-glib/ICalRecurrence.html
/usr/share/gtk-doc/html/libical-glib/ICalReqstat.html
/usr/share/gtk-doc/html/libical-glib/ICalTime.html
/usr/share/gtk-doc/html/libical-glib/ICalTimeSpan.html
/usr/share/gtk-doc/html/libical-glib/ICalTimezone.html
/usr/share/gtk-doc/html/libical-glib/ICalTrigger.html
/usr/share/gtk-doc/html/libical-glib/ICalValue.html
/usr/share/gtk-doc/html/libical-glib/annotation-glossary.html
/usr/share/gtk-doc/html/libical-glib/api-index-1-0.html
/usr/share/gtk-doc/html/libical-glib/api-index-2-0.html
/usr/share/gtk-doc/html/libical-glib/api-index-3-0-5.html
/usr/share/gtk-doc/html/libical-glib/api-index-3-0.html
/usr/share/gtk-doc/html/libical-glib/api-index-full.html
/usr/share/gtk-doc/html/libical-glib/ch01.html
/usr/share/gtk-doc/html/libical-glib/home.png
/usr/share/gtk-doc/html/libical-glib/index.html
/usr/share/gtk-doc/html/libical-glib/left-insensitive.png
/usr/share/gtk-doc/html/libical-glib/left.png
/usr/share/gtk-doc/html/libical-glib/libical-glib-i-cal-derived-parameter.html
/usr/share/gtk-doc/html/libical-glib/libical-glib-i-cal-derived-property.html
/usr/share/gtk-doc/html/libical-glib/libical-glib-i-cal-derived-value.html
/usr/share/gtk-doc/html/libical-glib/libical-glib-i-cal-enums.html
/usr/share/gtk-doc/html/libical-glib/libical-glib-i-cal-error.html
/usr/share/gtk-doc/html/libical-glib/libical-glib-i-cal-memory.html
/usr/share/gtk-doc/html/libical-glib/libical-glib-i-cal-mime.html
/usr/share/gtk-doc/html/libical-glib/libical-glib-i-cal-recur.html
/usr/share/gtk-doc/html/libical-glib/libical-glib-i-cal-restriction.html
/usr/share/gtk-doc/html/libical-glib/libical-glib-i-cal-unknowntokenhandling.html
/usr/share/gtk-doc/html/libical-glib/libical-glib.devhelp2
/usr/share/gtk-doc/html/libical-glib/right-insensitive.png
/usr/share/gtk-doc/html/libical-glib/right.png
/usr/share/gtk-doc/html/libical-glib/style.css
/usr/share/gtk-doc/html/libical-glib/up-insensitive.png
/usr/share/gtk-doc/html/libical-glib/up.png

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libical-glib.so.3
/V3/usr/lib64/libical-glib.so.3.0.16
/V3/usr/lib64/libical.so.3
/V3/usr/lib64/libical.so.3.0.16
/V3/usr/lib64/libical_cxx.so.3
/V3/usr/lib64/libical_cxx.so.3.0.16
/V3/usr/lib64/libicalss.so.3
/V3/usr/lib64/libicalss.so.3.0.16
/V3/usr/lib64/libicalss_cxx.so.3
/V3/usr/lib64/libicalss_cxx.so.3.0.16
/V3/usr/lib64/libicalvcal.so.3
/V3/usr/lib64/libicalvcal.so.3.0.16
/usr/lib64/libical-glib.so.3
/usr/lib64/libical-glib.so.3.0.16
/usr/lib64/libical.so.3
/usr/lib64/libical.so.3.0.16
/usr/lib64/libical_cxx.so.3
/usr/lib64/libical_cxx.so.3.0.16
/usr/lib64/libicalss.so.3
/usr/lib64/libicalss.so.3.0.16
/usr/lib64/libicalss_cxx.so.3
/usr/lib64/libicalss_cxx.so.3.0.16
/usr/lib64/libicalvcal.so.3
/usr/lib64/libicalvcal.so.3.0.16

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/libical/ical-glib-src-generator
/usr/libexec/libical/ical-glib-src-generator

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libical/3bf3cf94d36c740565ea0b38105f1dc5ee25c695
/usr/share/package-licenses/libical/3f96533507f18e90b0358965251430691823209a
/usr/share/package-licenses/libical/8c589624765e6a849a00a07166fafe0e2f8dd463
/usr/share/package-licenses/libical/d7e3ed5ac149ac1e2d2e0f4daff081c1dafef1c0
/usr/share/package-licenses/libical/e06cc15cb9b44cb1aa2f5210a92baa95ceb2978e
