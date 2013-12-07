# revision 16864
# category Package
# catalog-ctan /macros/latex/contrib/url
# catalog-date 2010-01-27 23:13:46 +0100
# catalog-license lppl
# catalog-version 3.2
Name:		texlive-url
Version:	3.2
Release:	5
Summary:	Verbatim with URL-sensitive line breaks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/url
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/url.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/url.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The command \url is a form of verbatim command that allows
linebreaks at certain characters or combinations of characters,
accepts reconfiguration, and can usually be used in the
argument to another command. (The \urldef command provides
robust commands that serve in cases when \url doesn't work in
an argument.) The command is intended for email addresses,
hypertext links, directories/paths, etc., which normally have
no spaces, so by default the package ignores spaces in its
argument. However, a package option "allows spaces", which is
useful for operating systems where spaces are a common part of
file names.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/url/url.sty
%doc %{_texmfdistdir}/doc/latex/url/miscdoc.sty
%doc %{_texmfdistdir}/doc/latex/url/url.pdf
%doc %{_texmfdistdir}/doc/latex/url/url.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.2-2
+ Revision: 757328
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 3.2-1
+ Revision: 719861
- texlive-url
- texlive-url
- texlive-url

