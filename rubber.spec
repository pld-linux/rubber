Summary:	A LaTeX wrapper for automatically building documents
Summary(pl):	Wrapper LaTeXa dla automatycznie budowanych dokumentów
Name:		rubber
Version:	1.1
Release:	1
License:	GPL v2
Group:		Applications/Publishing/TeX
Source0:	http://ebeffara.free.fr/pub/%{name}-%{version}.tar.gz
# Source0-md5:	8087cdb498f51f91c2427c7d0b253189
URL:		http://www.pps.jussieu.fr/~beffara/soft/rubber/
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	tetex-latex
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rubber is a program whose purpose is to handle all tasks related to
the compilation of LaTeX documents. This includes compiling the
document itself, of course, enough times so that all references are
defined, and running BibTeX to manage bibliographic references.
Automatic execution of dvips to produce PostScript documents is also
included, as well as usage of pdfLaTeX to produce PDF documents.

%description -l pl
Rubber jest programem wykonuj±cym wszystkie zadania zwi±zane z
kompilacj± dokumentów LaTeXa. Zadania te obejmuj± kompilacjê samego
dokumentu, oczywi¶cie tak± liczbê razy, ¿eby wszystkie referencje
zosta³y zdefiniowane, oraz uruchamianie BibTeXa zarz±dzaj±cego
odno¶nikami bibliograficznymi. Dodatkowo rubber automatycznie wywo³uje
dvips aby stworzyæ dokumenty PostScript oraz pdfLaTeX aby stworzyæ
dokumenty PDF.

%prep
%setup -q

%build
./configure \
	--prefix=%{_prefix} \
	--mandir=%{_mandir} \
	--infodir=%{_infodir}

python setup.py build

%{__make} -C doc all

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{py_sitescriptdir}/rubber/ -name "*.py" -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/rubber
%{py_sitescriptdir}/*.egg-info
%{_datadir}/%{name}
%{_infodir}/rubber*
%{_mandir}/man1/rubber*
%lang(fr) %{_mandir}/fr/man1/rubber*
