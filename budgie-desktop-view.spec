Name:           budgie-desktop-view
Version:        1.2
Release:        1
Summary:        Budgie Desktop View is the official Budgie desktop icons application / implementation.
Group:          Graphical desktop/Budgie
License:        ASL 2.0
URL:            https://github.com/BuddiesOfBudgie/budgie-desktop-view
Source0:        https://github.com/BuddiesOfBudgie/budgie-desktop-view/releases/download/v%{version}/%{name}-v%{version}.tar.xz

BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gio-unix-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gdk-3.0) >= %{gtk3_version}
BuildRequires:  pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires:  pkgconfig(vapigen) >= %{vala_version}

Requires: glib2%{?_isa}
Requires: gtk+3%{?_isa}

%description
Budgie Desktop View is the official Budgie desktop icons application / implementation.

The scope of this project is to provide quick access to the content and applications you consider most important.
It is not designed to replace your file manager or to perform typical file manager actions.
Budgie Desktop View provides:
Options to enable and access "special" folders such as your Home directory and Trash.
Showing active drive / volume mounts (including mounted removable media).
An ordered list of Desktop directory contents, prioritizing folders before files while maintaining order of content that respects locales.
Independently adjustable icon sizing from your file manager
Right-click menu options for the background canvas to quickly access Budgie Desktop and System Settings, 
as well right-click menu options for opening a file using the default app, or via the Terminal.
Drag & Drop support. Copies files and symlink directories (to avoid the need for recursive copy functionality).
Keyboard-based navigation, including move-to-trash or cancel copy operation on use of delete key.
Budgie Desktop View is designed for the Budgie Desktop. Usage outside of Budgie is not supported and is outside this project's scope.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%license LICENSE.md
%{_bindir}/org.buddiesofbudgie.budgie-desktop-view
%{_datadir}/applications/org.buddiesofbudgie.budgie-desktop-view.desktop
%{_datadir}/glib-2.0/schemas/org.buddiesofbudgie.budgie-desktop-view.gschema.xml
%{_sysconfdir}/xdg/autostart/org.buddiesofbudgie.budgie-desktop-view-autostart.desktop
