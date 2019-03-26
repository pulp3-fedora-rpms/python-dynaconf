# Created by pyp2rpm-3.3.2
%global pypi_name dynaconf

Name:           python-%{pypi_name}
Version:        1.2.1
Release:        1%{?dist}
Summary:        The dynamic configurator for your Python Project

License:        MIT
URL:            https://github.com/rochacbruno/dynaconf
# Docs are missing from pypi
Source0:        https://github.com/rochacbruno/%{pypi_name}/archive/%{version}.tar.gz
Patch1:         0001-Remove-prior-versions-of-aafig.py-that-are-Python3-i.patch
Patch2:         0002-aafig.py-Fix-for-recent-docutils-version.patch
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(codecov)
BuildRequires:  python3dist(configobj)
BuildRequires:  python3dist(configobj)
BuildRequires:  python3dist(configobj)
BuildRequires:  python3dist(flake8)
BuildRequires:  python3dist(flake8-debugger)
BuildRequires:  python3dist(flake8-print)
BuildRequires:  python3dist(flake8-todo)
BuildRequires:  python3dist(flask) >= 0.12
BuildRequires:  python3dist(hvac)
BuildRequires:  python3dist(hvac)
BuildRequires:  python3dist(pep8-naming)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  python3dist(python-box)
BuildRequires:  python3dist(python-dotenv)
BuildRequires:  python3dist(python-dotenv)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(radon)
BuildRequires:  python3dist(redis)
BuildRequires:  python3dist(redis)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools) >= 38.6.0
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(toml)
BuildRequires:  python3dist(toml)
BuildRequires:  python3dist(toml)
BuildRequires:  python3dist(sphinx)
# For docs
Buildrequires:  python3dist(aafigure)
Buildrequires:  python3dist(django)
Buildrequires:  python3dist(recommonmark)
# For tests
Buildrequires:  python3dist(tox)
# For tests as well. See requirements_dev.txt
Buildrequires:  python3dist(codecov)
Buildrequires:  python3dist(pytest-cov)
Buildrequires:  python3dist(pytest-xdist)
Buildrequires:  python3dist(logzero)

%description
[![Dynaconf]( **dynaconf** - The **dyna**mic **conf**igurator for your Python
Project[![MIT License]( [![PyPI]( [![PyPI]( [![Travis CI]( [![codecov](
[![Codacy Badge](

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(click)
Requires:       python3dist(configobj)
Requires:       python3dist(configobj)
Requires:       python3dist(configobj)
Requires:       python3dist(hvac)
Requires:       python3dist(hvac)
Requires:       python3dist(python-box)
Requires:       python3dist(python-dotenv)
Requires:       python3dist(pyyaml)
Requires:       python3dist(pyyaml)
Requires:       python3dist(redis)
Requires:       python3dist(redis)
Requires:       python3dist(setuptools)
Requires:       python3dist(six)
Requires:       python3dist(toml)
Requires:       python3dist(toml)
%description -n python3-%{pypi_name}
[![Dynaconf]( **dynaconf** - The **dyna**mic **conf**igurator for your Python
Project[![MIT License]( [![PyPI]( [![PyPI]( [![Travis CI]( [![codecov](
[![Codacy Badge](

%package -n python-%{pypi_name}-doc
Summary:        dynaconf documentation
%description -n python-%{pypi_name}-doc
Documentation for dynaconf

%prep
%autosetup -S git -n %{pypi_name}-%{version}
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
tox -e py%{python3_version_nodots}

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/dynaconf
%{python3_sitelib}/docs
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Thu Mar 21 2019 Mike DePaulo <mikedep333@redhat.com> - 1.2.1-1
- Initial package.
