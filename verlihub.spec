Summary:	DC Hub
Summary(pl):	Koncentrator DC
Name:		verlihub
Version:	0.9.7
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/verlihub/%{name}-%{version}.tar.gz
# Source0-md5:	769dc0eb03e7ea082b543eb9c1a5f7e0
URL:		http://verlihub.sf.net/
BuildRequires:	GeoIP-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	mysql-devel
BuildRequires:	pcre-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VerliHub is a Direct Connect protocol server (Hub), runs on linux,
written in C++, relatively low CPU & RAM usage, and several useful
features. Uses MySQL database.

%description -l pl
VerliHub jest koncentratorem protoko³u Direct Connect. Dzia³a piêknie
na linuksie, napisane jest w C++, charakteryzuje siê relatywnie niskim
zu¿yciem procesora i pamiêci oraz wykorzystaniem u¿ytecznych patentów.
Dzia³a wspólnie z serwerem MySQL.

%package devel
Summary:	Header files for verlihub
Summary(pl):	Pliki nag³ówkowe dla verlihub
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description devel
This package includes the header files for developing.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe.

%package static
Summary:	Static verlihub librarys
Summary(pl):	Biblioteki statyczne verlihub
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static librarys for verlihub.

%description static -l pl
Ten pakiet zawiera statyczne biblioteki verlihub.

%prep
%setup -q

%build
%{__aclocal} 
%{__autoconf}
%{__automake}

%configure

%{__make} \
	LDFLAGS="-lGeoIP"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/verlihub

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -f scripts/{c*,in*,r*,s*,t*} $RPM_BUILD_ROOT%{_datadir}/verlihub

%clean
rm -rf $RPM_BUILD_ROOT
rm -f docs/Makefile*

%files 
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO docs/*
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/verlihub
%attr(755,root,root) %{_datadir}/verlihub/*
%{_libdir}/*.la
%{_libdir}/*.0*
%{_libdir}/libverlihub
%{_libdir}/libvhapi

%files devel
%defattr(644,root,root,755)
%{_includedir}/verlihub/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
