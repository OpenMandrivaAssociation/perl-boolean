%define upstream_name    boolean
Name:		perl-%{upstream_name}
Version:	0.46
Release:	2

Summary:	Boolean support for Perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/ingydotnet/boolean-pm
Source0:	https://cpan.metacpan.org/authors/id/I/IN/INGY/boolean-%{version}.tar.gz

BuildRequires:	make
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
%setup -q -n %{upstream_name}-%{version}

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
