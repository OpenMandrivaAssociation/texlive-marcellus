%global tl_name marcellus
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Marcellus fonts with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/marcellus
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/marcellus.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/marcellus.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for
the Marcellus family of fonts, designed by Brian J. Bonislawsky.
Marcellus is a flared-serif family, inspired by classic Roman
inscription letterforms. There is currently just a regular weight and
small-caps. The regular weight will be silently substituted for bold.

