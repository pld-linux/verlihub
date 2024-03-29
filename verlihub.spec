%define		subver	d-RC2
Summary:	DC Hub
Summary(pl.UTF-8):	Koncentrator DC
Name:		verlihub
Version:	0.9.8
Release:	0.%{subver}.4
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/verlihub/%{name}-%{version}%{subver}.tar.gz
# Source0-md5:	0824be2cf3af08ccda1638c5d5d0bc4e
URL:		http://www.verlihub-project.org/doku.php
BuildRequires:	GeoIP-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	mysql-devel
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VerliHub is a Direct Connect protocol server (Hub), runs on linux,
written in C++, relatively low CPU & RAM usage, and several useful
features. Uses MySQL database.

%description -l pl.UTF-8
VerliHub jest koncentratorem protokołu Direct Connect. Działa pięknie
na linuksie, napisane jest w C++, charakteryzuje się relatywnie niskim
zużyciem procesora i pamięci oraz wykorzystaniem użytecznych patentów.
Działa wspólnie z serwerem MySQL.

%package devel
Summary:	Header files for verlihub
Summary(pl.UTF-8):	Pliki nagłówkowe dla verlihub
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
Requires:	GeoIP-devel
Requires:	libstdc++-devel
Requires:	mysql-devel
Requires:	openssl-devel
Requires:	pcre-devel

%description devel
This package includes the header files for developing.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe.

%package static
Summary:	Static verlihub librarys
Summary(pl.UTF-8):	Biblioteki statyczne verlihub
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static librarys for verlihub.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczne biblioteki verlihub.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/verlihub

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -f scripts/{c*,im*,v*} $RPM_BUILD_ROOT%{_datadir}/verlihub

# remove makefile from docs
rm -f docs/Makefile*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO docs/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_datadir}/verlihub
%attr(755,root,root) %{_datadir}/verlihub/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/verlihub/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
