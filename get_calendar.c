/* ***************************************************** */
/* Get year,month,day,hour,min,sec given time in udunits */
/* get_calendar.c                                        */
/* ***************************************************** */
/* Author: Christian Page, CERFACS, Toulouse, France.    */
/* ***************************************************** */
/*! \file get_calendar.c
    \brief Get year,month,day,hour,min,sec given time in udunits.
*/

/* LICENSE BEGIN

Copyright Cerfacs (Christian Page) (2015)

christian.page@cerfacs.fr

This software is a computer program whose purpose is to downscale climate
scenarios using a statistical methodology based on weather regimes.

This software is governed by the CeCILL license under French law and
abiding by the rules of distribution of free software. You can use, 
modify and/ or redistribute the software under the terms of the CeCILL
license as circulated by CEA, CNRS and INRIA at the following URL
"http://www.cecill.info". 

As a counterpart to the access to the source code and rights to copy,
modify and redistribute granted by the license, users are provided only
with a limited warranty and the software's author, the holder of the
economic rights, and the successive licensors have only limited
liability. 

In this respect, the user's attention is drawn to the risks associated
with loading, using, modifying and/or developing or reproducing the
software by the user in light of its specific status of free software,
that may mean that it is complicated to manipulate, and that also
therefore means that it is reserved for developers and experienced
professionals having in-depth computer knowledge. Users are therefore
encouraged to load and test the software's suitability as regards their
requirements in conditions enabling the security of their systems and/or 
data to be ensured and, more generally, to use and operate it in the 
same conditions as regards security. 

The fact that you are presently reading this means that you have had
knowledge of the CeCILL license and that you accept its terms.

LICENSE END */

#include <udunits.h>

/** TRUE value macro is 1. */
#define TRUE 1
/** FALSE value macro is 0. */
#define FALSE 0

int get_calendar_(int *year, int *month, int *day, int *hour, int *minutes, double *seconds, char *tunits, double *timein, int *ntime);

/** Get year,month,day,hour,min,sec given time in udunits. */
int
get_calendar_(int *year, int *month, int *day, int *hour, int *minutes, double *seconds, char *tunits, double *timein, int *ntime) {

  /** 
      @param[out]  year       Year vector
      @param[out]  month      Month vector
      @param[out]  day        Day vector
      @param[out]  hour       Hour vector
      @param[out]  minutes    Minutes vector
      @param[out]  seconds    Seconds vector
      @param[out]  tunits     Time units (udunits)
      @param[in]   timein     Input time vector values
      @param[in]   ntime      Number of times
   */

  int t; /* Time loop counter */
  int istat; /* Diagnostic status */

  ut_system *unitSystem = NULL; /* Unit System (udunits) */
  ut_unit *dataunits = NULL; /* udunits variable */

  double res;

  /* Initialize udunits */
  ut_set_error_message_handler(ut_ignore);
  unitSystem = ut_read_xml(NULL);
  ut_set_error_message_handler(ut_write_to_stderr);
  dataunits = ut_parse(unitSystem, tunits, UT_ASCII);
  
  /* Loop over times and retrieve day, month, year */
  for (t=0; t<(*ntime); t++)
    (void) ut_decode_time(timein[t], &(year[t]), &(month[t]), &(day[t]), &(hour[t]), &(minutes[t]), &(seconds[t]), &res);
  
  /* Terminate udunits */
  (void) ut_free(dataunits);
  (void) ut_free_system(unitSystem);

  /* Success status */
  return 0;
}
