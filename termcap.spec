Summary:	The terminal feature database used by certain applications
Name:		termcap
Version:	11.0.1
Release:	28
License:	none
Group:		System/Libraries
URL:		http://www.catb.org/~esr/terminfo/
Source0:	http://www.ccil.org/~esr/terminfo/termtypes.tc.bz2
Patch0:		termcap-linuxlat.patch
Patch1:		termcap-xtermchanges.patch
Patch2:		termcap-utf8.patch
# (fc) 11.0.1-4mdk patch to correctly handle Home/End with X11R6 keycode
Patch3:		termcap-xtermX11R6.patch
# (vdanen) 11.0.1-6mdk patch so Eterm is seen as a color-capable term
Patch4:		termcap-Eterm.patch
# (shikamaru) 11.0.1-17mdv add urxvt as well
Patch5:		termcap-urxvt.patch

%ifarch sparc
%rename	termfiles_sparc
%endif
BuildArch:	noarch

%description
The termcap package provides the /etc/termcap file.  /etc/termcap is
a database which defines the capabilities of various terminals and
terminal emulators.  Certain programs use the /etc/termcap file to
access various features of terminals (the bell, colors, and graphics,
etc.).

%prep
%setup -q -T -c %{name}-%{version}
bzcat %{SOURCE0} > %{name}
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p0

%build

%install
install -m644 %{name} -D %{buildroot}%{_sysconfdir}/%{name}

%files
%config(noreplace) %{_sysconfdir}/%{name}




%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 11.0.1-20mdv2011.0
+ Revision: 670675
- mass rebuild

* Tue Nov 30 2010 Rémy Clouard <shikamaru@mandriva.org> 11.0.1-19mdv2011.0
+ Revision: 604012
- update termcap info for rxvt-unicode

* Thu Apr 08 2010 Rémy Clouard <shikamaru@mandriva.org> 11.0.1-18mdv2010.1
+ Revision: 533137
- add urxvt to termcap as well

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 11.0.1-17mdv2010.1
+ Revision: 520262
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 11.0.1-16mdv2010.0
+ Revision: 427292
- rebuild

* Sat Mar 21 2009 Funda Wang <fwang@mandriva.org> 11.0.1-15mdv2009.1
+ Revision: 359941
- rediff linuxlat patch

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 11.0.1-14mdv2009.0
+ Revision: 225648
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 11.0.1-13mdv2008.1
+ Revision: 179644
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Nov 21 2006 Pablo Saratxaga <pablo@mandriva.com> 11.0.1-12mdv2007.0
+ Revision: 85806
- fixed "ho" entry in patch3 (bug #7244)
- Import termcap

* Tue Aug 01 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 11.0.1-11mdv2007.0
- revert license back to none
- add url

* Tue Aug 01 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 11.0.1-10mdv2007.0
- %%mkrel
- with no license, this package should be considered as public domain, therefore
  set license to Public Domain

* Thu Dec 23 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 11.0.1-9mdk
- cleanups!
- buildarch set to noarch

