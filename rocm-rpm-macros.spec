Name:           rocm-rpm-macros
Version:        5.7.0
Release:        1%{dist}
Summary:        ROCm RPM macros
License:        GPLv2

URL:            https://fedoraproject.org/
Source0:        macros.rocm
Source1:        GPL

BuildArch:      noarch
%description
This package contains ROCm RPM macros for building ROCm packages.

%prep
%setup -cT
install -pm 644 %{SOURCE1} .

%install
install -Dpm 644 %{SOURCE0} %{buildroot}%{_rpmmacrodir}/macros.rocm

%files
%license GPL
%{_rpmmacrodir}/macros.rocm

%changelog
* Fri Oct 6 2023 Tom Rix <trix@redhat.com> 40-1
- Initial package
