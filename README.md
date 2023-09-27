# Instant NGP

## Source

```bash
https://github.com/NVlabs/instant-ngp
```

## Requirements

```bash
gcc-12 & g++-12
cuda-12.2
optix-8.0.0
```

and set

```bash
~/.zshrc
->
export OptiX_INSTALL_DIR=$HOME/NVIDIA-OptiX-SDK-8.0.0-linux64-x86_64/
```

## Install

```bash
conda create -n ingp python=3.11
conda activate ingp
./setup.sh
```

## Run

```bash
python convert.py
python demo.py
```

## Enjoy it~
