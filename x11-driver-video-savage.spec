Name: x11-driver-video-savage
Version: 2.3.6
Release: 2
Summary: X.org driver for S3 Savage Cards
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-savage-%{version}.tar.bz2

BuildRequires: libdrm-devel >= 2.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.12
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: pkgconfig(gl)

Requires: x11-server-common %(xserver-sdk-abi-requires videodrv)

Conflicts: xorg-x11-server < 7.0

%description
x11-driver-video-savage is the X.org driver for S3 Savage Cards.

%prep
%setup -qn xf86-video-savage-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%{_libdir}/xorg/modules/drivers/savage_drv.so
%{_mandir}/man4/savage.*



%changelog
* Mon Jul 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.3.6-1
+ Revision: 810701
- version update 2.3.6

* Fri Jul 06 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.3.5-1
+ Revision: 808303
- version update 2.3.5

* Tue Mar 27 2012 Bernhard Rosenkraenzer <bero@bero.eu> 2.3.4-2
+ Revision: 787268
- Rebuild for x11-server 1.12

* Sun Mar 25 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.3.4-1
+ Revision: 786716
- version update 2.3.4

* Sat Dec 31 2011 Matthew Dawkins <mattydaw@mandriva.org> 2.3.3-2
+ Revision: 748455
- rebuild cleaned up spec

* Sun Oct 09 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 2.3.3-1
+ Revision: 703934
- update to new version 2.3.3

* Sat Oct 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 2.3.2-4
+ Revision: 703723
- rebuild for new x11-server

* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 2.3.2-3
+ Revision: 683585
- Rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 2.3.2-2
+ Revision: 671166
- mass rebuild

* Sun Dec 05 2010 Thierry Vignaud <tv@mandriva.org> 2.3.2-1mdv2011.0
+ Revision: 610591
- new release

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 2.3.1-3mdv2011.0
+ Revision: 595717
- require xorg server with proper ABI

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 2.3.1-2mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Mon Aug 03 2009 Thierry Vignaud <tv@mandriva.org> 2.3.1-1mdv2010.0
+ Revision: 407720
- new release

* Fri Jul 03 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 2.3.0-1mdv2010.0
+ Revision: 391904
- update to new version 2.3.0

* Tue Dec 30 2008 Colin Guthrie <cguthrie@mandriva.org> 2.2.1-4mdv2009.1
+ Revision: 321381
- Rebuild for new xserver

* Sat Nov 29 2008 Adam Williamson <awilliamson@mandriva.org> 2.2.1-3mdv2009.1
+ Revision: 308175
- rebuild for new X server

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 2.2.1-2mdv2009.0
+ Revision: 265928
- rebuild early 2009.0 package (before pixel changes)
- improved description
- add missing dot at end of description
- improved summary

* Tue May 27 2008 Colin Guthrie <cguthrie@mandriva.org> 2.2.1-1mdv2009.0
+ Revision: 211784
- New version
- Drop patch (merged upstream)

* Mon Feb 11 2008 Paulo Andrade <pcpa@mandriva.com.br> 2.1.3-5mdv2008.1
+ Revision: 165610
- Revert to use upstream tarball and remove local patches.

* Tue Jan 22 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 2.1.3-4mdv2008.1
+ Revision: 156618
- re-enable rpm debug packages support

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 2.1.3-3mdv2008.1
+ Revision: 154796
- Updated BuildRequires and resubmit package.
- Remove -devel package as it isn't really required as it provides only 2 files
  that aren't even header files; still don't install the .la files.
  All dependency files should be stored in the x11-util-modular package as they
  are only required for the "modular" build.
  Also, add missing patch to remove call to a function that does not exist
  anymore.
- Move .la files to new -devel package, and also add .deps files to -devel package.
- There are signficant changes since xf86-video-savage-2.1.3 branch, so
  while fixing it to use the proper tag for the tarball, the mandriva branch
  was moved down to not include the recent, possibly experimental changes.
- Update for new policy of hidden symbols and common macros.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Oct 16 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 2.1.3-2mdv2008.1
+ Revision: 99045
- minor spec cleanup
- build against new xserver (1.4)

* Fri Aug 17 2007 Thierry Vignaud <tv@mandriva.org> 2.1.3-1mdv2008.0
+ Revision: 64854
- fix man pages
- new release

