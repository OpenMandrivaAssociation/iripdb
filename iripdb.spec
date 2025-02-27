%define name iripdb
%define version 0.1.1
%define release  %mkrel 6

Summary: Generator of DB files necessary for the iRiver iHP-1xx series
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Patch0: iripdb-0.1.1-link.patch
License: GPL
Group: Sound
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Url: https://www.marevalo.net/iRipDB/
BuildRequires: libid3lib3.8-devel
BuildRequires: libvorbis-devel
BuildRequires: libogg-devel

%description
RipDB allows generating the DB files necessary for the iRiver iHP-1xx series of
MP3/Ogg HD Player on Linux and Windows. That will allow you to navigate your
files through the artist/album/genre menus. It supports adding MP3 and Ogg
files at this point. It's released under the GNU's General Public License and,
at this moment only in source code form.

%prep
%setup -q
%patch0 -p0

%build
%make all CC="gcc %{optflags} %{ldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -m 755 -D iripdb $RPM_BUILD_ROOT%{_bindir}/iripdb

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS Changelog COPYING README doc/*
%{_bindir}/iripdb

