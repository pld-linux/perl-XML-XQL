
# Conditional build:
%bcond_without tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	XQL
Summary:	Query XML tree structures with XQL
Name:		perl-XML-XQL
Version:	0.68
Release:	1
License:	Same as Perl Itself
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bb84096fdf8bcc96a35971539ce8c19e
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(XML::DOM) >= 1.29
BuildRequires:	perl-Parse-Yapp
BuildRequires:	perl-Date-Manip >= 5.33
BuildRequires:	perl-XML-Parser >= 2.30
%endif
Obsoletes:	perl-libxml-enno
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Perl extension that allows you to perform XQL queries on XML
object trees. Currently only the XML::DOM module is supported, but
other implementations, like XML::Grove, may soon follow.

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
%{perl_vendorlib}/XML/XQL/*.pm
%{_mandir}/man3/*
%attr(755,root,root) %{_bindir}/*
