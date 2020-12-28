Summary:	Unix Amiga Emulator
Summary(pl.UTF-8):	Uniksowy Emulator Amigi
Name:		uae
Version:	0.8.29
Release:	2
License:	GPL v2
Group:		Applications/Emulators
Source0:	http://www.amigaemulator.org/files/sources/develop/%{name}-%{version}.tar.bz2
# Source0-md5:	54abbabb5e8580b679c52de019141d61
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-ac_fixes.patch
Patch1:		%{name}-allow_spaces_in_zip_filenames.patch
Patch2:		%{name}-preserve_home_in_writing_optionsfile.patch
Patch3:		%{name}-struct_uae_wrong_fields_name.patch
Patch4:		%{name}-uae_reset_args.patch
Patch5:		format-security.patch
Patch6:		xvidmode.patch
URL:		http://www.amigaemulator.org/
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.4.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXxf86dga-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
Requires:	gtk+2 >= 2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UAE is mostly complete software emulation of the hardware of the
Commodore Amiga 500/1000/2000. A Commodore Amiga is a 16/32 bit
computer system based on the Motorola 680x0 CPU and a few specially
designed custom chips that provide very good graphics and sound
capabilities. UAE is written for Unixish systems; it is developed on a
Linux machine but it should compile and run on any half-recent
Unix-like operating system.

%description -l pl.UTF-8
UAE jest w większości kompletnym oprogramowaniem do emulacji Commodore
Amiga 500/1000/2000. Commodore Amiga jest 16/32 bitowym komputerem
bazującym na procesorze Motorola 680x0 i kilku specjalnie
zaprojektowanych kościach oferujących bardzo dobrą grafikę i muzykę.
UAE jest napisany dla systemów uniksowych; jest rozwijany pod Linuksem
ale powinien się kompilować na większości platformach uniksowych.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p0

sed -e 's/build68kc/build68k/' -i src/Makefile.in

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--disable-file-sound	\
	--enable-dga		\
	--enable-threads	\
	--enable-ui		\
	--enable-vidmode	\
	--without-asciiart	\
	--without-sdl		\
	--without-sdl-sound	\
	--without-sdl-gfx	\
	--without-svgalib	\
	--with-alsa		\
	--with-x

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_desktopdir}}

install readdisk uae $RPM_BUILD_ROOT%{_bindir}
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/{COMPATIBILITY,CREDITS,FAQ,NEWS,README}
%attr(755,root,root) %{_bindir}/readdisk
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
