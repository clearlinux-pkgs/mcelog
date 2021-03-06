#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mcelog
Version  : 177
Release  : 56
URL      : https://github.com/andikleen/mcelog/archive/v177/mcelog-177.tar.gz
Source0  : https://github.com/andikleen/mcelog/archive/v177/mcelog-177.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: mcelog-autostart = %{version}-%{release}
Requires: mcelog-bin = %{version}-%{release}
Requires: mcelog-data = %{version}-%{release}
Requires: mcelog-license = %{version}-%{release}
Requires: mcelog-man = %{version}-%{release}
Requires: mcelog-services = %{version}-%{release}
Patch1: memory.patch
Patch2: 0001-Send-telemetry-record-on-MCE.patch

%description
mcelog used to do released, but now switched to a rolling release
scheme. That means the git tree is always kept stable and can
be used directly in production.

%package autostart
Summary: autostart components for the mcelog package.
Group: Default

%description autostart
autostart components for the mcelog package.


%package bin
Summary: bin components for the mcelog package.
Group: Binaries
Requires: mcelog-data = %{version}-%{release}
Requires: mcelog-license = %{version}-%{release}
Requires: mcelog-services = %{version}-%{release}

%description bin
bin components for the mcelog package.


%package data
Summary: data components for the mcelog package.
Group: Data

%description data
data components for the mcelog package.


%package license
Summary: license components for the mcelog package.
Group: Default

%description license
license components for the mcelog package.


%package man
Summary: man components for the mcelog package.
Group: Default

%description man
man components for the mcelog package.


%package services
Summary: services components for the mcelog package.
Group: Systemd services

%description services
services components for the mcelog package.


%prep
%setup -q -n mcelog-177
cd %{_builddir}/mcelog-177
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1625669024
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1625669024
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mcelog
cp %{_builddir}/mcelog-177/LICENSE %{buildroot}/usr/share/package-licenses/mcelog/4cc77b90af91e615a64ae04893fdffa7939db84c
%make_install
## install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
cp mcelog.service %{buildroot}/usr/lib/systemd/system
ln -s ../mcelog.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants

mkdir -p %{buildroot}/usr/share/clr-service-restart
ln -sf /usr/lib/systemd/system/mcelog.service %{buildroot}/usr/share/clr-service-restart/mcelog.service
## install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/mcelog.service

%files bin
%defattr(-,root,root,-)
/usr/bin/mcelog

%files data
%defattr(-,root,root,-)
/usr/share/clr-service-restart/mcelog.service

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mcelog/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/mcelog.conf.5
/usr/share/man/man5/mcelog.triggers.5
/usr/share/man/man8/mcelog.8

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/mcelog.service
/usr/lib/systemd/system/mcelog.service
