Summary:	lkmonitor - linux kernel monitor
Name:		lkmonitor
Version:	0.1
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/lkmonitor/%{name}-%{version}.tar.gz
# Source0-md5:	39740974aac73360e110d3e91985992c
URL:		http://lkmonitor.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libgnomeui-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lkmonitor is a tool for monitoring and managing linux's kernel. It has
been developed for GNOME, using Glib and Gtk libraries in C Language.
lkmonitor tries to offer detailed information about the
characteristics of the system, such as types of cpu, state of the
memory and/or the file system registered in kernel.

%prep
%setup -q

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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/lkmonitor
%{_desktopdir}/*
%{_pixmapsdir}/*
