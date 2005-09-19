Summary:	Convmv - convert filenames from one encoding to another
Name:		convmv
Version:	1.08
Release:	1
License:	GPL v2
Group:		Applications/File
Source0:	http://j3e.de/linux/convmv/%{name}-%{version}.tar.gz
# Source0-md5:	40707f82b1a9631fe715f68f94431d3a
URL:		http://j3e.de/linux/convmv/
BuildRequires:	perl-tools-pod
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convmv is meant to help convert a single filename, a directory tree and the contained files
or a whole filesystem into a different encoding. It just converts the filenames, not the
content of the files. A special feature of convmv is that it also takes care of symlinks,
also converts the symlink target pointer in case the symlink target is being converted, too.
All this comes in very handy when one wants to switch over from old 8-bit locales to UTF-8
locales. It is also possible to convert directories to UTF-8 which are already partly UTF-8
encoded. Convmv is able to detect if certain files are UTF-8 encoded and will skip them by
default. To turn this smartness off use the "--nosmart" switch.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS Changes TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1.gz
