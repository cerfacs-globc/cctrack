#!/bin/sh
#
level=$1
area=$2
infile=$3
workdir=$4
outdir=$5
basemapdir=$6

export GMTPROJ="-Js0.0/90.0/5.3i/60.0 -R-34.0/17.0/78.0/59.0r"
export LEGPOS="-34/17"
export TIMPOS="25.0 20.0"

if [ $level = 1000 ]
then
    ldir=$workdir
    if [ "$area" = "EUR" ]
    then
	carte=$workdir/eur_last${tagmap}_pres
        carte_web=$outdir/eur_last${tagmap}_pres
    else
	carte=$workdir/na_last${tagmap}_pres
	carte_web=$outdir/na_last${tagmap}_pres
    fi
    form="c"
    s1=0.25
    s2=0.30
    s3=0.35
    s4=0.40
    s5=0.45
else
    ldir=$workdir/500hpa
    if [ "$area" = "EUR" ]
    then
	carte=$workdir/eur500_last${tagmap}
	carte_web=$outdir/eur500_last${tagmap}
    else
	carte=$workdir/na500_last${tagmap}
        carte_web=$outdir/na500_last${tagmap}
    fi
    form="d"
    s1=0.38
    s2=0.45
    s3=0.52
    s4=0.59
    s5=0.66
fi

rm -f ${carte}*

cd $workdir

gmtset FONT_ANNOT_PRIMARY 14p,Helvetica MAP_ORIGIN_X 0 MAP_ORIGIN_Y 0 PS_MEDIA 11x17 PS_CHAR_ENCODING ISOLatin1+

if [ "$area" = "EUR" ]
then
    cp ${basemapdir}/EUROPE/mapfond_topo_eur.ps ${carte}.ps
else
    cp ${basemapdir}/mapfond_topo_na.ps ${carte}.ps
fi


cnt=1
cntmax=`awk 'END {print $1}' ${infile}`
echo "Il y a $cntmax trajectoires"

cnt2tot=1

while [ $cnt -le $cntmax ]
do

cnt2=1
cnt2max=`awk "\\$1 == $cnt {total++} END {print total}" ${infile}`
echo "Traj $cnt a $cnt2max points"

while [ $cnt2 -le $cnt2max ]
do

    lpf=`awk "FNR==$cnt2tot {print \\$5}" ${infile}`
    lp=`echo $lpf | awk '{print int($1+0.5)}'`
    hh=`awk "FNR==$cnt2tot {print \\$6}" ${infile}`
    lat=`awk "FNR==$cnt2tot {print \\$2}" ${infile}`
    lon=`awk "FNR==$cnt2tot {print \\$3}" ${infile}`

    if [ $lp -ge 1010 ]; then
	color=skyblue
    elif [ $lp -ge 1000 ]; then
	color=green
    elif [ $lp -ge 990 ]; then
	color=yellow
    elif [ $lp -ge 980 ]; then
	color=orange
    elif [ $lp -ge 970 ]; then
	color=red
    elif [ $lp -ge 960 ]; then
        color=magenta
    else
	color=white
    fi

    if [ $lp -ge 1000 ]; then
	lpa=`echo $lp | cut -c3-4`
    else
	lpa=`echo $lp | cut -c2-3`
    fi
    
    if [ $cnt2 -ne $cnt2max ]; then
        awk "FNR==$cnt2tot {print \$2,\$3,\$4,\$5,\$6,\$7,\$8,\$9}" ${infile} > temp.txt
	ll=`expr $cnt2tot + 1`
        awk "FNR==$ll {print \$2,\$3,\$4,\$5,\$6,\$7,\$8,\$9}" ${infile} >> temp.txt
	psxy temp.txt $GMTPROJ -:  -W2.0p,${color} -A -K -O >> ${carte}.ps
    fi

    if [ $hh = 0 ]
    then
     echo $lat $lon | psxy $GMTPROJ -:  -Sx0.2c -W0.75p,white  -K -O >> ${carte}.ps
    fi
    echo $lat $lon | psxy $GMTPROJ -:  -Sl0.35c+t"${lpa}" -G${color} -D0/0.4c -K -O >> ${carte}.ps
    echo "$lat $lon $cnt $cnt2 $cnt2tot"

# On ajoute la date d'apparition
    if [ $cnt2 -eq 1 ]
    then
      dd=`awk "FNR==$cnt2tot {print \\$8}" ${infile}`
      echo $lat $lon | psxy $GMTPROJ -:  -Sl0.4c+t"${dd}-${hh}z" -Gwhite -D0/-0.4c -K -O >> ${carte}.ps
    fi

    cnt2=`expr $cnt2 + 1`
    cnt2tot=`expr $cnt2tot + 1`
done
cnt=`expr $cnt + 1`
done

# Debut de la periode
#yyp=`r.date -n -L ${yyyy}${mm}${dd}${run} -$dt | head -1 | awk '{print $1}'`
#mmp=`r.date -n -L ${yyyy}${mm}${dd}${run} -$dt | head -1 | awk '{print $2}'`
#ddp=`r.date -n -L ${yyyy}${mm}${dd}${run} -$dt | head -1 | awk '{print $3}'`
#hhp=`r.date -n -L ${yyyy}${mm}${dd}${run} -$dt | head -1 | awk '{print $4}'`

#H 14 Helvetica Last ${tagtime}. From ${ddp}-${mmp}-${yyp}, ${run}z to ${dd}-${mm}-${yyyy}, ${run}z (every 6h)
#D 0.2i 0.5p

pslegend $GMTPROJ -D${LEGPOS}+w8.0i/1.0i+jBL -F1p+g255 -K -O << EOF >> ${carte}.ps
G -0.05i
H 14 Helvetica MSLP Cyclone Tracking (minimum central pressure) - http://meteocentre.com
D 0.2i 0.5p
N 7
S 0.1i s 0.15i white 0.25p 0.2i < 960 hPa
S 0.1i s 0.15i magenta 0.25p 0.2i 960-69
S 0.1i s 0.15i red 0.25p 0.2i 970-79
S 0.1i s 0.15i orange 0.25p 0.2i 980-89
S 0.1i s 0.15i yellow 0.25p 0.2i 990-99
S 0.1i s 0.15i green 0.25p 0.2i 1000-09
S 0.1i s 0.15i skyblue 0.25p 0.2i >= 1010
EOF

timestamp=`date +%H:%M:%Sz`
echo "$TIMPOS" | psxy $GMTPROJ -:  -Sl0.5c+t"$timestamp" -Ggrey -K -O >> ${carte}.ps

#sed -i '/GMTAPI/d' ${carte}.ps # PATCH POUR BOGUE ALEATOIRE DANS GMT4.5.7
convert -interlace none -density 72 -rotate 90 -trim +repage ${carte}.ps ${carte}.gif
