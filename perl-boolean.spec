%define upstream_name    boolean
%define upstream_version 0.23

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Boolean support for Perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildArch:	noarch
Provides:	perl(boolean)

%description
Most programming languages have a native 'Boolean' data type. Perl does
not.

Perl has a simple and well known Truth System. The following scalar values
are false:

    $false1 = undef;
    $false2 = 0;
    $false3 = 0.0;
    $false4 = '';
    $false5 = '0';

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.230.0-2mdv2011.0
+ Revision: 656982
- rebuild for updated spec-helper

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.230.0-1mdv2011.0
+ Revision: 596720
- update to 0.23

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.200.0-1mdv2011.0
+ Revision: 471281
- import perl-boolean


* Sun Nov 29 2009 cpan2dist 0.20-1mdv
- initial mdv release, generated with cpan2dist
