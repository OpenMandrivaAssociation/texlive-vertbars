# revision 20589
# category Package
# catalog-ctan /macros/latex/contrib/vertbars
# catalog-date 2010-11-28 20:56:07 +0100
# catalog-license lppl1.3
# catalog-version 1.0b
Name:		texlive-vertbars
Version:	1.0b
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package is an extension to lineno, replacing that
package's line numbers with bars to the left or right of the
text.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/vertbars/vertbars.sty
%doc %{_texmfdistdir}/doc/latex/vertbars/README
%doc %{_texmfdistdir}/doc/latex/vertbars/vertbars.pdf
#- source
%doc %{_texmfdistdir}/source/latex/vertbars/vertbars.ins
%doc %{_texmfdistdir}/source/latex/vertbars/vertbars.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
