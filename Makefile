LIBDIR=/opt/local/lib
INCDIR=/opt/local/include
DATETIMELIBDIR=./lib
DATETIMEINCDIR=./include
UDUNITSLIBDIR=/opt/local/lib
UDUNITSINCDIR=/opt/local/include/udunits2
DESTLIBDIR=.
BINDIR=../bin

FORTRAN=gfortran
CC=gcc

NETCDF=netcdff
OPTFLAGS=-O2 -cpp -ffixed-line-length-132 -DNETCDF
CFLAGS=-O2

.SUFFIXES: .ftn

make_tracks.abs: make_tracks.ftn libtracks.a libtracks_tools.a libstd_nc.a tracks_cte.h
	mkdir -p $(BINDIR)
	$(FORTRAN) make_tracks.ftn $(OPTFLAGS) -o $(BINDIR)/make_tracks.abs -L$(DESTLIBDIR) -L$(LIBDIR) -L$(DATETIMELIBDIR) -L$(UDUNITSLIBDIR) -I. -I$(INCDIR) -I$(DATETIMEINCDIR) -I$(UDUNITSINCDIR) get_calendar.o -ltracks -ltracks_tools -lstd_nc -l$(NETCDF) -ldatetime -ludunits2
	rm -f make_tracks.o

libtracks.a: libtracks.ftn tracks_cte.h libtracks.o
	mkdir -p $(DESTLIBDIR)
	rm -f $(DESTLIBDIR)/libtracks.a 
	ar rv $(DESTLIBDIR)/libtracks.a libtracks.o
	ranlib $(DESTLIBDIR)/libtracks.a 
	rm -f libtracks.o

libtracks_tools.a: libtracks_tools.ftn tracks_cte.h libtracks_tools.o get_calendar.c get_calendar.o
	mkdir -p $(DESTLIBDIR)
	rm -f $(DESTLIBDIR)/libtracks_tools.a 
	ar rv $(DESTLIBDIR)/libtracks_tools.a libtracks_tools.o 
	ranlib $(DESTLIBDIR)/libtracks_tools.a 
	rm -f libtracks_tools.o

libstd_nc.a: libstd_nc.ftn tracks_cte.h libstd_nc.o
	mkdir -p $(DESTLIBDIR)
	rm -f $(DESTLIBDIR)/libstd_nc.a
	ar rv $(DESTLIBDIR)/libstd_nc.a libstd_nc.o
	ranlib $(DESTLIBDIR)/libstd_nc.a 
	rm -f libstd_nc.o

mt2gmt5: mt2gmt5.ftn
	mkdir -p $(BINDIR)
	$(FORTRAN) $(OPTFLAGS) mt2gmt5.ftn -o $(BINDIR)/mt2gmt5 -L$(LIBDIR) -I. -I$(INCDIR) -ltracks

get_calendar.o: get_calendar.c
	$(CC) $(CFLAGS) -I. -I$(INCDIR) -I$(UDUNITSINCDIR) -c get_calendar.c -o get_calendar.o

.f.o:
	$(FORTRAN) $(OPTFLAGS) -c $< -o $@

.ftn.o:
	$(FORTRAN) $(OPTFLAGS) -I. -I$(INCDIR) -I$(DATETIMEINCDIR) -c $< -o $@

.c.o:
	$(CC) $(CFLAGS) -I. -I$(INCDIR) -c $< -o $@
