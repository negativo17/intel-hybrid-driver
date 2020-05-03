Name:           intel-hybrid-driver
Epoch:          1
Version:        1.0.2
Release:        1%{?dist}
Summary:        VA driver for Intel G45 & HD Graphics family
License:        MIT and BSD and NTP
URL:            https://01.org/linuxmedia/vaapi

Source0:        https://github.com/intel/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# https://github.com/intel/intel-hybrid-driver/pull/26
# https://github.com/intel/intel-hybrid-driver/commit/dfa9c8eba29573e24f73b1890f8a67f0e46e3d7b
Patch0:         %{name}-libva-2.patch
Patch1:         %{name}-configure.patch
Patch2:         https://patch-diff.githubusercontent.com/raw/intel/intel-hybrid-driver/pull/28.patch#/%{name}-gcc10.patch

BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig(libdrm) >= 2.4.45
BuildRequires:  pkgconfig(libva) >= 1.0.0
BuildRequires:  pkgconfig(libcmrt) >= 0.10.0
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(wayland-server)

Obsoletes:      libva-intel-hybrid-driver < %{epoch}:%{version}-%{release}
Provides:       libva-intel-hybrid-driver = %{epoch}:%{version}-%{release}

%description
VA-API implementation for Intel G45 chipsets and Intel HD Graphics for Intel
Core processor family.

 Supported Platforms	Features
 Haswell       (HSW)	vp8enc
 Bay Trail M   (BYT)	vp8enc
 Broadwell     (BRW)	vp9dec vp9enc
 Braswell      (BSW)	vp8enc vp9dec

%prep
%autosetup -p1

%build
autoreconf -vif
%configure \
  --enable-drm \
  --enable-x11 \
  --enable-wayland

%make_build

%install
%make_install 
find %{buildroot} -name "*.la" -delete

%files
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/dri/hybrid_drv_video.so

%changelog
* Sun May 03 2020 Simone Caronni <negativo17@gmail.com> - 1:1.0.2-1
- First build.
