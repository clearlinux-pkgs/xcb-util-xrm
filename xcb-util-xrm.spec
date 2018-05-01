#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xcb-util-xrm
Version  : 1.3
Release  : 1
URL      : https://github.com/Airblader/xcb-util-xrm/releases/download/v1.3/xcb-util-xrm-1.3.tar.bz2
Source0  : https://github.com/Airblader/xcb-util-xrm/releases/download/v1.3/xcb-util-xrm-1.3.tar.bz2
Summary  : XCB X resource manager utility functions
Group    : Development/Tools
License  : MIT
Requires: xcb-util-xrm-lib
BuildRequires : doxygen
BuildRequires : graphviz
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xcb-aux)
BuildRequires : pkgconfig(xorg-macros)

%description
About XCB util modules
======================
The XCB util modules provides a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%package dev
Summary: dev components for the xcb-util-xrm package.
Group: Development
Requires: xcb-util-xrm-lib
Provides: xcb-util-xrm-devel

%description dev
dev components for the xcb-util-xrm package.


%package lib
Summary: lib components for the xcb-util-xrm package.
Group: Libraries

%description lib
lib components for the xcb-util-xrm package.


%prep
%setup -q -n xcb-util-xrm-1.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1525195418
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1525195418
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/xcb/xcb_xrm.h
/usr/lib64/libxcb-xrm.so
/usr/lib64/pkgconfig/xcb-xrm.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libxcb-xrm.so.0
/usr/lib64/libxcb-xrm.so.0.0.0
