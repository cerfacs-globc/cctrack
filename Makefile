LIBDIR=/opt/local/lib
INCDIR=/opt/local/include
DESTLIBDIR=.
BINDIR=../bin

FORTRAN=gfortran

NETCDF=netcdff
OPTFLAGS=-O2 -cpp -ffixed-line-length-132 -DNETCDF

make_tracks.abs: make_tracks.ftn libtracks.a libtracks_tools.a libstd_nc.a libarmnlib.a libezscint.a tracks_cte.h
	mkdir -p $(BINDIR)
	$(FORTRAN) make_tracks.ftn $(OPTFLAGS) -o $(BINDIR)/make_tracks.abs -L$(DESTLIBDIR) -L$(LIBDIR) -I. -I$(INCDIR) -ltracks -ltracks_tools -lstd_nc -larmnlib -lezscint -l$(NETCDF)
	rm -f make_tracks.o

libtracks.a: libtracks.ftn tracks_cte.h
	mkdir -p $(DESTLIBDIR)
	rm -f $(DESTLIBDIR)/libtracks.a 
	ar rv $(DESTLIBDIR)/libtracks.a libtracks.o
	ranlib $(DESTLIBDIR)/libtracks.a 
	rm -f libtracks.o

libtracks_tools.a: libtracks_tools.ftn tracks_cte.h
	mkdir -p $(DESTLIBDIR)
	rm -f $(DESTLIBDIR)/libtracks_tools.a 
	ar rv $(DESTLIBDIR)/libtracks_tools.a libtracks_tools.o 
	ranlib $(DESTLIBDIR)/libtracks_tools.a 
	rm -f libtracks_tools.o

libarmnlib.a: armnlib/igaxg.o armnlib/xgaig.o armnlib/convip.o armnlib/incdat.o armnlib/moduledate.o armnlib/datec.o
	mkdir -p $(DESTLIBDIR)
	rm -f $(DESTLIBDIR)/libarmnlib.a
	ar rv $(DESTLIBDIR)/libarmnlib.a armnlib/*.o
	ranlib $(DESTLIBDIR)/libarmnlib.a 
	rm -f libarmnlib.o

libezscint.a:
	make -C armnlib/interp genlib

libstd_nc.a: libstd_nc.ftn tracks_cte.h
	mkdir -p $(DESTLIBDIR)
	rm -f $(DESTLIBDIR)/libstd_nc.a
	ar rv $(DESTLIBDIR)/libstd_nc.a libstd_nc.o
	ranlib $(DESTLIBDIR)/libstd_nc.a 
	rm -f libstd_nc.o

mt2gmt5: mt2gmt5.ftn
	mkdir -p $(BINDIR)
	$(FORTRAN) $(OPTFLAGS) mt2gmt5.ftn -o $(BINDIR)/mt2gmt5 -L$(LIBDIR) -I. -I$(INCDIR) -ltracks

.f.o:
	$(FORTRAN) $(OPTFLAGS) -c $< -o $@

.ftn.o:
	$(FORTRAN) $(OPTFLAGS) -I. -I$(INCDIR) -c $< -o $@
