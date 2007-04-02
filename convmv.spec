Summary:	Convmv - convert filenames from one encoding to another
Summary(pl.UTF-8):	Convmv - konwersja nazw plików z jednego kodowania do innego
Name:		convmv
Version:	1.10
Release:	1
License:	GPL v2
Group:		Applications/File
Source0:	http://j3e.de/linux/convmv/%{name}-%{version}.tar.gz
# Source0-md5:	8daf88557f40523312c40abc31b8167f
URL:		http://j3e.de/linux/convmv/
BuildRequires:	perl-tools-pod
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convmv is meant to help convert a single filename, a directory tree
and the contained files or a whole filesystem into a different
encoding. It just converts the filenames, not the content of the
files. A special feature of convmv is that it also takes care of
symlinks, also converts the symlink target pointer in case the symlink
target is being converted, too. All this comes in very handy when one
wants to switch over from old 8-bit locales to UTF-8 locales. It is
also possible to convert directories to UTF-8 which are already partly
UTF-8 encoded. Convmv is able to detect if certain files are UTF-8
encoded and will skip them by default. To turn this smartness off use
the "--nosmart" switch.

%description -l pl.UTF-8
Convmv ma za zadanie pomóc przy konwersji pojedynczych nazw plików,
drzew katalogów wraz z zawartymi w nich plikami lub całego systemu
plików na inne kodowanie. Konwertuje tylko nazwy plików, a nie ich
zawartość. Szczególną cechą convmv jest to, że dba także o dowiązania
symboliczne i konwertuje wskazania docelowe w przypadku, gdy cel
dowiązania jest zmieniany. Jest to pomocne przy przechodzeniu ze
starych 8-bitowych lokalizacji do nowych w UTF-8. Można także
przekonwertować do UTF-8 katalogi, które były już częściowo kodowane w
UTF-8. Convmv jest w stanie wykryć, czy dane pliki są zakodowane w
UTF-8 i domyślnie je pominąć. Aby wyłączyć to zachowanie można użyć
przełącznika "--nosmart".

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
%{_mandir}/man1/*.1*
