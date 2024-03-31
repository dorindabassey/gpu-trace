Name:           gpu-trace
Version:        2.12
Release:        1%{?dist}
Summary:        Simple script to collect GPU traces

License:        MIT
URL:            https://github.com/lostgoat/gpu-trace
Source0:        https://github.com/lostgoat/%{name}/archive/refs/tags/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  gcc  systemd-rpm-macros

%description
gpu-trace is a tool intended to aid the collection process of gpuvis traces.
It can run either as a daemon or standalone fashion.

%prep
%autosetup


%build

%install
mkdir -p %{buildroot}%{_bindir}
export INSTALL_ROOT=%{buildroot}
export INSTALL_PREFIX=%{_prefix}
export SYSTEMD_SERVICE_PATH=/usr/lib/systemd
%make_install


%files
%license LICENSE
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%doc README.md


%changelog
* Fri Jan 14 2022 Dorinda Bassey <dbassey@redhat.com> - 2.7-1
- Initial Packaged Version
