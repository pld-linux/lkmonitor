Summary:	lkmonitor - Linux kernel monitor
Summary(pl.UTF-8):	lkmonitor - monitor jądra Linuksa
Name:		lkmonitor
Version:	0.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/lkmonitor/%{name}-%{version}.tar.gz
# Source0-md5:	1c017263dcd38c65453f2cbee3d36832
URL:		http://lkmonitor.sourceforge.net/
Patch0:		%{name}-pixmapsdir.patch
Patch1:		%{name}-locale.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libgnomeui-devel >= 2.0
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
for i in po/es_ES.*; do mv "$i" `echo "$i" | sed 's/es_ES\./es\./'`; done
for i in po/zh.*; do mv "$i" `echo "$i" | sed 's/zh\./zh_CN\./'`; done

%build
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
mv -f $RPM_BUILD_ROOT%{_datadir}/gnome/apps/System/* $RPM_BUILD_ROOT%{_desktopdir}
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
