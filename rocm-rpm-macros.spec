Name:           rocm-rpm-macros
Version:        5.7.0
Release:        1%{dist}
Summary:        ROCm RPM macros
License:        GPLv2

URL:            https://fedoraproject.org/
Source0:        GPL
Source1:        macros.rocm

Requires:       environment-modules
BuildArch:      noarch
%description
This package contains ROCm RPM macros for building ROCm packages.

%prep
%setup -cT
install -pm 644 %{SOURCE0} .

%install
install -Dpm 644 %{SOURCE1} %{buildroot}%{_rpmmacrodir}/macros.rocm

%files
%license GPL
%{_rpmmacrodir}/macros.rocm

%changelog
* Sun Oct 8 2023 Tom Rix <trix@redhat.com> 5.7.0
- Initial package
