#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : psutil
Version  : 5.3.1
Release  : 34
URL      : http://pypi.debian.net/psutil/psutil-5.3.1.tar.gz
Source0  : http://pypi.debian.net/psutil/psutil-5.3.1.tar.gz
Summary  : Cross-platform lib for process and system monitoring in Python.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: psutil-legacypython
Requires: psutil-python3
Requires: psutil-python
Requires: enum34
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
This directory contains scripts which are meant to be used internally
(benchmarks, CI automation, etc.).

%package legacypython
Summary: legacypython components for the psutil package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the psutil package.


%package python
Summary: python components for the psutil package.
Group: Default
Requires: psutil-legacypython
Requires: psutil-python3

%description python
python components for the psutil package.


%package python3
Summary: python3 components for the psutil package.
Group: Default
Requires: python3-core

%description python3
python3 components for the psutil package.


%prep
%setup -q -n psutil-5.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507164627
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test || :
%install
export SOURCE_DATE_EPOCH=1507164627
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
