%global _commit 02002c9068d2a824bafa8168fcf0c5a4be3aebf5
%global _shortcommit %(c=%{_commit}; echo ${c:0:7})

Name:           dtksettings
Version:        0.1.3
Release:        1.git%{_shortcommit}%{?dist}
Summary:        DtkSettings is a powerfull tool to generation config form json
License:        GPLv3
URL:            https://github.com/linuxdeepin/dtksettings
Source0:        %{url}/archive/%{_commit}/%{name}-%{_shortcommit}.tar.gz
BuildRequires:  qt5-qtbase-devel

%description
DtkSettings is a powerfull tool to generation config form json.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}

%prep
%setup -q -n %{name}-%{_commit}

%build
%qmake_qt5 PREFIX=%{_prefix} LIB_INSTALL_DIR=%{_libdir}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc README.md
%{_bindir}/dtk-settings-tool
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/libdtk-*/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib*.so

%changelog
* Tue Mar  7 2017 mosquito <sensor.wen@gmail.com> - 0.1.3-1.git02002c9
- Update to 0.1.3
* Sun Feb 26 2017 mosquito <sensor.wen@gmail.com> - 0.1.2-1.git13efd5f
- Initial build
