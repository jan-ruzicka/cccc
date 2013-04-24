Name:           cccc
Version:        3.2.1
Release:        1
License:        GPL
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  make, gcc, glibc-devel, gcc-c++, bison
BuildRequires:  libstdc++, libstdc++-devel


Group:          Development/Languages/C and C++
Summary:        C and C++ Code Counter
Source:         http://github.com/jan-ruzicka/cccc/archive/%{name}-%{version}.tar.gz

%description
CCCC is a tool which analyzes C++ and Java files and generates a report
on various metrics of the code. Metrics supported include 
lines of code, McCabe's complexity and metrics i
proposed by Chidamber&Kemerer and Henry&Kafura.

%prep
%setup -q

%build
cd ccccdist
cd pccts 
make clean
make
cd ..

cd cccc
make -f posixgcc.mak clean
make -f posixgcc.mak 
cd ..

cd test
make -f posix.mak 
cd ..


%install
install -d ${RPM_BUILD_ROOT}%{_bindir}
install ccccdist/cccc/cccc ${RPM_BUILD_ROOT}%{_bindir}

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%{_bindir}/*

%changelog
* Wed Apr 24 2013 Jan Ruzicka <jan.ruzicka[AT]comtechmobile.com> 3.2.1-1
- Initial RPM setup copied and modified from opensuse.org
