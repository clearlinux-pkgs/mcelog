#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mcelog
Version  : 149
Release  : 25
URL      : https://github.com/andikleen/mcelog/archive/v149.tar.gz
Source0  : https://github.com/andikleen/mcelog/archive/v149.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: mcelog-bin
Requires: mcelog-config
Requires: mcelog-autostart
Requires: mcelog-doc
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
Requires: mcelog-config

%description bin
bin components for the mcelog package.


%package config
Summary: config components for the mcelog package.
Group: Default

%description config
config components for the mcelog package.


%package doc
Summary: doc components for the mcelog package.
Group: Documentation

%description doc
doc components for the mcelog package.


%prep
%setup -q -n mcelog-149
%patch1 -p1
%patch2 -p1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1490649903
export CFLAGS="$CFLAGS -Os -ffunction-sections "
export FCFLAGS="$CFLAGS -Os -ffunction-sections "
export FFLAGS="$CFLAGS -Os -ffunction-sections "
export CXXFLAGS="$CXXFLAGS -Os -ffunction-sections "
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1490649903
rm -rf %{buildroot}
%make_install
## make_install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
cp mcelog.service %{buildroot}/usr/lib/systemd/system
ln -s ../mcelog.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
## make_install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/mcelog.service

%files bin
%defattr(-,root,root,-)
/usr/bin/mcelog

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/mcelog.service
/usr/lib/systemd/system/mcelog.service

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man5/*
%doc /usr/share/man/man8/*
