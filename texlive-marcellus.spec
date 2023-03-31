Name:		texlive-marcellus
Version:	64451
Release:	2
Summary:	Marcellus fonts with LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/marcellus
License:	ofl lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/marcellus.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/marcellus.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the Marcellus family of fonts, designed by Brian J.
Bonislawsky. Marcellus is a flared-serif family, inspired by
classic Roman inscription letterforms. There is currently just
a regular weight and small-caps. The regular weight will be
silently substituted for bold.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/marcellus
%{_texmfdistdir}/fonts/vf/public/marcellus
%{_texmfdistdir}/fonts/type1/public/marcellus
%{_texmfdistdir}/fonts/truetype/public/marcellus
%{_texmfdistdir}/fonts/tfm/public/marcellus
%{_texmfdistdir}/fonts/map/dvips/marcellus
%{_texmfdistdir}/fonts/enc/dvips/marcellus
%doc %{_texmfdistdir}/doc/fonts/marcellus

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
