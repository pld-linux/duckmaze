Summary:	Simple puzzle game written in Python
Summary(pl.UTF-8):	Prosta gra logiczna napisana w Pythonie
Name:		duckmaze
Version:	0.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/duckmaze/%{name}-pc-%{version}.zip
# Source0-md5:	acda6d78754a988846e313d3de7779d1
Patch0:		%{name}-import.patch
URL:		http://duckmaze.sourceforge.net/
BuildRequires:	python-pygame-devel
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
duckmaze is a game about a duck that is in a maze. The duck can move
walls, but only if there are no walls in the way.

It's a simple puzzle game which starts with easy levels but progresses
to some quite tricky ones.

%description -l pl.UTF-8
duckmaze jest grą o kaczce w labiryncie. Kaczka może przesuwać
mury, ale tylko gdy na drodze nie znajdują się inne mury.

Jest to prosta gra logiczna, w której gracz zaczynając od prostych
poziomów przechodzi do coraz trudniejszych.

%prep
%setup -q -n %{name}-pc-%{version}
%patch0 -p1
%{__sed} -i -e 's@install_dir = "."@install_dir = "%{_datadir}/%{name}"@g' duckmaze.py

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

install duckmaze.py $RPM_BUILD_ROOT%{_bindir}/%{name}
install level_editor.py level.py version $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -r images levels mopelib $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{TODO.txt,index.html}
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
