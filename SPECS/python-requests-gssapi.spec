%global sname requests-gssapi
%global s_name requests_gssapi

Name:           python-%{sname}
Version:        1.2.3
Release:        3%{?dist}
Summary:        A GSSAPI/SPNEGO authentication handler for python-requests

License:        ISC
URL:            https://github.com/pythongssapi/%{sname}
Source0:        https://github.com/pythongssapi/%{sname}/releases/download/v%{version}/%{sname}-%{version}.tar.gz
BuildArch:      noarch

# Patches

BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3-gssapi
BuildRequires:  python3-requests
BuildRequires:  python3-setuptools

%global _description\
Requests is an HTTP library, written in Python, for human beings. This\
library adds optional GSSAPI authentication support and supports\
mutual authentication. It includes a fully backward-compatible shim\
for requests-kerberos.

%description %_description

%package -n python3-%{sname}
Summary:        %summary
Requires:       python3-gssapi
Requires:       python3-requests
%{?python_provide:%python_provide python3-%{sname}}
%description -n python3-%{sname} %_description

%prep
%autosetup -S git_am -n %{sname}-%{version}

%build

%py3_build

%install
%py3_install

%check
%{__python3} -m unittest

%files -n python3-%{sname}
%doc README.rst AUTHORS HISTORY.rst
%license LICENSE
%{python3_sitelib}/%{s_name}*


%changelog
* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 1.2.3-3
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1.2.3-2
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Mon Feb 08 2021 Robbie Harwood <rharwood@redhat.com> - 1.2.3-1
- New upstream release (1.2.3)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 07 2020 Robbie Harwood <rharwood@redhat.com> - 1.2.2-1
- New upstream release (1.2.2)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-2
- Rebuilt for Python 3.9

* Tue Mar 31 2020 Robbie Harwood <rharwood@redhat.com> - 1.2.1-1
- New upstream release (1.2.1)

* Tue Feb 18 2020 Robbie Harwood <rharwood@redhat.com> - 1.2.0-1
- New upstream release (1.2.0)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 21 2019 Robbie Harwood <rharwood@redhat.com> - 1.1.0-1
- New upstream release (1.1.0)

* Thu Apr 11 2019 Robbie Harwood <rharwood@redhat.com> - 1.0.1-1
- New upstream release (1.0.1)
- Resolves: #1698650

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 17 2018 Robbie Harwood <rharwood@redhat.com> - 1.0.0-5
- Drop python2 subpackage
- Resolves: #1629796

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 19 2017 Robbie Harwood <rharwood@redhat.com> - 1.0.0-1
- New upstream release (v1.0.0)
