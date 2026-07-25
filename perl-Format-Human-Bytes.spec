%define upstream_name    Format-Human-Bytes
%define upstream_version 0.06

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	6

Summary:	Format bytecounts in a human readable form
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Format-Human-Bytes
Source0:	https://cpan.metacpan.org/authors/id/S/SE/SEWI/Format-Human-Bytes-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Module::Install)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
Format bytecounts in a human readable form.

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
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.60.0-2mdv2011.0
+ Revision: 654330
- rebuild for updated spec-helper

* Sat Sep 18 2010 Shlomi Fish <shlomif@mandriva.org> 0.60.0-1mdv2011.0
+ Revision: 579590
- Upgraded to 0.06 and now using tar.lzma

* Fri Apr 09 2010 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 533390
- update to 0.05

* Sun Dec 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.1
+ Revision: 474244
- import perl-Format-Human-Bytes


* Sun Dec 06 2009 cpan2dist 0.04-1mdv
- initial mdv release, generated with cpan2dist
