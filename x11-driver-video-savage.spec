Name: x11-driver-video-savage
Version: 2.1.3
Release: %mkrel 3
Summary: The X.org driver for S3 Savage Cards
Group: System/X11

########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-video-savage  xorg/drivers/xf86-video-savage
# cd xorg/drivers/xf86-video/savage
# git-archive --format=tar --prefix=xf86-video-savage-2.1.3/ master | bzip2 -9 > xf86-video-savage-2.1.3.tar.bz2
########################################################################
Source0: xf86-video-savage-%{version}.tar.bz2

License: MIT
BuildRoot: %{_tmppath}/%{name}-root

########################################################################
# git-format-patch master..origin/mandriva+gpl
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################

BuildRequires: libdrm-devel >= 2.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: GL-devel

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

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/savage_drv.la
%{_libdir}/xorg/modules/drivers/savage_drv.so
%{_mandir}/man4/savage.*
