%define vala 0.11.3
Name:           gupnp-vala
Version:        0.10.3
Release:        %mkrel 1
Summary:        GUPnP is a uPnP framework. This adds vala language bindings
Group:          Development/Other
License:        LGPLv2+
URL:            http://www.gupnp.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.xz
BuildRequires: vala-devel >= %vala
BuildRequires: vala-tools >= %vala
BuildRequires: vala >= %vala
BuildRequires: gssdp-devel >= 0.11
BuildRequires: gupnp-devel >= 0.13.3
BuildRequires: gupnp-av-devel >= 0.5.9
BuildRequires: gupnp-ui-devel
BuildRequires: libsoup-devel
Requires: pkgconfig
Requires: vala >= 0.9.5
BuildArch:	noarch

%description
GUPnP is an object-oriented open source framework for creating UPnP 
devices and control points, written in C using GObject and libsoup. 
The GUPnP API is intended to be easy to use, efficient and flexible. 

This package adds vala language bindings

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%check
make check

%files
%defattr(-,root,root,-)
%doc AUTHORS
%{_datadir}/vala/vapi/*
%{_libdir}/pkgconfig/gupnp-vala-1.0.pc



%changelog
* Mon Feb 13 2012 Götz Waschk <waschk@mandriva.org> 0.10.3-1mdv2012.0
+ Revision: 773748
- update to new version 0.10.3

* Tue Sep 13 2011 Götz Waschk <waschk@mandriva.org> 0.10.2-1
+ Revision: 699678
- update to new version 0.10.2

* Tue Sep 06 2011 Götz Waschk <waschk@mandriva.org> 0.10.1-1
+ Revision: 698455
- new version

* Tue Aug 30 2011 Götz Waschk <waschk@mandriva.org> 0.10.0-1
+ Revision: 697463
- new version
- bump gssdp dep

* Fri Apr 15 2011 Funda Wang <fwang@mandriva.org> 0.8.0-1
+ Revision: 653182
- new version 0.8.0

  + Matthew Dawkins <mattydaw@mandriva.org>
    - new version 0.6.12

* Tue Aug 17 2010 Emmanuel Andry <eandry@mandriva.org> 0.6.11-1mdv2011.0
+ Revision: 570989
- New version 0.6.11
- update BR
- fix files list

* Wed Aug 04 2010 Götz Waschk <waschk@mandriva.org> 0.6.9-1mdv2011.0
+ Revision: 565700
- update to new version 0.6.9

* Tue Aug 03 2010 Funda Wang <fwang@mandriva.org> 0.6.7-1mdv2011.0
+ Revision: 565291
- new version 0.6.7

* Tue Apr 13 2010 Götz Waschk <waschk@mandriva.org> 0.6.5-1mdv2010.1
+ Revision: 534171
- new version
- bump gupnp dep

* Sat Feb 20 2010 Frederik Himpe <fhimpe@mandriva.org> 0.6.4-1mdv2010.1
+ Revision: 508705
- update to new version 0.6.4

* Sun Oct 04 2009 Colin Guthrie <cguthrie@mandriva.org> 0.6-1mdv2010.0
+ Revision: 453271
- Fix group
- import gupnp-vala


* Thu Sep 17 2009 Bastien Nocera <bnocera@redhat.com> 0.6-1
- Update to 0.6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun 21 2009 Peter Robinson <pbrobinson@gmail.com> 0.5.4-2
- Add patch to fix 64 bit pkgconfig paths. Fixes RHBZ 496794

* Wed Jun  3 2009 Peter Robinson <pbrobinson@gmail.com> 0.5.4-1
- New upstream release

* Wed Apr  8 2009 Peter Robinson <pbrobinson@gmail.com> 0.5.3-5
- Rebuild

* Fri Apr  3 2009 Peter Robinson <pbrobinson@gmail.com> 0.5.3-3
- Remove noarch, as its not due to the pkgconfig file

* Tue Mar 10 2009 Peter Robinson <pbrobinson@gmail.com> 0.5.3-2
- Patch for noarch and some reqs thanks to Michel Salim

* Wed Feb 25 2009 Peter Robinson <pbrobinson@gmail.com> 0.5.3-1
- New upstream version, review request fixes, update spec for new version

* Wed Jan 14 2009 Peter Robinson <pbrobinson@gmail.com> 0.5-1
- New upstream version

* Wed Dec 31 2008 Peter Robinson <pbrobinson@gmail.com> 0.4-1
- Update to new version to fix compile with newer vala and gupnp releases

* Wed Jul 9 2008 Peter Robinson <pbrobinson@gmail.com> 0.2-2
- Fixed dep on vala-tools

* Wed Jul 9 2008 Peter Robinson <pbrobinson@gmail.com> 0.2-1
- Initial release
