#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mcelog
Version  : 137
Release  : 12
URL      : https://github.com/andikleen/mcelog/archive/v137.tar.gz
Source0  : https://github.com/andikleen/mcelog/archive/v137.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: mcelog-bin
Requires: mcelog-config
Requires: mcelog-doc
Patch1: memory.patch

%description
mcelog is the user space backend for logging machine check errors
reported by the hardware to the kernel. The kernel does the immediate
actions (like killing processes etc.) and mcelog decodes the errors
and manages various other advanced error responses like
offlining memory, CPUs or triggering events. In addition
mcelog also handles corrected errors, by logging and accounting them.

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
%setup -q -n mcelog-137
%patch1 -p1

%build
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install
## make_install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
cp mcelog.service %{buildroot}/usr/lib/systemd/system
ln -s ../mcelog.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mcelog

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/mcelog.service
/usr/lib/systemd/system/multi-user.target.wants/mcelog.service

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man5/*
%doc /usr/share/man/man8/*
