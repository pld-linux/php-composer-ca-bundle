# TODO
# - system ca certs
%define		php_min_version 5.3.2
%define		pkgname	ca-bundle
%include	/usr/lib/rpm/macros.php
Summary:	Lets you find a path to the system CA bundle, and includes a fallback to the Mozilla CA bundle
Name:		php-composer-%{pkgname}
Version:	1.0.2
Release:	0.1
License:	MIT
Group:		Development/Libraries
Source0:	https://github.com/composer/ca-bundle/archive/%{version}/%{pkgname}-%{version}.tar.gz
# Source0-md5:	0e08430806fbcad13b8e568a854e5b4e
URL:		https://github.com/composer/ca-bundle
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
