Name:		lzip
Summary:	Lossless file compressor based on the LZMA algorithm
Version:	1.15
Release:	1
Source0:	http://nongnu.askapache.com/lzip/%{name}-%{version}.tar.gz
Group:		Archiving/Compression
URL:		http://www.nongnu.org/lzip/lzip.html
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
%setup -q

%build
%configure2_5x CXXFLAGS="%{optflags}" LDFLAGS="%{ldflags}"
%make

%install
%makeinstall_std

%files
%doc AUTHORS COPYING NEWS README ChangeLog
%_bindir/%{name}
%_infodir/%{name}.info*
%_mandir/man1/%{name}.1*


%changelog
* Mon Mar 12 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.13-1
+ Revision: 784345
- version update 1.12

* Fri May 06 2011 Funda Wang <fwang@mandriva.org> 1.12-1
+ Revision: 670631
- new version 1.12

* Fri Oct 01 2010 Funda Wang <fwang@mandriva.org> 1.11-1mdv2011.0
+ Revision: 582373
- new version 1.11

* Sun Jul 18 2010 Funda Wang <fwang@mandriva.org> 1.10-1mdv2011.0
+ Revision: 554850
- New version 1.10

* Mon Jan 18 2010 Frederik Himpe <fhimpe@mandriva.org> 1.9-1mdv2010.1
+ Revision: 493243
- update to new version 1.9
- Fix source URL

* Sat Jan 02 2010 Frederik Himpe <fhimpe@mandriva.org> 1.8-1mdv2010.1
+ Revision: 485125
- Update to new version 1.8
- Use Mandriva CFLAGS

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Mar 20 2009 Nicolas Vigier <nvigier@mandriva.com> 1.4-1mdv2009.1
+ Revision: 359079
- version 1.4

* Fri Oct 17 2008 Nicolas Vigier <nvigier@mandriva.com> 1.0-1mdv2009.1
+ Revision: 294708
- import lzip

