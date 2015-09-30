%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Library shared among Hawaii Shell and other applications
Name:		libhawaii
Version:	0.5.90
Release:	1
Group:		Graphical desktop/Other
License:	LGPLv2+ and GPLv2+
URL:		http://www.maui-project.org
Source0:	http://downloads.sourceforge.net/mauios/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
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
%{_libdir}/hawaii

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc AUTHORS README.md
%{_libdir}/*.so
%{_includedir}/hawaii
%{_libdir}/cmake/*
