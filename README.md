# Instant NGP Recon

## Install OptiX

follow the link to install OptiX

```bash
https://developer.nvidia.com/optix
```

and add

```bash
export OptiX_INSTALL_DIR=$HOME/NVIDIA-OptiX-SDK-<your-optix-version>/
```

to $HOME/.zshrc

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
