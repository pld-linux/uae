Summary:	Unix Amiga Emulator
Summary(pl):	Unixowy Emulator Amigi
Name:		uae
Version:	0.8.16
Release:	2
License:	GPL
Group:		Applications/Emulators
Source0:	ftp://ftp.freiburg.linux.de/pub/uae/sources/develop/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac_fixes.patch
URL:		http://www.freiburg.linux.de/~uae/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
UAE is mostly complete software emulation of the hardware of the
Commodore Amiga 500/1000/2000. A Commodore Amiga is a 16/32 bit
computer system based on the Motorola 680x0 CPU and a few specially
designed custom chips that provide very good graphics and sound
capabilities. UAE is written for Unixish systems; it is developed on a
Linux machine but it should compile and run on any half-recent
Unix-like operating system.

This program have SUID!

%description -l pl
UAE jest w wiêkszo¶ci kompletnym oprogramowaniem do emulacji Commodore
Amiga 500/1000/2000. Commodore Amiga jest 16/32 bitowym komputerem
bazuj±cym na procesorze Motorola 680x0 i kilku specjalnie
zaprojektowanych ko¶ciach oferuj±cych bardzo dobr± grafikê i muzykê.
UAE jest napisany dla systemów uniksowych; jest rozwijany pod linuksem
ale powinien siê kompilowaæ na wiêkszo¶ci platformach uniksowych.

Program ma SUID!

%prep
%setup -q
%patch0 -p1

%build
libtoolize --copy --force
aclocal -I %{_aclocaldir}/gnome
autoconf
automake -a -c || :
%configure \
	--with-x \
	--enable-sound \
	--enable-dga \
	--enable-vidmode \
	--enable-ui \
	--enable-threads
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_bindir}

install {readdisk,uae} $RPM_BUILD_ROOT/%{_bindir}

gzip -9nf docs/{COMPATIBILITY,CREDITS,FAQ,NEWS,README}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*.gz
%attr(0755,root,root) %{_bindir}/readdisk
%attr(0755,root,root) %{_bindir}/uae
