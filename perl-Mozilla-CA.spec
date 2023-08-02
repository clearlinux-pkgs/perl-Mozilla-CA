#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Mozilla-CA
Version  : 20221114
Release  : 38
URL      : https://cpan.metacpan.org/authors/id/H/HA/HAARG/Mozilla-CA-20221114.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/H/HA/HAARG/Mozilla-CA-20221114.tar.gz
Summary  : "Mozilla's CA cert bundle in PEM format"
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0 MPL-1.1
Requires: perl-Mozilla-CA-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Mozilla::CA - Mozilla's CA cert bundle in PEM format
SYNOPSIS
use IO::Socket::SSL;
use Mozilla::CA;

%package dev
Summary: dev components for the perl-Mozilla-CA package.
Group: Development
Provides: perl-Mozilla-CA-devel = %{version}-%{release}
Requires: perl-Mozilla-CA = %{version}-%{release}

%description dev
dev components for the perl-Mozilla-CA package.


%package perl
Summary: perl components for the perl-Mozilla-CA package.
Group: Default
Requires: perl-Mozilla-CA = %{version}-%{release}

%description perl
perl components for the perl-Mozilla-CA package.


%prep
%setup -q -n Mozilla-CA-20221114
cd %{_builddir}/Mozilla-CA-20221114

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Mozilla::CA.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
