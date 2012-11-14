Summary:	Library for decoding .opus files, including seeking support
Summary(pl.UTF-8):	Biblioteka do dekodowania plików .opus wraz z obsługą przewijania
Name:		opusfile
Version:	0.2
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://downloads.xiph.org/releases/opus/%{name}-%{version}.tar.gz
# Source0-md5:	454375f51fb2f84bef9bf2fbf9535bb1
URL:		http://opus-codec.org/
BuildRequires:	libogg-devel >= 1:1.3
BuildRequires:	openssl-devel
BuildRequires:	opus-devel >= 1.0.1
BuildRequires:	pkgconfig
Requires:	libogg >= 1:1.3
Requires:	opus >= 1.0.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for decoding .opus files, including seeking support.

%description -l pl.UTF-8
Biblioteka do dekodowania plików .opus wraz z obsługą przewijania.

%package devel
Summary:	Header files for opusfile library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki opusfile
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libogg-devel >= 1:1.3
Requires:	openssl-devel
Requires:	opus-devel >= 1.0.1

%description devel
Header files for opusfile library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki opusfile.

%package static
Summary:	Static opusfile library
Summary(pl.UTF-8):	Statyczna biblioteka opusfile
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static opusfile library.

%description static -l pl.UTF-8
Statyczna biblioteka opusfile.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/opusfile

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README.txt
%attr(755,root,root) %{_libdir}/libopusfile.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libopusfile.so.0

%files devel
%defattr(644,root,root,755)
%doc doc/html/*
%attr(755,root,root) %{_libdir}/libopusfile.so
%{_libdir}/libopusfile.la
%{_includedir}/opus/opusfile.h
%{_pkgconfigdir}/opusfile.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libopusfile.a
