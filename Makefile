LIBDIR=../bin
INCDIR=.
BINDIR=../bin

RMN=rmn 
OPTFLAGS=-O 2

make_tracks.abs: make_tracks.ftn libtracks.a libtracks_tools.a tracks_cte.h
	mkdir -p $(BINDIR)
	. ssmuse-sh -d hpcs/201402/02/base -d hpcs/201402/02/intel13sp1u2 -d rpn/libs/15.2;\
	s.compile -src make_tracks.ftn -o $(BINDIR)/make_tracks.abs -includes $(INCDIR) -librmn $(RMN) $(OPTFLAGS) -libpath $(LIBDIR) -libappl "tracks tracks_tools"
	rm -f make_tracks.f make_tracks.o
	rm -rf .fo

libtracks.a: libtracks.ftn tracks_cte.h
	mkdir -p $(LIBDIR)
	. ssmuse-sh -d hpcs/201402/02/base -d hpcs/201402/02/intel13sp1u2 -d rpn/libs/15.2;\
	s.compile -src libtracks.ftn -librmn $(RMN) -includes $(INCDIR) 
	rm -f $(LIBDIR)/libtracks.a 
	ar rv $(LIBDIR)/libtracks.a libtracks.o 
	ranlib $(LIBDIR)/libtracks.a 
	rm -f libtracks.o libtracks.f 

libtracks_tools.a: libtracks_tools.ftn tracks_cte.h
	mkdir -p $(LIBDIR)
	. ssmuse-sh -d hpcs/201402/02/base -d hpcs/201402/02/intel13sp1u2 -d rpn/libs/15.2;\
	s.compile -src libtracks_tools.ftn -librmn $(RMN) -includes $(INCDIR) 
	rm -f $(LIBDIR)/libtracks_tools.a 
	ar rv $(LIBDIR)/libtracks_tools.a libtracks_tools.o 
	ranlib $(LIBDIR)/libtracks_tools.a 
	rm -f libtracks_tools.o libtracks_tools.f 

mt2gmt5: mt2gmt5.ftn
	mkdir -p $(BINDIR)
	. ssmuse-sh -d hpcs/201402/02/base -d hpcs/201402/02/intel13sp1u2 -d rpn/libs/15.2;\
	s.compile -src mt2gmt5.ftn -o $(BINDIR)/mt2gmt5 -includes $(INCDIR) -librmn $(RMN) $(OPTFLAGS) -libpath $(LIBDIR) -libappl "tracks"
	rm -f mt2gmt5.f mt2gmt5.o
