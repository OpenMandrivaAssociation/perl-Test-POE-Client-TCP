%define upstream_name    Test-POE-Client-TCP
%define upstream_version 1.12

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.12
Release:	3

Summary:	A POE Component providing TCP client services for test cases
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/Test-POE-Client-TCP-1.12.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(POE)
BuildRequires:	perl(POE::Filter)
BuildRequires:	perl(POE::Filter::Line)
BuildRequires:	perl(POE::Wheel::ReadWrite)
BuildRequires:	perl(POE::Wheel::SocketFactory)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Text::ParseWords)
BuildArch:	noarch

%description
Test::POE::Client::TCP is a the POE manpage component that provides a TCP
client framework for inclusion in client component test cases, instead of
having to roll your own.

Once registered with the component, a session will receive events related
to connections made, disconnects, flushed output and input from the
specified server.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/Test


%changelog
* Tue Jul 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.100.0-1mdv2011.0
+ Revision: 688831
- update to new version 1.10

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.80.0-1mdv2011.0
+ Revision: 552637
- update to 1.08

* Sat Nov 07 2009 Jérôme Quelin <jquelin@mandriva.org> 1.60.0-1mdv2010.1
+ Revision: 462460
- update to 1.06

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.40.0-1mdv2010.0
+ Revision: 405591
- rebuild using %%perl_convert_version

* Sun Jun 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.04-1mdv2010.0
+ Revision: 387781
- update to new version 1.04

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-1mdv2010.0
+ Revision: 370217
- update to new version 1.02

* Wed Jan 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdv2009.1
+ Revision: 332123
- update to new version 0.10

* Fri Jan 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdv2009.1
+ Revision: 330195
- update to new version 0.08

* Wed Jul 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdv2009.0
+ Revision: 230639
- update to new version 0.06

* Sat May 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdv2009.0
+ Revision: 210832
- import perl-Test-POE-Client-TCP


* Sat May 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdv2009.0
- first mdv release

