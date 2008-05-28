Name: x11-driver-video-savage
Version: 2.2.1
Release: %mkrel 1
Summary: X.org driver for S3 Savage Cards
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-savage-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libdrm-devel >= 2.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: GL-devel

Conflicts: xorg-x11-server < 7.0

%description
x11-driver-video-savage is the X.org driver for S3 Savage Cards.

%prep
%setup -q -n xf86-video-savage-%{version}

%build
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
