#
# Conditional build:
%bcond_without	apidocs		# API documentation
%bcond_without	static_libs	# static library
%bcond_without	gtk3		# GTK+ 3 backend
%bcond_without	gtk4		# GTK 4 backend
%bcond_without	qt5		# Qt 5 backend
%bcond_without	qt6		# Qt 6 backend
#
Summary:	Flatpak portal library
Summary(pl.UTF-8):	Biblioteka portali Flatpaka
Name:		libportal
Version:	0.8.1
Release:	1
License:	LGPL v2+
Group:		Libraries
#Source0Download: https://github.com/flatpak/libportal/releases
Source0:	https://github.com/flatpak/libportal/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	3226036adea29ce152d9ca0be5ab0486
URL:		https://github.com/flatpak/libportal
%if %{with qt5}
BuildRequires:	Qt5Core-devel >= 5
BuildRequires:	Qt5Gui-devel >= 5
BuildRequires:	Qt5Test-devel >= 5
BuildRequires:	Qt5Widgets-devel >= 5
BuildRequires:	Qt5X11Extras-devel >= 5
%endif
%if %{with qt6}
BuildRequires:	Qt6Core-devel >= 6
BuildRequires:	Qt6Gui-devel >= 6
BuildRequires:	Qt6Test-devel >= 6
BuildRequires:	Qt6Widgets-devel >= 6
%endif
%{?with_apidocs:BuildRequires:	gi-docgen >= 2021.1}
BuildRequires:	glib2-devel >= 1:2.58
BuildRequires:	gobject-introspection-devel
%{?with_gtk3:BuildRequires:	gtk+3-devel >= 3.0}
%{?with_gtk4:BuildRequires:	gtk4-devel >= 4}
%{?with_qt5:BuildRequires:	libstdc++-devel >= 6:4.7}
%{?with_qt6:BuildRequires:	libstdc++-devel >= 6:7}
BuildRequires:	meson >= 0.59.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.029
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala
BuildRequires:	xz
Requires:	glib2 >= 1:2.58
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
Requires:	glib2-devel >= 1:2.58

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

%package -n vala-libportal
Summary:	Vala API for libportal library
Summary(pl.UTF-8):	API języka Vala do biblioteki libportal
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala

%description -n vala-libportal
Vala API for libportal library.

%description -n vala-libportal -l pl.UTF-8
API języka Vala do biblioteki libportal.

%package gtk3
Summary:	Portal API wrappers (GTK+3)
Summary(pl.UTF-8):	Obudowanie API Portal (GTK+3)
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gtk3
Portal API wrappers (GTK+3).

%description gtk3 -l pl.UTF-8
Obudowanie API Portal (GTK+3).

%package gtk3-devel
Summary:	Header file for libportal-gtk3 library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki libportal-gtk3
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gtk3 = %{version}-%{release}
Requires:	gtk+3-devel >= 3.0

%description gtk3-devel
Header file for libportal-gtk3 library.

%description gtk3-devel -l pl.UTF-8
Plik nagłówkowy biblioteki libportal-gtk3.

%package gtk3-static
Summary:	Static libportal-gtk3 library
Summary(pl.UTF-8):	Statyczna biblioteka libportal-gtk3
Group:		Development/Libraries
Requires:	%{name}-gtk3-devel = %{version}-%{release}

%description gtk3-static
Static libportal-gtk3 library.

%description gtk3-static -l pl.UTF-8
Statyczna biblioteka libportal-gtk3.

%package -n vala-libportal-gtk3
Summary:	Vala API for libportal-gtk3 library
Summary(pl.UTF-8):	API języka Vala do biblioteki libportal-gtk3
Group:		Development/Libraries
Requires:	%{name}-gtk3-devel = %{version}-%{release}
Requires:	vala-libportal

%description -n vala-libportal-gtk3
Vala API for libportal-gtk3 library.

%description -n vala-libportal-gtk3 -l pl.UTF-8
API języka Vala do biblioteki libportal-gtk3.

%package gtk4
Summary:	Portal API wrappers (GTK4)
Summary(pl.UTF-8):	Obudowanie API Portal (GTK4)
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gtk4
Portal API wrappers (GTK4).

%description gtk4 -l pl.UTF-8
Obudowanie API Portal (GTK4).

%package gtk4-devel
Summary:	Header file for libportal-gtk4 library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki libportal-gtk4
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gtk4 = %{version}-%{release}
Requires:	gtk4-devel >= 4

%description gtk4-devel
Header file for libportal-gtk4 library.

%description gtk4-devel -l pl.UTF-8
Plik nagłówkowy biblioteki libportal-gtk4.

%package gtk4-static
Summary:	Static libportal-gtk4 library
Summary(pl.UTF-8):	Statyczna biblioteka libportal-gtk4
Group:		Development/Libraries
Requires:	%{name}-gtk4-devel = %{version}-%{release}

%description gtk4-static
Static libportal-gtk4 library.

%description gtk4-static -l pl.UTF-8
Statyczna biblioteka libportal-gtk4.

%package -n vala-libportal-gtk4
Summary:	Vala API for libportal-gtk4 library
Summary(pl.UTF-8):	API języka Vala do biblioteki libportal-gtk4
Group:		Development/Libraries
Requires:	%{name}-gtk4-devel = %{version}-%{release}
Requires:	vala-libportal

%description -n vala-libportal-gtk4
Vala API for libportal-gtk4 library.

%description -n vala-libportal-gtk4 -l pl.UTF-8
API języka Vala do biblioteki libportal-gtk4.

%package qt5
Summary:	Portal API wrappers (Qt5)
Summary(pl.UTF-8):	Obudowanie API Portal (Qt5)
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description qt5
Portal API wrappers (Qt5).

