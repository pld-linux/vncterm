Summary:	LinuxVNC - VNC terminal using LibVNCServer library
Summary(pl.UTF-8):	LinuxVNC - terminal VNC wykorzystujący bibliotekę LibVNCServer
Name:		vncterm
Version:	0.9.10
Release:	1
License:	GPL v2
Group:		Applications/Graphics
#Source0Download: https://github.com/LibVNC/vncterm/releases
Source0:	https://github.com/LibVNC/vncterm/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	9aec637912e56f8fc03b61bb6398e9a1
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
%setup -q

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
