Summary:        GUPnP is a uPnP framework. This adds vala language bindings
Name:           gupnp-vala
Version:        0.10.4
Release:        1
Group:          Development/Other
License:        LGPLv2+
URL:            http://www.gupnp.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz

BuildRequires: vala-devel
BuildRequires: vala-tools
BuildRequires: vala
BuildRequires: pkgconfig(gssdp-1.0)
BuildRequires: pkgconfig(gupnp-1.0)
BuildRequires: pkgconfig(gupnp-av-1.0)
BuildRequires: pkgconfig(gupnp-ui-1.0)
BuildRequires: pkgconfig(libsoup-2.4)

Requires: vala >= 0.9.5

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
%doc AUTHORS
%{_datadir}/vala/vapi/*
%{_libdir}/pkgconfig/gupnp-vala-1.0.pc