%description qt5 -l pl.UTF-8
Obudowanie API Portal (Qt5).

%package qt5-devel
Summary:	Header file for libportal-qt5 library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki libportal-qt5
Group:		Development/Libraries
Requires:	Qt5Core-devel >= 5
Requires:	Qt5Gui-devel >= 5
Requires:	Qt5Widgets-devel >= 5
Requires:	Qt5X11Extras-devel >= 5
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-qt5 = %{version}-%{release}

%description qt5-devel
Header file for libportal-qt5 library.

%description qt5-devel -l pl.UTF-8
Plik nagłówkowy biblioteki libportal-qt5.

%package qt5-static
Summary:	Static libportal-qt5 library
Summary(pl.UTF-8):	Statyczna biblioteka libportal-qt5
Group:		Development/Libraries
Requires:	%{name}-qt5-devel = %{version}-%{release}

%description qt5-static
Static libportal-qt5 library.

%description qt5-static -l pl.UTF-8
Statyczna biblioteka libportal-qt5.

%package qt6
Summary:	Portal API wrappers (Qt6)
Summary(pl.UTF-8):	Obudowanie API Portal (Qt6)
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description qt6
Portal API wrappers (Qt6).

%description qt6 -l pl.UTF-8
Obudowanie API Portal (Qt6).

%package qt6-devel
Summary:	Header file for libportal-qt6 library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki libportal-qt6
Group:		Development/Libraries
Requires:	Qt6Core-devel >= 6
Requires:	Qt6Gui-devel >= 6
Requires:	Qt6Widgets-devel >= 6
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-qt6 = %{version}-%{release}

%description qt6-devel
Header file for libportal-qt6 library.

%description qt6-devel -l pl.UTF-8
Plik nagłówkowy biblioteki libportal-qt6.

%package qt6-static
Summary:	Static libportal-qt6 library
Summary(pl.UTF-8):	Statyczna biblioteka libportal-qt6
Group:		Development/Libraries
Requires:	%{name}-qt6-devel = %{version}-%{release}

%description qt6-static
Static libportal-qt6 library.

%description qt6-static -l pl.UTF-8
Statyczna biblioteka libportal-qt6.

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
	%{!?with_static_libs:--default-library=shared} \
	-Dbackend-gtk3=%{__enabled_disabled gtk3} \
	-Dbackend-gtk4=%{__enabled_disabled gtk4} \
	-Dbackend-qt5=%{__enabled_disabled qt5} \
	-Dbackend-qt6=%{__enabled_disabled qt6} \
	%{!?with_apidocs:-Ddocs=false}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%if %{with apidocs}
install -d $RPM_BUILD_ROOT%{_gidocdir}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/libportal-1 $RPM_BUILD_ROOT%{_gidocdir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	gtk3 -p /sbin/ldconfig
%postun	gtk3 -p /sbin/ldconfig

%post	gtk4 -p /sbin/ldconfig
%postun	gtk4 -p /sbin/ldconfig

%post	qt5 -p /sbin/ldconfig
%postun	qt5 -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_libdir}/libportal.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libportal.so.1
%{_libdir}/girepository-1.0/Xdp-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libportal.so
%{_includedir}/libportal
%{_datadir}/gir-1.0/Xdp-1.0.gir
%{_pkgconfigdir}/libportal.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libportal.a
%endif

%files -n vala-libportal
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/libportal.deps
%{_datadir}/vala/vapi/libportal.vapi

%if %{with gtk3}
%files gtk3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libportal-gtk3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libportal-gtk3.so.1
%{_libdir}/girepository-1.0/XdpGtk3-1.0.typelib

%files gtk3-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libportal-gtk3.so
%{_includedir}/libportal-gtk3
%{_datadir}/gir-1.0/XdpGtk3-1.0.gir
%{_pkgconfigdir}/libportal-gtk3.pc

%if %{with static_libs}
%files gtk3-static
%defattr(644,root,root,755)
%{_libdir}/libportal-gtk3.a
%endif

%files -n vala-libportal-gtk3
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/libportal-gtk3.deps
%{_datadir}/vala/vapi/libportal-gtk3.vapi
%endif

%if %{with gtk4}
%files gtk4
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libportal-gtk4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libportal-gtk4.so.1
%{_libdir}/girepository-1.0/XdpGtk4-1.0.typelib

%files gtk4-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libportal-gtk4.so
%{_includedir}/libportal-gtk4
%{_datadir}/gir-1.0/XdpGtk4-1.0.gir
%{_pkgconfigdir}/libportal-gtk4.pc

%if %{with static_libs}
%files gtk4-static
%defattr(644,root,root,755)
%{_libdir}/libportal-gtk4.a
%endif

%files -n vala-libportal-gtk4
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/libportal-gtk4.deps
%{_datadir}/vala/vapi/libportal-gtk4.vapi
%endif

%if %{with qt5}
%files qt5
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libportal-qt5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libportal-qt5.so.1

%files qt5-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libportal-qt5.so
%{_includedir}/libportal-qt5
%{_pkgconfigdir}/libportal-qt5.pc

%if %{with static_libs}
%files qt5-static
%defattr(644,root,root,755)
%{_libdir}/libportal-qt5.a
%endif
%endif

%if %{with qt6}
%files qt6
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libportal-qt6.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libportal-qt6.so.1

%files qt6-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libportal-qt6.so
%{_includedir}/libportal-qt6
%{_pkgconfigdir}/libportal-qt6.pc

%if %{with static_libs}
%files qt6-static
%defattr(644,root,root,755)
%{_libdir}/libportal-qt6.a
%endif
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gidocdir}/libportal-1
%endif
