%define upstream_name    boolean
%define upstream_version 0.20

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Boolean support for Perl
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

Provides: perl(boolean)

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


