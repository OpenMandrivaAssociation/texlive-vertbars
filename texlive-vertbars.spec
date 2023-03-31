Name:		texlive-vertbars
Version:	49429
Release:	2
Summary:	Mark vertical rules in margin of text
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/vertbars
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vertbars.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vertbars.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/vertbars
%doc %{_texmfdistdir}/doc/latex/vertbars

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
