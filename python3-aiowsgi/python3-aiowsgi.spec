# Created by pyp2rpm-3.3.3
%global pypi_name aiowsgi
%global srcname aiowsgi

Name:           %{srcname}
Version:        0.7
Release:        1%{?dist}
Summary:        minimalist wsgi server using asyncio

License:        MIT
URL:            https://github.com/gawel/aiowsgi/
Source0:        aiowsgi-0.7.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(asyncio)
BuildRequires:  python3dist(coverage)
BuildRequires:  python3dist(coveralls)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(waitress)
BuildRequires:  python3dist(webob)
BuildRequires:  python3dist(webtest)
BuildRequires:  python3dist(wsgiproxy2)
BuildRequires:  python3dist(sphinx)

%description
 aiowsgi - minimalist wsgi server using asyncio Require python 2.7, 3.3+Source:

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

Requires:       python3dist(asyncio)
Requires:       python3dist(coverage)
Requires:       python3dist(coveralls)
Requires:       python3dist(mock)
Requires:       python3dist(pytest)
Requires:       python3dist(waitress)
Requires:       python3dist(webob)
Requires:       python3dist(webtest)
Requires:       python3dist(wsgiproxy2)
%description -n python3-%{srcname}
 aiowsgi - minimalist wsgi server using asyncio Require python 2.7, 3.3+Source:

%package -n %{srcname}-doc
Summary:        aiowsgi documentation
%description -n %{srcname}-doc
Documentation for aiowsgi

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%files -n %{srcname}-doc
%doc html
%license LICENSE

%changelog
* Thu Feb 06 2020 Tom McKay <thomasmckay@redhat.com> - 0.7-1
- Initial package.
