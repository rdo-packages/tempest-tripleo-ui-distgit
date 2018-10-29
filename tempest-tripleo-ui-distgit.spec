%global plugin tempest-tripleo-ui
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           python-tempest-tripleo-ui
Version:        master
Release:        2%{?dist}
Summary:        The tempest plugin for TripleO UI
License:        ASL 2.0
URL:            http://tripleo.org
Source0: https://tarballs.openstack.org/%{plugin}/%{plugin}-%{upstream_version}.tar.gz

BuildArch:      noarch

%description

%prep

%build

%install

%files
%license LICENSE
%doc README.md

%postun

%changelog
* Fri Oct 5 2018 Honza Pokorny <honza@redhat.com> 0.0.1
- First RPM
