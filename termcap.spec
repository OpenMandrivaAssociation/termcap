%define	name	termcap
%define	version	11.0.1

Summary:	The terminal feature database used by certain applications
Name:		%{name}
Version:	%{version}
Release:	%mkrel 15
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

%ifarch sparc
Obsoletes:	termfiles_sparc
Provides:	termfiles_sparc
%endif
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%build

%install
rm -rf %{buildroot}
install -m644 %{name} -D %{buildroot}%{_sysconfdir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/%{name}


