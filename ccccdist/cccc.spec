Name:           cccc
Version:        3.2.1
Release:        1
License:        GPL
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  make, gcc, glibc-devel, gcc-c++, bison
BuildRequires:  libstdc++6, libstdc++-devel


Group:          Development/Languages/C and C++
Summary:        C and C++ Code Counter
Source:         cccc-%{version}.tar.gz

%description
CCCC is a tool which analyzes C++ and Java files and generates a report
on various metrics of the code. Metrics supported include 
lines of code, McCabe's complexity and metrics i
proposed by Chidamber&Kemerer and Henry&Kafura.

%prep
%setup -q

%build
make DESTDIR=%{buildroot}

%install

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%{_bindir}/*

%changelog
* Wed Apr 24 2013 Jan Ruzicka <jan.ruzicka[AT]comtechmobile.com> 3.2.1-1
- Initial RPM setup copied and modified from opensuse.org
