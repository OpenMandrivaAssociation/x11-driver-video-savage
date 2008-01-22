Name: x11-driver-video-savage
Version: 2.1.3
Release: %mkrel 4
Summary: The X.org driver for S3 Savage Cards
Group: System/X11
URL: http://xorg.freedesktop.org
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-video-savage  xorg/drivers/xf86-video-savage
# cd xorg/drivers/xf86-video/savage
# git-archive --format=tar --prefix=xf86-video-savage-2.1.3/ xf86-video-savage-2.1.3 | bzip2 -9 > xf86-video-savage-2.1.3.tar.bz2
########################################################################
Source0: xf86-video-savage-%{version}.tar.bz2
License: MIT
########################################################################
# git-format-patch -b xf86-video-savage-2.1.3..origin/mandriva+gpl
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################
BuildRequires: x11-util-macros		>= 1.1.5-4mdk
BuildRequires: libdrm-devel		>= 2.3.0
BuildRequires: libpixman-1-devel	>= 0.9.6
BuildRequires: x11-proto-devel		>= 7.3
BuildRequires: libmesagl-devel		>= 7.0.2
BuildRequires: x11-server-devel		>= 1.4
Conflicts: xorg-x11-server < 7.0

%description
The X.org driver for S3 Savage Cards

%prep
%setup -q -n xf86-video-savage-%{version}

%patch1 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}/%{_libdir}/xorg/modules/drivers/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/savage_drv.so
%{_mandir}/man4/savage.*
