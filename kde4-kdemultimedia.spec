%define		_state		stable
%define		orgname		kdemultimedia
%define		qtver		4.8.1
%define		taglib_ver	1.5

Summary:	K Desktop Environment - multimedia applications
Summary(pl.UTF-8):	K Desktop Environment - aplikacje multimedialne
Name:		kde4-kdemultimedia
Version:	4.8.4
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	fdae8b516f4fc9e0025e2f316dad5709
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	QtTest-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cdparanoia-III-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	ffmpeg-devel >= 0.8
BuildRequires:	flac-devel >= 1.1.2
BuildRequires:	kde4-kdebase-workspace-devel >= %{version}
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	libmusicbrainz3-devel >= 1:3.0.0
BuildRequires:	libogg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtunepimp-devel
BuildRequires:	libvorbis-devel
BuildRequires:	phonon-devel >= 4.4.1
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	taglib-devel >= %{taglib_ver}
BuildRequires:	xine-lib-devel >= 1:1.0
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE multimedia applications. Package includes:

 - KMID - MIDI player,
 - KMIDI - software MIDI player,
 - KMIX - audio mixer,
 - KSCD - CD player,
 - Noatun - a media player.

%description -l pl.UTF-8
Multimedialne aplikacje KDE. Pakiet zawiera:

 - KMID - odtwarzacz MIDI,
 - KMIDI - programowy odtwarzacz MIDI,
 - KMIX - mikser audio,
 - KSCD - odtwarzacz CD,
 - Noatun - odtwarzacz plików multimedialnych.

%package libkcddb
Summary:	CDDB accessing library
Summary(pl.UTF-8):	Biblioteka dostępu do baz CDDB
Group:		X11/Libraries
Requires:	kde4-kdelibs >= %{version}

%description libkcddb
Library for accessing CDDB (cd track information databases) services.

%description libkcddb -l pl.UTF-8
Biblioteka dostępu do serwisów CDDB (baz danych z informacjami o
utworach).

%package devel
Summary:	Header files for kdemultimedia libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek kdemultimedia
Group:		X11/Development/Libraries
Requires:	%{name}-audiocd >= %{version}
Requires:	%{name}-libkcddb = %{version}-%{release}
Requires:	kde4-kdelibs-devel >= %{version}

%description devel
Header files for kdemultimedia libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek kdemultimedia

%package audiocd
Summary:	Audiocd protocol for konqueror
Summary(pl.UTF-8):	Protokół audiocd dla konquerora
Group:		X11/Applications
Requires:	%{name}-libkcddb = %{version}-%{release}
Requires:	kde4-konqueror >= %{version}
Provides:	kdemultimedia(audiocd) = %{version}-%{release}

%description audiocd
This package allows konqueror to play audiocd's without the need of an
external application. Just enter audiocd:/ in the location field.

%description audiocd -l pl.UTF-8
Ten pakiet pozwala konquerorowi odtwarzanie płyt z muzyką bez potrzeby
używania zewnętrznej aplikacji. Po prostu wpisz audiocd:/ w pole
adresu.

%package cddb
Summary:	CDDB library for KDE
Summary(pl.UTF-8):	Biblioteka CDDB pod KDE
Group:		X11/Applications
Requires:	%{name}-libkcddb = %{version}-%{release}
Requires:	kde4-kdebase >= %{version}

%description cddb
Support for cd database (CDDB), which is the source for track data for
KDE apps (title, author, etc.) when the cd does not have CD-Text.

%description cddb -l pl.UTF-8
Wsparcie dla baz danych płyt CD (CDDB) z których program ściąga
informacje o odtwarzanym utworze (tytuł, autora itd.) jeśli płyta nie
ma CD-Text.

%package dragon
Summary:	Dragon Player - very simple Phonon-based media player
Summary(pl.UTF-8):	Dragon Player - bardzo prosty odtwarzacz multimediów oparty na Phononie
Group:		X11/Libraries
Requires:	kde4-kdebase-workspace-solid >= %{version}
Requires:	kde4-kdelibs >= %{version}

%description dragon
Dragon Player - very simple Phonon-based media player.

