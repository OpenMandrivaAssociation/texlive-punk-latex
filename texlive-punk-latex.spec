# revision 27389
# category Package
# catalog-ctan /macros/latex/contrib/punk-latex
# catalog-date 2012-05-30 14:49:05 +0200
# catalog-license gpl
# catalog-version 1.1
Name:		texlive-punk-latex
Version:	1.1
Release:	2
Summary:	LaTeX support for punk fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/punk-latex
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/punk-latex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/punk-latex.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
