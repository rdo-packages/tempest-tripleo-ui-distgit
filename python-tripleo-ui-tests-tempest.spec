# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility
%global service tripleo-ui
%global plugin tempest-tripleo-ui
%global module tempest_tripleo_ui
%global common_desc \
The tempest plugin for TripleO UI

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           python-%{service}-tests-tempest
Version:        XXX
Release:        XXX
Summary:        The tempest plugin for TripleO UI
License:        ASL 2.0
URL:            https://git.openstack.org/cgit/openstack/%{plugin}/
Source0:        https://tarballs.openstack.org/%{plugin}/%{plugin}-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  git
BuildRequires:  openstack-macros

Requires:   python%{pyver}-oslo-config >= 2:5.1.0
Requires:   python%{pyver}-pbr >= 3.1.1
Requires:   python%{pyver}-selenium >= 3.14.1
Requires:   python%{pyver}-six => 1.10.0
Requires:   python%{pyver}-tempest >= 1:17.1.0

%description
%{common_desc}

%package -n python%{pyver}-%{service}-tests-tempest

%prep
%autosetup -n %{plugin}-%{upstream_version} -S git

# Let's handle dependencies ourseleves
%py_req_cleanup
# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
%{pyver_build}

%install
%{pyver_install}

%files -n python%{pyver}-%{service}-tests-tempest
%license LICENSE
%doc README.rst
%{pyver_sitelib}/%{module}
%{pyver_sitelib}/*.egg-info

%changelog
* Wed Jan 23 2019 Honza Pokorny <honza@redhat.com> 0.0.1
- First RPM
