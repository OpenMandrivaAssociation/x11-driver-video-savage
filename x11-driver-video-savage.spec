%define _disable_ld_no_undefined 1

Summary:	X.org driver for S3 Savage Cards
Name:		x11-driver-video-savage
Version:	2.3.8.20161117
Release:	3
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-savage-%{version}.tar.bz2
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-savage is the X.org driver for S3 Savage Cards.

%prep
%setup -qn xf86-video-savage-%{version}
%apply_patches
[ -e autogen.sh ] && ./autogen.sh

%build
%configure
%make

%install
%makeinstall_std

%files
%{_libdir}/xorg/modules/drivers/savage_drv.so
%{_mandir}/man4/savage.*

