%define	name	SVGATextMode
%define	version	1.10
%define	release	%mkrel 14

Summary:	A utility for improving the appearance of text consoles
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Terminals
Source0:	ftp://metalab.unc.edu/pub/Linux/utils/console/%{name}-%{version}-src.tar.bz2
Source1:	%{name}-kernel2.4-headers.tar.bz2
#(deush) regenerate patch0
Patch0:		%{name}-1.9-make.patch
#(deush) add some fonts 
Patch1:		%{name}-1.9-src-mdk.patch
#(deush) kernel-headers --> add include file where missed ...
#Patch2:	%{name}-1.10-include.patch.bz2
Patch3:		%{name}-1.9-set80.patch
Patch4:		%{name}-1.9-src-manbz2.patch
Patch5:		%{name}-missing-header-fix.patch
Patch6:		%{name}-1.10-gcc-3.3.patch
Patch7:		%{name}-1.10-use-2.4-headers.patch
Patch8:		SVGATextMode-1.10-fix-build.patch
Patch9:		SVGATextMode-1.10-kheaders-build-fix.patch
Patch10:	SVGATextMode-1.10-fix-str-fmt.patch
Requires:	kbd
BuildRequires:	bison flex
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
ExclusiveArch:	%{ix86}

%description
SVGATextMode is a utility for reprogramming (S)VGA hardware,
which can improve the appearance of text consoles.
You should install SVGATextMode if you want to alter the
appearance of your text consoles. The utility uses a 
configuration file (TextConfig) to set up 
textmodes with higher resolution, larger fonts, higher 
display refresh rates, etc.

Although SVGATextMode can be used to program any text
mode size, your results will depend on your VGA card.

%prep
%setup -q -a1
%patch0 -p1 -b .make
%patch1 -p1 -b .rh
#%patch2 -p1 
%patch3 -p0 -b .set80
%patch4 -p1 -b .warly
%patch5 -p0 -b .peroyvind
%patch6 -p1 -b .gcc3.3
%patch7 -p1 -b .kernel2.4
%patch8 -p1 -b .sys_types.h
%patch9 -p1 -b .kheaders-build-fix
%patch10 -p0 -b .str

%build
%make dep
%make all CFLAGS_DEFAULT="%optflags"
# CFLAGS="$RPM_OPT_FLAGS -IXFREE/include"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{etc,usr/man/man5,usr/man/man8,usr/sbin}
make DESTDIR=$RPM_BUILD_ROOT newinstall manbz2-install
install -m 0755 STMmenu $RPM_BUILD_ROOT%{_sbindir}/stm-menu
# move man pages
mkdir $RPM_BUILD_ROOT%{_datadir}
mv $RPM_BUILD_ROOT/usr/man $RPM_BUILD_ROOT%{_datadir}

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/TextConfig
%doc README README.FIRST CREDITS COPYING HISTORY TODO Changelog
%doc doc/*
%{_sbindir}/*
%{_mandir}/*/*


%changelog
* Mon Jan 03 2011 Funda Wang <fwang@mandriva.org> 1.10-14mdv2011.0
+ Revision: 627703
- fix str fmt

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Mon Jul 28 2008 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1.10-13mdv2009.0
+ Revision: 251928
- Uncompress all package patches.
- Fix build with latest kernel headers.

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
    - Import SVGATextMode



* Thu Jun 22 2006 Lenny Cartier <lenny@mandriva.com> 1.10-12mdv2007.0
- rebuild

* Fri Apr 28 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.10-11mdk
- fix build (P8)
- compile with $RPM_OPT_FLAGS
- %%mkrel
- fix summary-ended-with-dot

* Mon Jun 14 2004 Per �yvind Karlsen <peroyvind@linux-mandrake.com> 1.10-10mdk
- fix buildrequires

* Mon Apr 19 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.10-9mdk
- ship with kernel 2.4 headers (S1) and use them (P7)

* Wed Jul 23 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.10-8mdk
- oops, fix gcc-3.3 patch (P6), thx gwenole

* Tue Jul 15 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.10-7mdk
- fix gcc-3.3 build (P6)

* Fri May 23 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.10-6mdk
- rebuild for rpm-4.2
- macroize
- quiet setup
- fix problem with missing header causing SVGATextMode not to compile (Patch5)
- nicer formatting
- drop unapplied patch(Patch2)

* Tue Sep 11 2001 Stefan van der Eijk <stefan@eijk.nu> 1.10-5mdk
- BuildRequires: bison flex
- Copyright --> License

* Tue May 22 2001 Jeff Garzik <jgarzik@mandrakesoft.com> 1.10-4mdk
- Use ix86 macro in ExclusiveArch

* Tue Jan 09 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.10-3mdk
- include cache.h again, and rebuild for kernel 2.4.

* Sat Nov 25 2000 Daouda Lo <daouda@mandrakesoft.com> 1.10-2mdk
- build with defaults cflags -O3 (chmouel).

* Fri Nov 24 2000 Daouda Lo <daouda@mandrakesoft.com> 1.10-1mdk
- release
- fix gcc-2.96 compilation
- redefine path to kernel headers (cache.h and dcache.h)
- macroz + cleanup 

* Tue Aug 29 2000 Etienne Faure <etienne@mandrakesoft.com> 1.9-7mdk
- rebuilt using _mandir macro

* Mon Apr  3 2000 Adam Lebsack <adam@mandrakesoft.com> 1.9-6mdk
- release build.

* Thu Dec 30 1999 Florent Villard <warlyl@mandrakesoft.com> 1.9-5mdk
- clean the bz2 man pages 

* Mon Dec 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Don't do a set80 under X (break X).

* Wed Dec  1 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Upgrade ExclusiveArch to support k6.
- add a defattr.

* Sat Jul 17 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- 1.9
- Update ExclusiveArch tag to support i486 and i686
- set more reasonable defaults
- fix handling of $RPM_OPT_FLAGS
- use always at least -O2 (needed for outb())

* Wed Jun 30 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Update ExclusiveArch tag.

* Tue May 04 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions
- add de locale
- fix a bug in the %%description - SVGATextMode does NOT use XF86Config

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 4)

* Wed Jan 06 1999 Cristian Gafton <gafton@redhat.com>
- glibc 2.1

* Thu Sep 03 1998 Cristian Gafton <gafton@redhat.com>
- added patch for Matrox Millenium AGP

* Fri May 01 1998 Cristian Gafton <gafton@redhat.com>
- ExclusiveArch: i386

* Sun Jan 11 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.8
- built against glibc; spec file cleanup

* Wed Jul 2 1997 Timo Karjalainen <timok@iki.fi>
- Upgraded to version 1.6

* Fri Jun 13 1997 Timo Karjalainen <timok@iki.fi>
- Config file moved from /usr/etc to /etc
- Some minor changes to specfile

* Wed Jun 4 1997 Ximenes Zalteca <ximenes@null.net>
- Re-Group:'d

* Sun Apr 27 1997 Christian 'Dr. Disk' Hechelmann <drdisk@ds9.au.s.shuttle.de>
- added %%changelog
- added %%clean
- added BuildRoot
