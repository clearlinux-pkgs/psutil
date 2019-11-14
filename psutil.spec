#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : psutil
Version  : 5.6.5
Release  : 69
URL      : https://files.pythonhosted.org/packages/03/9a/95c4b3d0424426e5fd94b5302ff74cea44d5d4f53466e1228ac8e73e14b4/psutil-5.6.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/03/9a/95c4b3d0424426e5fd94b5302ff74cea44d5d4f53466e1228ac8e73e14b4/psutil-5.6.5.tar.gz
Summary  : Cross-platform lib for process and system monitoring in Python.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: psutil-license = %{version}-%{release}
Requires: psutil-python = %{version}-%{release}
Requires: psutil-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : procps-ng
BuildRequires : python3-dev
BuildRequires : util-linux
Patch1: CVE-2019-18874.patch

%description
|  |version| |py-versions| |packages| |license|
        |  |travis| |appveyor| |doc| |twitter| |tidelift|

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
%setup -q -n psutil-5.6.5
cd %{_builddir}/psutil-5.6.5
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1573757257
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/psutil
cp %{_builddir}/psutil-5.6.5/LICENSE %{buildroot}/usr/share/package-licenses/psutil/51ede753f5d20b28226ab01c133ad67797eaf716
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/psutil/51ede753f5d20b28226ab01c133ad67797eaf716

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
