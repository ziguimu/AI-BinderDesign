#!/bin/bash

echo "===== Start Boltz human controls ====="


echo "===== 7D12 human ====="

boltz predict \
Boltz/7D12_human/7D12.yaml \
--out_dir Boltz/7D12_human/result \
--use_msa_server \
--diffusion_samples 3


echo "===== EGF human ====="

boltz predict \
Boltz/EGF_human/EGF.yaml \
--out_dir Boltz/EGF_human/result \
--use_msa_server \
--diffusion_samples 3


echo "===== cetuximab human ====="

boltz predict \
Boltz/cetuximab_human/cetuximab.yaml \
--out_dir Boltz/cetuximab_human/result \
--use_msa_server \
--diffusion_samples 3


echo "===== Finished all Boltz human controls ====="
