%define vala 0.8.0
Name:           gupnp-vala
Version:        0.6.9
Release:        %mkrel 1
Summary:        GUPnP is a uPnP framework. This adds vala language bindings
Group:          Development/Other
License:        LGPLv2+
URL:            http://www.gupnp.org/
Source0:        http://www.gupnp.org/sites/all/files/sources/%name-%version.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: vala-devel >= %vala
BuildRequires: vala-tools >= %vala
BuildRequires: vala >= %vala
BuildRequires: gssdp-devel >= 0.6.4
BuildRequires: gupnp-devel >= 0.13.3
BuildRequires: gupnp-av-devel
BuildRequires: gupnp-ui-devel
BuildRequires: libsoup-devel
Requires: pkgconfig
Requires: vala >= 0.7.0

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
rm -rf %{buildroot}
%makeinstall_std

%check
make check

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS
# Exclude as file is empty
%exclude %{_datadir}/vala/vapi/gssdp-1.0.deps
%{_datadir}/vala/vapi/gssdp-1.0.vapi
%{_datadir}/vala/vapi/gupnp-1.0.deps
%{_datadir}/vala/vapi/gupnp-1.0.vapi
%{_datadir}/vala/vapi/gupnp-av-1.0.deps
%{_datadir}/vala/vapi/gupnp-av-1.0.vapi
%{_datadir}/vala/vapi/gupnp-ui-1.0.deps
%{_datadir}/vala/vapi/gupnp-ui-1.0.vapi
%{_libdir}/pkgconfig/gupnp-vala-1.0.pc

