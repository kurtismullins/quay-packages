# Created by pyp2rpm-3.3.4
%global pypi_name flask
%global srcname flask

Name:           %{srcname}
Version:        1.1.2
Release:        1%{?dist}
Summary:        A simple framework for building complex web applications

License:        BSD-3-Clause
URL:            https://palletsprojects.com/p/flask/
Source0:        Flask-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(click) >= 5.1
BuildRequires:  python3dist(coverage)
BuildRequires:  python3dist(itsdangerous) >= 0.24
BuildRequires:  python3dist(jinja2) >= 2.10.1
BuildRequires:  python3dist(pallets-sphinx-themes)
BuildRequires:  python3dist(pallets-sphinx-themes)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(python-dotenv)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-issues)
BuildRequires:  python3dist(sphinx-issues)
BuildRequires:  python3dist(sphinxcontrib-log-cabinet)
BuildRequires:  python3dist(sphinxcontrib-log-cabinet)
BuildRequires:  python3dist(tox)
BuildRequires:  python3dist(werkzeug) >= 0.15
BuildRequires:  python3dist(sphinx)

%description
Flask is a lightweight WSGI_ web application framework. It is designed to make
getting started quick and easy, with the ability to scale up to complex
applications. It began as a simple wrapper around Werkzeug_ and Jinja_ and has
become one of the most popular Python web application frameworks.Flask offers
suggestions, but doesn't enforce any dependencies or project layout. It is up
to the...

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

Requires:       python3dist(click) >= 5.1
Requires:       python3dist(itsdangerous) >= 0.24
Requires:       python3dist(jinja2) >= 2.10.1
Requires:       python3dist(pallets-sphinx-themes)
Requires:       python3dist(python-dotenv)
Requires:       python3dist(setuptools)
Requires:       python3dist(sphinx)
Requires:       python3dist(sphinx-issues)
Requires:       python3dist(sphinxcontrib-log-cabinet)
Requires:       python3dist(werkzeug) >= 0.15
%description -n python3-%{srcname}
Flask is a lightweight WSGI_ web application framework. It is designed to make
getting started quick and easy, with the ability to scale up to complex
applications. It began as a simple wrapper around Werkzeug_ and Jinja_ and has
become one of the most popular Python web application frameworks.Flask offers
suggestions, but doesn't enforce any dependencies or project layout. It is up
to the...

%package -n %{srcname}-doc
Summary:        flask documentation
%description -n %{srcname}-doc
Documentation for flask

%prep
%autosetup -n Flask-%{version}
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
%license LICENSE.rst artwork/LICENSE.rst docs/license.rst examples/javascript/LICENSE examples/tutorial/LICENSE
%doc README.rst examples/javascript/README.rst examples/tutorial/README.rst
%{_bindir}/flask
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%files -n %{srcname}-doc
%doc html
%license LICENSE.rst artwork/LICENSE.rst docs/license.rst examples/javascript/LICENSE examples/tutorial/LICENSE

%changelog
* Thu May 28 2020 Kurtis Mullins <kmullins@redhat.com> - 1.1.2-1
- Initial package.
