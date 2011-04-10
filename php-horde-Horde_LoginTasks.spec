# TODO
# - system locale dir
%define		status		stable
%define		pearname	Horde_LoginTasks
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Horde Login Tasks System
Name:		php-horde-Horde_LoginTasks
Version:	1.0.0
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	375e944c2ff8c06f08ca700a9e35704e
URL:		http://pear.horde.org/package/Horde_LoginTasks/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.horde.org)
Requires:	php-horde-Horde_Translation < 2.0.0
Requires:	php-pear
Suggests:	php-horde-Horde_Date
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	 pear(Horde/Date.*)

%description
The Horde_LoginTasks library provides a set of methods for dealing
with tasks run upon login to Horde applications.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc optional-packages.txt
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Horde/LoginTasks.php
%{php_pear_dir}/Horde/LoginTasks
%{php_pear_dir}/data/Horde_LoginTasks
