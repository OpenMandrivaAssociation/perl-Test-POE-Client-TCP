%define module   Test-POE-Client-TCP
%define version    1.02
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    A POE Component providing TCP client services for test cases
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Test/%{module}-%{version}.tar.gz
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(POE)
BuildRequires: perl(POE::Filter)
BuildRequires: perl(POE::Filter::Line)
BuildRequires: perl(POE::Wheel::ReadWrite)
BuildRequires: perl(POE::Wheel::SocketFactory)
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::ParseWords)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Test::POE::Client::TCP is a the POE manpage component that provides a TCP
client framework for inclusion in client component test cases, instead of
having to roll your own.

Once registered with the component, a session will receive events related
to connections made, disconnects, flushed output and input from the
specified server.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/Test

