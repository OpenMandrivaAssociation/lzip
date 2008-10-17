Name:		lzip
Summary:	Lossless file compressor based on the LZMA algorithm
Version:	1.0
Release:	%mkrel 1
Source:		http://es.geocities.com/ant_diaz2001/%{name}-%{version}.tar.gz
Group:		Archiving/Compression
URL:		http://es.geocities.com/ant_diaz2001/lzip.html
License:	GPLv3+
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
%description
Lzip is a lossless file compressor based on the LZMA (Lempel-Ziv-Markov
chain-Algorithm) algorithm. The high compression of LZMA comes from
combining two basic, well-proven compression ideas: sliding dictionaries
(i.e. LZ77/78), and markov models (i.e. the thing used by every
compression algorithm that uses a range encoder or similar order-0
entropy coder as its last stage) with segregation of contexts according
to what the bits are used for.

Lzip is not a replacement for gzip or bzip2, but a complement; which
one is best to use depends on user's needs. Gzip is the fastest and most
widely used. Bzip2 compresses better than gzip but is slower, both
compressing and decompressing. Lzip decompresses almost as fast as gzip
and compresses better than bzip2, but requires more memory and time
during compression. These features make lzip well suited for software
distribution and data archival.

%prep
%setup -q

%build
%{__rm} -Rf %{buildroot}
%configure
%make

%install
%{__rm} -Rf %{buildroot}
%makeinstall
%{__mkdir_p} %{buildroot}%{_mandir}/man1
%{__cp} -p doc/lzip.1 %{buildroot}%{_mandir}/man1/lzip.1

%clean
%{__rm} -Rf %{buildroot}

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%files
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README ChangeLog
%_bindir/%{name}
%_infodir/%{name}.info*
%_mandir/man1/%{name}.1*
