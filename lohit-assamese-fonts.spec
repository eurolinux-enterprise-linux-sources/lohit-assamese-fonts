%global fontname lohit-assamese
%global fontconf 65-0-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        2.5.3
Release:        2%{?dist}
Summary:        Free Assamese font

Group:          User Interface/X
License:        OFL
URL:            https://fedorahosted.org/lohit/
Source0:        https://fedorahosted.org/releases/l/o/lohit/%{fontname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: fontforge >= 20080429
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem
Obsoletes: lohit-fonts-common < %{version}-%{release}

%description
This package provides a free Assamese truetype/opentype font.


%prep
%setup -q -n %{fontname}-%{version} 

%build
make
mv 66-%{fontname}.conf 65-0-lohit-assamese.conf

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{fontconf} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}


%_font_pkg -f %{fontconf} *.ttf

%doc ChangeLog COPYRIGHT OFL.txt AUTHORS README ChangeLog.old


%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.5.3-2
- Mass rebuild 2013-12-27

* Thu Jan 31 2013 Pravin Satpute <psatpute@redhat.com> - 2.5.3-1
- Upstream release 2.5.3

* Thu Nov 22 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.2-1
- Upstream release 2.5.2 and spec file cleanup
- enabled autohinting in fontconfig file

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 25 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.1-2
- Resolved bug #803294

* Thu Mar 01 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.1-1
- Upstream new release 2.5.1

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 07 2011 Pravin Satpute <psatpute@redhat.com> - 2.5.0-1
- Upstream new release with relicensing to OFL

* Wed Apr 13 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.3-9
- fixes bug 705348
- patch for correcting fsf address

* Wed Apr 13 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.3-8
- fixes bug 692359

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 04 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.3-6
- fixes bug 673411

* Wed May 12 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.3-5
- fixes bug 586308

* Thu Apr 15 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.3-4
- fixes bug 578029

* Thu Dec 24 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-3
- fixes bug 548686 and 549319

* Fri Sep 25 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-2
- updated specs

* Wed Sep 09 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-1
- first release after lohit-fonts split in new tarball
