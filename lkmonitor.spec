Summary:	lkmonitor - Linux kernel monitor
Summary(pl.UTF-8):	lkmonitor - monitor jądra Linuksa
Name:		lkmonitor
Version:	0.3
Release:	4
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/lkmonitor/%{name}-%{version}.tar.gz
# Source0-md5:	dd84ee3952fc03ee8319658dc3866e3c
Patch0:		%{name}-pixmapsdir.patch
Patch1:		%{name}-locale.patch
Patch2:		%{name}-pixmaps.patch
Patch3:		%{name}-desktop.patch
URL:		http://lkmonitor.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	libgnomeui-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lkmonitor is a tool for monitoring and managing Linux kernel. It has
been developed for GNOME, using Glib and GTK+ libraries in C Language.
lkmonitor tries to offer detailed information about the
characteristics of the system, such as types of CPU, state of the
memory and/or the file system registered in kernel.

%description -l pl.UTF-8
lkmonitor to narzędzie do monitorowania i zarządzania jądrem Linuksa.
Zostało stworzone dla GNOME, przy użyciu bibliotek Glib i GTK+, w
języku C. lkmonitor próbuje dostarczyć szczegółowe informacje o
charakterystyce systemu, takie jak rodzaj procesora, stan pamięci czy
systemy plików zarejestrowane w jądrze.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
for i in po/es_ES.*; do mv "$i" `echo "$i" | sed 's/es_ES\./es\./'`; done
for i in po/zh.*; do mv "$i" `echo "$i" | sed 's/zh\./zh_CN\./'`; done
mv pixmaps/gnome-computer.png pixmaps/gnome-workstation.png
mv pixmaps/gnome-ccperiph.png pixmaps/gnome-ccperiph-lkm.png

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}/* $RPM_BUILD_ROOT%{_pixmapsdir}
mv -f $RPM_BUILD_ROOT%{_datadir}/gnome/apps/Applications/* $RPM_BUILD_ROOT%{_desktopdir}
rm -rf $RPM_BUILD_ROOT/usr/doc/lkmonitor
rmdir $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/lkmonitor
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
