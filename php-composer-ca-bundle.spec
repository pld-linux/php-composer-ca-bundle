%define		php_min_version 5.3.2
%define		pkgname	ca-bundle
%include	/usr/lib/rpm/macros.php
Summary:	Lets you find a path to the system CA bundle, and includes a fallback to the Mozilla CA bundle
Name:		php-composer-%{pkgname}
Version:	1.1.4
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/composer/ca-bundle/archive/%{version}/%{pkgname}-%{version}.tar.gz
# Source0-md5:	30c69a32798c044be829245f87a82c94
URL:		https://github.com/composer/ca-bundle
Patch0:		system-ca-certs.patch
Requires:	ca-certificates >= 20141019-3
Requires:	php(core) >= %{php_min_version}
Requires:	php(openssl)
Requires:	php(pcre)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Small utility library that lets you find a path to the system CA
bundle, and includes a fallback to the Mozilla CA bundle.

Originally written as part of composer/composer, now extracted and
made available as a stand-alone library.

%prep
%setup -q -n %{pkgname}-%{version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/Composer/CaBundle
cp -a src/* $RPM_BUILD_ROOT%{php_data_dir}/Composer/CaBundle

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%dir %{php_data_dir}/Composer
%{php_data_dir}/Composer/CaBundle
