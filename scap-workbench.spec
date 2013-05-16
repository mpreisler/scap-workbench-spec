Name:		scap-workbench
Version:	0.8.0
Release:	1%{?dist}
Summary:	Scanning, tailoring, editing and validation tool for SCAP content

License:	GPLv3+
URL:		https://fedorahosted.org/scap-workbench/
Source0:	https://fedorahosted.org/released/scap-workbench/%{name}-%{version}.tar.bz2

# --progress was added in 0.9.5
BuildRequires:	openscap-devel >= 0.9.5
Requires:		openscap-utils >= 0.9.5	

%description
scap-workbench is GUI tool that provides scanning, tailoring, 
editing and validation functionality for SCAP content. The tool 
is based on OpenSCAP library.

%prep
%setup -q

%build
%cmake .
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/scap_workbench
%{_mandir}/man8/scap_workbench.8.gz
%{_datadir}/pixmaps/scap_workbench.png

%changelog
* Thu May 15 2013 Martin Preisler <mpreisle@redhat.com> 0.8.0-1
- Initial release of the rewritten workbench
