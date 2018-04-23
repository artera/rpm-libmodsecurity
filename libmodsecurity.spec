
Name: libmodsecurity
Version: 3.0.2
Release: 1%{?dist}
Summary: A library that loads/interprets rules written in the ModSecurity SecRules

License: ASL 2.0
URL: https://www.modsecurity.org/

Source0: https://github.com/SpiderLabs/ModSecurity/releases/download/v%{version}/modsecurity-v%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: flex
BuildRequires: bison
BuildRequires: git-core
BuildRequires: ssdeep-devel
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(yajl)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(geoip)
BuildRequires: pkgconfig(libpcre)
BuildRequires: pkgconfig(lmdb)

# libinjection is supposed to be bundled (same as with mod_security 2.x)
# See: https://github.com/client9/libinjection#embedding
Provides: bundled(libinjection) = 3.9.2

%description
Libmodsecurity is one component of the ModSecurity v3 project.
The library codebase serves as an interface to ModSecurity Connectors
taking in web traffic and applying traditional ModSecurity processing.
In general, it provides the capability to load/interpret rules written
in the ModSecurity SecRules format and apply them to HTTP content provided
by your application via Connectors.


%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package static
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description static
The %{name}-static package contains static libraries for developing
applications that use %{name}.



%prep
%autosetup -n modsecurity-v%{version}


%build
%configure --libdir=%{_libdir} --with-lmdb
%make_build


%install
%make_install


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc README.md AUTHORS
%{_libdir}/*.so.*
%{_bindir}/*
%license LICENSE

%files devel
%doc README.md AUTHORS
%{_includedir}/*
%{_libdir}/*.so
%license LICENSE

%files static
%{_libdir}/*.a
%{_libdir}/*.la


%changelog
* Sat Apr 14 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 3.0.2-1
- Update to 3.0.2 (rhbz #1563219)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 21 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 3.0.0-1
- Update to 3.0.0 final release
- Drop upstreamed patch
- Add some new BRs

* Sun Oct 22 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 3.0.0-0.2.rc1
- Add a patch to fix the build on non-x86 arch

* Fri Sep 01 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 3.0.0-0.1.rc1
- Fix release tag

* Wed Aug 30 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 3.0.0-0.rc1
- Update to RC1
- Fix some spec issues

* Mon Feb 22 2016 Athmane Madjoudj <athmane@fedoraproject.org> 3.0-0.git
- Initial release

