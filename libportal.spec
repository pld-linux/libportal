#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	Flatpak portal library
Summary(pl.UTF-8):	Biblioteka portali Flatpaka
Name:		libportal
Version:	0.3
Release:	1
License:	LGPL v2+
Group:		Libraries
#Source0Download: https://github.com/flatpak/libportal/releases
Source0:	https://github.com/flatpak/libportal/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	dffd58a937dfbabc873e51029dc587f3
URL:		https://github.com/flatpak/libportal
BuildRequires:	glib2-devel >= 1:2.0
BuildRequires:	gtk-doc
BuildRequires:	meson >= 0.46.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libportal provides GIO-style async APIs for most Flatpak portals.

%description -l pl.UTF-8
libportal udostępnia asynchroniczne API w stylu GIO do większości
portali Flatpaka.

%package devel
Summary:	Header files for libportal library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libportal
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libportal library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libportal.

%package static
Summary:	Static libportal library
Summary(pl.UTF-8):	Statyczna biblioteka libportal
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libportal library.

%description static -l pl.UTF-8
Statyczna biblioteka libportal.

%package apidocs
Summary:	API documentation for libportal library
Summary(pl.UTF-8):	Dokumentacja API biblioteki libportal
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for libportal library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libportal.

%prep
%setup -q

%build
%meson build \
	%{!?with_static_libs:--default-library=shared}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_libdir}/libportal.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libportal.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libportal.so
%{_includedir}/libportal
%{_pkgconfigdir}/libportal.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libportal.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libportal
