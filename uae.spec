Summary:	Unix Amiga Emulator
Summary(pl):	Uniksowy Emulator Amigi
Name:		uae
Version:	0.8.25
Release:	1
License:	GPL
Group:		Applications/Emulators
Source0:	ftp://ftp.freiburg.linux.de/pub/uae/sources/develop/%{name}-%{version}.tar.gz
# Source0-md5:	e660ca2bec3c016c978ef88117b0c432
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-ac_fixes.patch
Patch1:		%{name}-snd_file_fix.patch
URL:		http://www.freiburg.linux.de/~uae/
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UAE is mostly complete software emulation of the hardware of the
Commodore Amiga 500/1000/2000. A Commodore Amiga is a 16/32 bit
computer system based on the Motorola 680x0 CPU and a few specially
designed custom chips that provide very good graphics and sound
capabilities. UAE is written for Unixish systems; it is developed on a
Linux machine but it should compile and run on any half-recent
Unix-like operating system.

%description -l pl
UAE jest w wiêkszo¶ci kompletnym oprogramowaniem do emulacji Commodore
Amiga 500/1000/2000. Commodore Amiga jest 16/32 bitowym komputerem
bazuj±cym na procesorze Motorola 680x0 i kilku specjalnie
zaprojektowanych ko¶ciach oferuj±cych bardzo dobr± grafikê i muzykê.
UAE jest napisany dla systemów uniksowych; jest rozwijany pod Linuksem
ale powinien siê kompilowaæ na wiêkszo¶ci platformach uniksowych.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I %{_aclocaldir}/gnome
%{__autoconf}
%{__automake} || :
%configure \
	--enable-dga		\
	--enable-vidmode	\
	--enable-ui		\
	--enable-threads	\
	--disable-file-sound	\
	--with-x		\
	--without-svgalib	\
	--without-sdl		\
	--without-sdl-sound	\
	--without-sdl-gfx	\
	--with-alsa		\
	--without-asciiart

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_desktopdir}}

install readdisk uae $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/{COMPATIBILITY,CREDITS,FAQ,NEWS,README}
%attr(755,root,root) %{_bindir}/readdisk
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