%description dragon -l pl.UTF-8
Dragon Player - bardzo prosty odtwarzacz multimediów oparty na
Phononie.

%package juk
Summary:	A jukebox like program
Summary(pl.UTF-8):	Program spełniający funkcję szafy grającej
Group:		X11/Applications
Requires:	kde4-kdebase >= %{version}
Requires:	taglib >= %{taglib_ver}

%description juk
JuK (pronounced jook) is a jukebox and music manager for the KDE
desktop similar to jukebox software on other platforms such as
iTunes(R) or RealOne(R). As is typical with many jukebox applications,
JuK allows you to edit the "tags" of the audio files, and manage your
collection and playlists.

%description juk -l pl.UTF-8
Juk (czyt. dżuk, jak w Jukebox) to szafa grająca i zarządca muzyki dla
KDE podobny do iTunes(R) lub RealOne(R). Podobnie jak wiele innych
tego typu aplikacji, JuK umożliwia modyfikowanie znaczników plików
dźwiękowych i zarządzanie kolekcją oraz playlistami.

%package kmix
Summary:	KDE audio mixer
Summary(pl.UTF-8):	Mikser dźwięku dla KDE
Group:		X11/Applications
Requires:	kde4-kdebase >= %{version}

%description kmix
Sound mixer application for KDE.

%description kmix -l pl.UTF-8
Mikser dźwięku dla KDE.

%package kscd
Summary:	KDE CD Player
Summary(pl.UTF-8):	Odtwarzacz CD dla KDE
Group:		X11/Applications
Requires:	%{name}-libkcddb = %{version}-%{release}
Requires:	kde4-kdebase >= %{version}

%description kscd
CD Player with CDDB support. It can automatically update its CD
database with the Internet and show graphical interpretation of played
sounds.

%description kscd -l pl.UTF-8
Odtwarzacz CD z obsługą CDDB. Automatycznie uaktualnia swoją bazę
danych o płytach CD z Internetem. Potrafi także wyświetlić ładną
graficzną interpretację granych dźwięków.

%package mplayerthumbs
Summary:	Video thumbnail generator for KDE
Summary(pl.UTF-8):	Generator podglądów video dla KDE
Group:		X11/Applications
Requires:	kde4-kdebase >= %{version}
Requires:	mplayer

%description mplayerthumbs
MPlayerThumbs is a video thumbnail generator for KDE file managers
(Konqueror, Dolphin, ...) , now available also for KDE 4.

%package ffmpegthumbs
Summary:	Video thumbnail generator for KDE
Summary(pl.UTF-8):	Generator podglądów video dla KDE
Group:		X11/Applications
Requires:	kde4-kdebase >= %{version}
Requires:	ffmpeg >= 0.8

%description ffmpegthumbs
FFMpegThumbs is a video thumbnail generator for KDE file managers
(Konqueror, Dolphin, ...) , now available also for KDE 4.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang juk		--with-kde
#%find_lang kio_audiocd	--with-kde
#%find_lang kmid	--with-kde
%find_lang kmix		--with-kde
#%find_lang kmixcfg	--with-kde
#%find_lang kscd		--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	libkcddb		-p /sbin/ldconfig
%postun	libkcddb		-p /sbin/ldconfig

%post	audiocd		-p /sbin/ldconfig
%postun	audiocd		-p /sbin/ldconfig

%files libkcddb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkcddb.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libkcddb.so.?

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%{_includedir}/libkcddb
%{_includedir}/libkcompactdisc
%attr(755,root,root) %{_libdir}/libaudiocdplugins.so
%attr(755,root,root) %{_libdir}/libkcompactdisc.so
%attr(755,root,root) %{_libdir}/libkcddb.so

%files audiocd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kcm_audiocd.so
%attr(755,root,root) %{_libdir}/kde4/kio_audiocd.so
%attr(755,root,root) %{_libdir}/kde4/libaudiocd_encoder*.so
%attr(755,root,root) %{_libdir}/libaudiocdplugins.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libaudiocdplugins.so.?
%attr(755,root,root) %{_libdir}/libkcompactdisc.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libkcompactdisc.so.?
%{_datadir}/apps/kconf_update/upgrade-metadata.sh
%{_datadir}/config.kcfg/audiocd_*_encoder.kcfg
%{_datadir}/apps/kconf_update/audiocd.upd
%{_datadir}/kde4/services/audiocd.protocol
%{_datadir}/kde4/services/audiocd.desktop
%{_datadir}/apps/solid/actions/solid_audiocd.desktop
%lang(en) %{_kdedocdir}/en/kioslave/audiocd

