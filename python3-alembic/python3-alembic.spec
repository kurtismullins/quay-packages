# Created by pyp2rpm-3.3.3
%global pypi_name alembic
%global srcname alembic

Name:           %{srcname}
Version:        1.3.3
Release:        1%{?dist}
Summary:        A database migration tool for SQLAlchemy

License:        MIT
URL:            https://alembic.sqlalchemy.org
Source0:        alembic-1.3.3.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(mako)
BuildRequires:  python3dist(python-dateutil)
BuildRequires:  python3dist(python-editor) >= 0.3
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sqlalchemy) >= 1.1.0
BuildRequires:  python3dist(sphinx)

%description
Alembic is a database migrations tool written by the author of SQLAlchemy <>_.
A migrations tool offers the following functionality:* Can emit ALTER
statements to a database in order to change the structure of tables and other
constructs * Provides a system whereby "migration scripts" may be constructed;
each script indicates a particular series of steps that can "upgrade" a target
database to...

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

Requires:       python3dist(mako)
Requires:       python3dist(python-dateutil)
Requires:       python3dist(python-editor) >= 0.3
Requires:       python3dist(setuptools)
Requires:       python3dist(sqlalchemy) >= 1.1.0
%description -n python3-%{srcname}
Alembic is a database migrations tool written by the author of SQLAlchemy <>_.
A migrations tool offers the following functionality:* Can emit ALTER
statements to a database in order to change the structure of tables and other
constructs * Provides a system whereby "migration scripts" may be constructed;
each script indicates a particular series of steps that can "upgrade" a target
database to...

%package -n %{srcname}-doc
Summary:        alembic documentation
%description -n %{srcname}-doc
Documentation for alembic

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs/build html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst README.unittests.rst docs/build/unreleased/README.txt
%{_bindir}/alembic
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%files -n %{srcname}-doc
%doc html
%license LICENSE

%changelog
* Mon Mar 02 2020 Tom McKay <thomasmckay@redhat.com> - 1.3.3-1
- Initial package.
