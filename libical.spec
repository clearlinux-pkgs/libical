#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libical
Version  : 3.0.1
Release  : 5
URL      : https://github.com/libical/libical/releases/download/v3.0.1/libical-3.0.1.tar.gz
Source0  : https://github.com/libical/libical/releases/download/v3.0.1/libical-3.0.1.tar.gz
Summary  : An implementation of basic iCAL protocols
Group    : Development/Tools
License  : BSD-3-Clause LGPL-2.1 MPL-2.0 MPL-2.0-no-copyleft-exception
Requires: libical-lib
BuildRequires : cmake
BuildRequires : glib-dev
BuildRequires : libxml2-dev
BuildRequires : tzdata

%description
Arnout Engelen pointed out, that you could create a php libical wrapper:
PHP currently seems to lack proper iCalendar libraries.
Since there already is a LibicalWrap.i for the Python
bindings, it's not very hard to make a libical .so that
can be accessed from PHP. Would be a valuable building
block in the practical adoption of the iCalendar
standard (imho).

%package dev
Summary: dev components for the libical package.
Group: Development
Requires: libical-lib
Provides: libical-devel

%description dev
dev components for the libical package.


%package lib
Summary: lib components for the libical package.
Group: Libraries

%description lib
lib components for the libical package.


%prep
%setup -q -n libical-3.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1511128027
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib64 -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib
make VERBOSE=1  %{?_smp_mflags}
popd

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
pushd clr-build ; make test ||: ; popd

%install
export SOURCE_DATE_EPOCH=1511128027
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/lib64/cmake/LibIcal/LibIcalConfig.cmake
/usr/lib64/cmake/LibIcal/LibIcalConfigVersion.cmake
/usr/lib64/cmake/LibIcal/LibIcalTargets-relwithdebinfo.cmake
/usr/lib64/cmake/LibIcal/LibIcalTargets.cmake

%files dev
%defattr(-,root,root,-)
/usr/include/libical-glib/i-cal-array.h
/usr/include/libical-glib/i-cal-attach.h
/usr/include/libical-glib/i-cal-comp-iter.h
/usr/include/libical-glib/i-cal-component.h
/usr/include/libical-glib/i-cal-datetimeperiod-type.h
/usr/include/libical-glib/i-cal-derived-parameter.h
/usr/include/libical-glib/i-cal-derived-property.h
/usr/include/libical-glib/i-cal-derived-value.h
/usr/include/libical-glib/i-cal-duration-type.h
/usr/include/libical-glib/i-cal-enums.h
/usr/include/libical-glib/i-cal-error.h
/usr/include/libical-glib/i-cal-forward-declarations.h
/usr/include/libical-glib/i-cal-geo-type.h
/usr/include/libical-glib/i-cal-langbind.h
/usr/include/libical-glib/i-cal-memory.h
/usr/include/libical-glib/i-cal-mime.h
/usr/include/libical-glib/i-cal-object.h
/usr/include/libical-glib/i-cal-parameter.h
/usr/include/libical-glib/i-cal-parser.h
/usr/include/libical-glib/i-cal-period-type.h
/usr/include/libical-glib/i-cal-property.h
/usr/include/libical-glib/i-cal-recur-iterator.h
/usr/include/libical-glib/i-cal-recur.h
/usr/include/libical-glib/i-cal-recurrence-type.h
/usr/include/libical-glib/i-cal-reqstat-type.h
/usr/include/libical-glib/i-cal-restriction.h
/usr/include/libical-glib/i-cal-time-span.h
/usr/include/libical-glib/i-cal-time.h
/usr/include/libical-glib/i-cal-timetype.h
/usr/include/libical-glib/i-cal-timezone-phase.h
/usr/include/libical-glib/i-cal-timezone.h
/usr/include/libical-glib/i-cal-timezonetype.h
/usr/include/libical-glib/i-cal-trigger-type.h
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
/usr/lib64/libical-glib.so
/usr/lib64/libical.so
/usr/lib64/libical_cxx.so
/usr/lib64/libicalss.so
/usr/lib64/libicalss_cxx.so
/usr/lib64/libicalvcal.so
/usr/lib64/pkgconfig/libical-glib.pc
/usr/lib64/pkgconfig/libical.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libical-glib.so.3
/usr/lib64/libical-glib.so.3.0.1
/usr/lib64/libical.so.3
/usr/lib64/libical.so.3.0.1
/usr/lib64/libical_cxx.so.3
/usr/lib64/libical_cxx.so.3.0.1
/usr/lib64/libicalss.so.3
/usr/lib64/libicalss.so.3.0.1
/usr/lib64/libicalss_cxx.so.3
/usr/lib64/libicalss_cxx.so.3.0.1
/usr/lib64/libicalvcal.so.3
/usr/lib64/libicalvcal.so.3.0.1
