#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : psutil
Version  : 4.4.1
Release  : 22
URL      : http://pypi.debian.net/psutil/psutil-4.4.1.tar.gz
Source0  : http://pypi.debian.net/psutil/psutil-4.4.1.tar.gz
Summary  : psutil is a cross-platform library for retrieving information onrunning processes and system utilization (CPU, memory, disks, network)in Python.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: psutil-python
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
This directory contains support scripts for Travis and Appveyor continuous
integration services.
Travis is used to run tests on Linux and OSX, Appveyor runs tests on Windows.

%package python
Summary: python components for the psutil package.
Group: Default

%description python
python components for the psutil package.


%prep
%setup -q -n psutil-4.4.1

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
