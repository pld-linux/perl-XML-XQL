#
# Conditional build:
%bcond_without tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	XQL
Summary:	XML::XQL - query XML tree structures with XQL
Summary(pl):	XML::XQL - odpytywanie struktur drzewiastych XML-a przy u¿yciu XQL-a
Name:		perl-XML-XQL
Version:	0.68
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bb84096fdf8bcc96a35971539ce8c19e
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-XML-DOM >= 1.29
BuildRequires:	perl-Date-Manip >= 5.33
BuildRequires:	perl-Parse-Yapp
BuildRequires:	perl-XML-Parser >= 2.30
%endif
Obsoletes:	perl-libxml-enno
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Perl extension that allows you to perform XQL queries on XML
object trees. Currently only the XML::DOM module is supported, but
other implementations, like XML::Grove, may soon follow.

%description -l pl
Jest to rozszerzenie Perla pozwalaj±ce na wykonywanie zapytañ XQL na
drzewach obiektów XML. Aktualnie obs³ugiwany jest tylko modu³
XML::DOM, ale mo¿e wkrótce bêd± inne implementacje, takie jak
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
