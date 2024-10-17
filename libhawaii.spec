%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Library shared among Hawaii Shell and other applications
Name:		libhawaii
Version:	0.8.0
Release:	1
Group:		Graphical desktop/Other
License:	LGPLv2+ and GPLv2+
URL:		https://hawaiios.org/
Source0:	https://github.com/hawaii-desktop/libhawaii/releases/download/v%{version}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5QuickTest)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	cmake(ECM)
Requires:	%{libname} = %{EVRD}

%track
prog %{name} = {
    url = http://downloads.sourceforge.net/project/mauios/hawaii/
    regex = "%{name}-(__VER__)\.tar\.gz"
    version = %{version}
}

%description
These are the libraries used by Hawaii Shell and other projects related
to the Hawaii desktop environment.

%package -n %{libname}
Summary:	Main package for %{name}
Group:		System/Libraries

%description -n %{libname}
Main library for %{name}.

%package -n %{develname}
Summary:	Development files for Hawaii library
Group:		Development/C++
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}

%description -n %{develname}
Development files and headers for %{name}.

%prep
%setup -q

%build
%cmake_qt5
%make

%install
%makeinstall_std -C build

%files
%dir %{_libdir}/qml/Hawaii/GSettings
%{_libdir}/qml/Hawaii/GSettings/*.so
%{_libdir}/qml/Hawaii/GSettings/plugins.qmltypes
%{_libdir}/qml/Hawaii/GSettings/qmldir

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc README.md
%dir %{_includedir}/Hawaii
%dir %{_includedir}/Hawaii/GSettings
%dir %{_includedir}/Hawaii/hawaii
%dir %{_includedir}/Hawaii/gsettings
%dir %{_libdir}/cmake/Hawaii
%{_includedir}/Hawaii/GSettings/QGSettings
%{_includedir}/Hawaii/gsettings/*.h
%{_includedir}/Hawaii/hawaii/*.h
%{_libdir}/*.so
%{_libdir}/cmake/Hawaii/*.cmake
%{_libdir}/cmake/Hawaii/*.in