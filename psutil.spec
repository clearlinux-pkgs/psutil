#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : psutil
Version  : 5.5.0
Release  : 59
URL      : https://files.pythonhosted.org/packages/6e/a0/833bcbcede5141cc5615e50c7cc5b960ce93d9c9b885fbe3b7d36e48a2d4/psutil-5.5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/6e/a0/833bcbcede5141cc5615e50c7cc5b960ce93d9c9b885fbe3b7d36e48a2d4/psutil-5.5.0.tar.gz
Summary  : Cross-platform lib for process and system monitoring in Python.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: psutil-license = %{version}-%{release}
Requires: psutil-python = %{version}-%{release}
Requires: psutil-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : procps-ng

%description
This directory contains scripts which are meant to be used internally
(benchmarks, CI automation, etc.).

%package license
Summary: license components for the psutil package.
Group: Default

%description license
license components for the psutil package.


%package python
Summary: python components for the psutil package.
Group: Default
Requires: psutil-python3 = %{version}-%{release}

%description python
python components for the psutil package.


%package python3
Summary: python3 components for the psutil package.
Group: Default
Requires: python3-core

%description python3
python3 components for the psutil package.


%prep
%setup -q -n psutil-5.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1548286121
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/psutil
cp LICENSE %{buildroot}/usr/share/package-licenses/psutil/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/psutil/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
