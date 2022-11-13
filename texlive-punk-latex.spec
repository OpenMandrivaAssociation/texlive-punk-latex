Name:		texlive-punk-latex
Version:	27389
Release:	1
Summary:	LaTeX support for punk fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/punk-latex
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/punk-latex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/punk-latex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package and .fd file provide support for Knuth's punk
fonts. That bundle also offers support within LaTeX; the
present package is to be preferred.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/punk-latex/ot1pnk.fd
%{_texmfdistdir}/tex/latex/punk-latex/punk.sty
%doc %{_texmfdistdir}/doc/latex/punk-latex/README
%doc %{_texmfdistdir}/doc/latex/punk-latex/punk.pdf
%doc %{_texmfdistdir}/doc/latex/punk-latex/punk.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
