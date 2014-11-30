#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	XML
%define		pnam	XQL
%include	/usr/lib/rpm/macros.perl
Summary:	XML::XQL - query XML tree structures with XQL
Summary(pl.UTF-8):	XML::XQL - odpytywanie struktur drzewiastych XML-a przy użyciu XQL-a
Name:		perl-XML-XQL
Version:	0.68
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bb84096fdf8bcc96a35971539ce8c19e
URL:		http://search.cpan.org/dist/XML-XQL/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Date-Manip >= 5.33
BuildRequires:	perl-Parse-Yapp
BuildRequires:	perl-XML-DOM >= 1.29
BuildRequires:	perl-XML-Parser >= 2.30
%endif
Obsoletes:	perl-libxml-enno
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Perl extension that allows you to perform XQL queries on XML
object trees. Currently only the XML::DOM module is supported, but
other implementations, like XML::Grove, may soon follow.

%description -l pl.UTF-8
Jest to rozszerzenie Perla pozwalające na wykonywanie zapytań XQL na
drzewach obiektów XML. Aktualnie obsługiwany jest tylko moduł
XML::DOM, ale może wkrótce będą inne implementacje, takie jak
XML::Grove.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/XML/XQL.pm
%dir %{perl_vendorlib}/XML/XQL
%{perl_vendorlib}/XML/XQL/*.pm
%{_mandir}/man3/*
%attr(755,root,root) %{_bindir}/*
