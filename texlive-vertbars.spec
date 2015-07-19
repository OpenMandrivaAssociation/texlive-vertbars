# revision 20589
# category Package
# catalog-ctan /macros/latex/contrib/vertbars
# catalog-date 2010-11-28 20:56:07 +0100
# catalog-license lppl1.3
# catalog-version 1.0b
Name:		texlive-vertbars
Version:	1.0b
Release:	10
Summary:	Mark vertical rules in margin of text
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/vertbars
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vertbars.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vertbars.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vertbars.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is an extension to lineno, replacing that
package's line numbers with bars to the left or right of the
text.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/vertbars/vertbars.sty
%doc %{_texmfdistdir}/doc/latex/vertbars/README
%doc %{_texmfdistdir}/doc/latex/vertbars/vertbars.pdf
#- source
%doc %{_texmfdistdir}/source/latex/vertbars/vertbars.ins
%doc %{_texmfdistdir}/source/latex/vertbars/vertbars.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0b-2
+ Revision: 757421
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0b-1
+ Revision: 719888
- texlive-vertbars
- texlive-vertbars
- texlive-vertbars

