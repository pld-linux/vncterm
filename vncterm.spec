Summary:	LinuxVNC - VNC terminal using LibVNCServer library
Summary(pl.UTF-8):	LinuxVNC - terminal VNC wykorzystujący bibliotekę LibVNCServer
Name:		vncterm
Version:	0.1
Release:	0.20140910.1
License:	GPL v2
Group:		Applications
%define	gitref	bedac42b4861138526304f913ca42cc9f1b3baef
Source0:	https://github.com/LibVNC/vncterm/archive/%{gitref}/%{name}-%{gitref}.tar.gz
# Source0-md5:	0a4cbc01137228b8541769dd6401ce2d
URL:		https://github.com/LibVNC/vncterm/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libvncserver-devel >= 0.9.8
BuildRequires:	pkgconfig
Requires:	libvncserver >= 0.9.8
Obsoletes:	libvncserver-progs < 0.9.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LinuxVNC - VNC terminal using LibVNCServer library.

%description -l pl.UTF-8
LinuxVNC - terminal VNC wykorzystujący bibliotekę LibVNCServer.

%prep
%setup -q -n vncterm-%{gitref}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/linuxvnc
