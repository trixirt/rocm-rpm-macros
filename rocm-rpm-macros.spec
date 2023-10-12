%global commit0 4f5cabb4e32139fb954811414c7afca65e840579
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           rocm-rpm-macros
Version:        1.0
Release:        2%{dist}
Summary:        ROCm RPM macros
License:        GPLv2

URL:            https://github.com/trixirt/rocm-rpm-macros
Source0:        %{url}/archive/%{commit0}/rocm-rpm-macros-%{shortcommit0}.tar.gz

Requires:       environment-modules
BuildArch:      noarch
%description
This package contains ROCm RPM macros for building ROCm packages.

%package modules
Summary: ROCm enviroment modules
Requires: environment(modules)

%description modules
This package contains ROCm environment modules for switching
between different GPU families.

%prep
%autosetup -p1 -n rocm-rpm-macros-%{commit0}

%install
mkdir -p %{buildroot}%{_rpmmacrodir}/
install -Dpm 644 macros.rocm %{buildroot}%{_rpmmacrodir}/
mkdir -p %{buildroot}%{_datadir}/modulefiles/rocm/
cp -p modules.rocm/* %{buildroot}%{_datadir}/modulefiles/rocm/

%files
%license GPL
%{_rpmmacrodir}/macros.rocm

%files modules
%license GPL
%{_datadir}/modulefiles/rocm/

%changelog
* Thu Oct 12 2023 Tom Rix <trix@redhat.com> 1.0-2
- Remove version for macros
- Combine modules as a subpackage

* Sun Oct 8 2023 Tom Rix <trix@redhat.com> 5.7.0-1
- Initial package
