# (tpg) optimize it a bit
%global optflags %optflags -Ofast

Name:		lzip
Summary:	Lossless file compressor based on the LZMA algorithm
Version:	1.25
Release:	1
Source0:	https://nongnu.askapache.com/lzip/%{name}-%{version}.tar.gz
Group:		Archiving/Compression
URL:		https://www.nongnu.org/lzip/lzip.html
License:	GPLv3+

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
%autosetup -p1

%build
%configure CXXFLAGS="%{optflags}" LDFLAGS="%{ldflags}"
%make_build CXX=%{__cxx}

%install
%make_install

%files
%doc AUTHORS COPYING NEWS README ChangeLog
%{_bindir}/%{name}
%{_infodir}/%{name}.info*
%{_mandir}/man1/%{name}.1*
