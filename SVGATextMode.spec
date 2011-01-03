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
