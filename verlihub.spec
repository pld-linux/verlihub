Summary:	DC Hub
Summary(pl):	Koncentrator DC
Name:		verlihub
Version:	0.9.6
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/verlihub/%{name}-%{version}.tar.gz
# Source0-md5:	c3c90d34e76bcdd299d105829d22c330
URL:		http://verlihub.sf.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	GeoIP-devel
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

%prep
%setup -q

%build
%{__aclocal} 
%{__autoconf}
%{__automake}

%configure

%{__make} LDFLAGS=-lGeoIP

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/verlihub}

install src/verlihub $RPM_BUILD_ROOT%{_bindir}

mv -f scripts/def_config docs
cp -f scripts/* $RPM_BUILD_ROOT%{_datadir}/verlihub

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc ChangeLog README TODO docs/*
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/verlihub/*
%attr(755,root,root) %{_datadir}/verlihub/*
