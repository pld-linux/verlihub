#
# TODO: fix build:
#	"Sorry, cannot currently work without pthreads"
#
Summary:	DC Hub
Summary(pl):	Koncentrator DC
Name:		verlihub
%define		subver	b
Version:	0.9.8
Release:	0.%{subver}.1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/verlihub/%{name}-%{version}%{subver}.tar.gz
# Source0-md5:	f5a715af67d60c38cc1e57cb4265185b
URL:		http://verlihub.sf.net/
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

%description -l pl
VerliHub jest koncentratorem protoko�u Direct Connect. Dzia�a pi�knie
na linuksie, napisane jest w C++, charakteryzuje si� relatywnie niskim
zu�yciem procesora i pami�ci oraz wykorzystaniem u�ytecznych patent�w.
Dzia�a wsp�lnie z serwerem MySQL.

%package devel
Summary:	Header files for verlihub
Summary(pl):	Pliki nag��wkowe dla verlihub
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
Requires:	GeoIP-devel
Requires:	libstdc++-devel
Requires:	mysql-devel
Requires:	openssl-devel
Requires:	pcre-devel

%description devel
This package includes the header files for developing.

%description devel -l pl
Ten pakiet zawiera pliki nag��wkowe.

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
%setup -q -n %{name}-%{version}%{subver}

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
