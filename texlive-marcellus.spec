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
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for
the Marcellus family of fonts, designed by Brian J. Bonislawsky.
Marcellus is a flared-serif family, inspired by classic Roman
inscription letterforms. There is currently just a regular weight and
small-caps. The regular weight will be silently substituted for bold.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from marcellus:
Map marcellus.map
TL_DROPIN_EOF
