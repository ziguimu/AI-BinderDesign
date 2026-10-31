#!/bin/bash


BASE=/mnt/d/PRP/prediction_controls

MODEL="alphafold2_multimer_v3"

echo "===== Start prediction controls ====="

run_colabfold () {

NAME=$1
SEED=$2

INPUT=$BASE/$NAME/EGFR_DIII_${NAME}.fasta
OUT=$BASE/$NAME/run_${SEED}/colabfold

echo "===== Start ${NAME} run_${SEED} ====="

mkdir -p $OUT

colabfold_batch \
--model-type $MODEL \
--num-models 3 \
--random-seed $SEED \
$INPUT \
$OUT

echo "===== Finished ${NAME} run_${SEED} ====="

}


# ==========================
# 7D12 control
# ==========================

for seed in 1 2 3
do
run_colabfold 7D12 $seed
done


# ==========================
# EGF control
# ==========================

for seed in 1 2 3
do
run_colabfold EGF $seed
done


# ==========================
# cetuximab control
# ==========================

for seed in 1 2 3
do
run_colabfold cetuximab $seed
done


echo "===== ALL DONE ====="
