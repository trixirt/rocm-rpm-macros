Name:           rocm-modules
Version:        1.0
Release:        1%{dist}
Summary:        ROCm enviroment modules
License:        GPLv2

URL:            https://fedoraproject.org/
Source0:        GPL
Source1:        modules.rocm

BuildArch:      noarch

Requires:       environment(modules)

%description
This package contains ROCm environment modules for switching
between different GPU families.

%prep
%setup -cT
install -pm 644 %{SOURCE0} .

%install
mkdir -p %{buildroot}%{_datadir}/modulefiles/rocm/
cp -p %{SOURCE1}/* %{buildroot}%{_datadir}/modulefiles/rocm/

%files
%license GPL
%{_datadir}/modulefiles/rocm/

%changelog
* Sun Oct 8 2023 Tom Rix <trix@redhat.com> - 1.0-1
- Initial package
