%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	XML-XQL perl module
Summary(pl):	Modu� perla XML-XQL
Name:		perl-XML-XQL
Version:	0.60
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/XML-XQL-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
BuildRequires:	perl-XML-DOM
BuildRequires:	perl-Parse-Yapp
BuildRequires:	perl-Date-Manip
%requires_eq	perl
Requires:	%{perl_sitearch}
Requires:	perl-XML-DOM
Requires:	perl-Parse-Yapp
Requires:	perl-Date-Manip
BuildRoot:	/tmp/%{name}-%{version}-root

%description
XML-XQL - module that allows you to perform XQL queries on XML object trees. 

%description -l pl
XML-XQL - modu� pozwalaj�cy na zapytania XQL na drzewach obiekt�w XML.

%prep
%setup -q -n XML-XQL-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/XML/XQL
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz
%attr(755,root,root) %{_bindir}/xql.pl

%{perl_sitelib}/XML/XQL.pm
%{perl_sitelib}/XML/XQL
%{perl_sitearch}/auto/XML/XQL

%{_mandir}/man3/*
