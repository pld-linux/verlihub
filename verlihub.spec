Summary:	DC Hub
Summary(pl):	Koncentrator DC
Name:		verlihub
Version:	0.9.4a
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/verlihub/%{name}-%{version}.tar.gz
# Source0-md5:	f25b6157cc8eec3ca393b2744158b3ea
URL:		http://verlihub.sf.net/
BuildRequires:	autoconf
BuildRequires:	automake
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

%prep
%setup -q

%build
%{__aclocal} 
%{__autoconf}
%{__automake}

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install src/verlihub $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
