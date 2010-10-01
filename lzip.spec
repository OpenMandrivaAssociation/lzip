Name:		lzip
Summary:	Lossless file compressor based on the LZMA algorithm
Version:	1.11
Release:	%mkrel 1
Source:		http://nongnu.askapache.com/lzip/%{name}-%{version}.tar.gz
Group:		Archiving/Compression
URL:		http://www.nongnu.org/lzip/lzip.html
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
%configure2_5x CXXFLAGS="%{optflags}" LDFLAGS="%{ldflags}"
%make

%install
%{__rm} -Rf %{buildroot}
%makeinstall_std

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
%_bindir/lziprecover

%_infodir/%{name}.info*
%_mandir/man1/%{name}.1*
%_mandir/man1/lziprecover.1*