%files cddb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kcm_cddb.so
%{_datadir}/config.kcfg/libkcddb.kcfg
%{_datadir}/apps/kconf_update/kcmcddb-emailsettings.upd
%{_datadir}/kde4/services/libkcddb.desktop

%files dragon
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dragon
%attr(755,root,root) %{_libdir}/kde4/dragonpart.so
%{_datadir}/apps/dragonplayer
%{_datadir}/apps/solid/actions/dragonplayer-opendvd.desktop
%{_datadir}/apps/konqsidebartng/virtual_folders/services/audiocd.desktop
%{_datadir}/config/dragonplayerrc
%{_datadir}/kde4/services/ServiceMenus/dragonplayer_play_dvd.desktop
%{_datadir}/kde4/services/dragonplayer_part.desktop
%{_desktopdir}/kde4/dragonplayer.desktop
%{_iconsdir}/*/*/apps/dragonplayer.png
%{_iconsdir}/*/*/actions/player-volume-muted.png
# FIXME: add -svg-icons subpackage like in kdebase-workspace and put the icons there
#%{_iconsdir}/*/scalable/actions/player-volume-muted.svgz
#%{_iconsdir}/hicolor/scalable/apps/dragonplayer.svgz
%lang(en) %{_kdedocdir}/en/dragonplayer

%files juk -f juk.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/juk
%{_datadir}/apps/juk
%{_datadir}/kde4/services/ServiceMenus/jukservicemenu.desktop
%{_desktopdir}/kde4/juk.desktop
%{_iconsdir}/*/*/*/juk*.png
%{_datadir}/dbus-1/interfaces/org.kde.juk.collection.xml
%{_datadir}/dbus-1/interfaces/org.kde.juk.player.xml
%{_datadir}/dbus-1/interfaces/org.kde.juk.search.xml

%files kmix -f kmix.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmix
%attr(755,root,root) %{_bindir}/kmixctrl
%attr(755,root,root) %{_libdir}/libkdeinit4_kmix.so
%attr(755,root,root) %{_libdir}/libkdeinit4_kmixctrl.so
%attr(755,root,root) %{_libdir}/kde4/kded_kmixd.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_mixer.so
%{_datadir}/apps/kmix
%{_datadir}/apps/plasma/services/mixer.operations
%{_datadir}/autostart/restore_kmix_volumes.desktop
%{_datadir}/autostart/kmix_autostart.desktop
%{_datadir}/kde4/services/kmixctrl_restore.desktop
%{_datadir}/kde4/services/kded/kmixd.desktop
%{_datadir}/kde4/services/plasma-engine-mixer.desktop
%{_desktopdir}/kde4/kmix.desktop
%{_iconsdir}/*/*/*/kmix.png
%{_datadir}/dbus-1/interfaces/org.kde.kmix.*.xml

%files kscd
# -f kscd.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kscd
%{_desktopdir}/kde4/kscd.desktop
%{_datadir}/config.kcfg/kscd.kcfg
%{_datadir}/apps/solid/actions/kscd-play-audiocd.desktop
%{_datadir}/apps/kscd
%{_iconsdir}/hicolor/*/apps/kscd.png
%{_iconsdir}/oxygen/*/actions/kscd-dock.png
%{_datadir}/dbus-1/interfaces/org.kde.kscd.cdplayer.xml

%files mplayerthumbs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mplayerthumbsconfig
%attr(755,root,root) %{_libdir}/kde4/videopreview.so
%{_datadir}/apps/videothumbnail
%{_datadir}/config.kcfg/mplayerthumbs.kcfg
%{_datadir}/kde4/services/videopreview.desktop

%files ffmpegthumbs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/ffmpegthumbs.so
%{_datadir}/kde4/services/ffmpegthumbs.desktop
