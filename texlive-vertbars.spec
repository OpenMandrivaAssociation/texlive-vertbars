%global tl_name vertbars
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0c
Release:	%{tl_revision}.1
Summary:	Mark vertical rules in margin of text
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/vertbars
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/vertbars.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/vertbars.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is an extension to lineno, replacing that package's line
numbers with bars to the left or right of the text.

