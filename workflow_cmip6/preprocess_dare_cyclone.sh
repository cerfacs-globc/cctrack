#!/bin/bash
#
set -e

if [ -z "${RUN_DIR}" ]
then
  RUN_DIR=$$
fi

if [ ! -d /home/mpiuser/sfs ]
then
  mkdir -p /home/mpiuser/sfs
fi

cd /home/mpiuser/sfs/
mkdir -p cyclone

cd /home/mpiuser/sfs/cyclone
mkdir -p $RUN_DIR

WORKDIR="/home/mpiuser/sfs/cyclone/${RUN_DIR}"

tar -cf - -C /home/mpiuser/docker . | tar -xpf - -C ${WORKDIR}/.

cd $WORKDIR

OUTDIR="output"
mkdir -p ${OUTDIR}

bash -vx ${WORKDIR}/tracking/workflow_cmip6/tracking_master_cmip6.sh ${WORKDIR}/tracking/workflow_cmip6 ${WORKDIR}/${OUTDIR} ${WORKDIR}/tracking/workflow_cmip6/cyclone_config_CMIP6.json

