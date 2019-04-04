#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x89EFD588E975D6DF (rbtcollins@hp.com)
#
Name     : deprecated-unittest2
Version  : 1.1.0
Release  : 61
URL      : http://pypi.debian.net/unittest2/unittest2-1.1.0.tar.gz
Source0  : http://pypi.debian.net/unittest2/unittest2-1.1.0.tar.gz
Source99 : http://pypi.debian.net/unittest2/unittest2-1.1.0.tar.gz.asc
Summary  : The new features in unittest backported to Python 2.4+.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: deprecated-unittest2-bin = %{version}-%{release}
Requires: deprecated-unittest2-python = %{version}-%{release}
Requires: argparse
Requires: six
Requires: traceback2
BuildRequires : argparse
BuildRequires : buildreq-distutils
BuildRequires : buildreq-distutils3
BuildRequires : deprecated-linecache2-legacypython
BuildRequires : deprecated-six-legacypython
BuildRequires : deprecated-traceback2-legacypython
BuildRequires : python3-dev
BuildRequires : setuptools-legacypython
BuildRequires : six
Patch1: remove-argparse-from-requires.patch

%description
unittest2 is a backport of the new features added to the unittest testing
framework in Python 2.7 and onwards. It is tested to run on Python 2.6, 2.7,
3.2, 3.3, 3.4 and pypy.

%package bin
Summary: bin components for the deprecated-unittest2 package.
Group: Binaries

%description bin
bin components for the deprecated-unittest2 package.


%package legacypython
Summary: legacypython components for the deprecated-unittest2 package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the deprecated-unittest2 package.


%package python
Summary: python components for the deprecated-unittest2 package.
Group: Default

%description python
python components for the deprecated-unittest2 package.


%prep
%setup -q -n unittest2-1.1.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554340952
export MAKEFLAGS=%{?_smp_mflags}
python2 setup.py build -b py2

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/unit2

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)
