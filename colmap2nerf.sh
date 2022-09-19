cd ~/github/instant-ngp/scripts

python colmap2nerf.py \
  --aabb_scale 16 \
  --images /home/chli/chLi/NeRF/keyboard/images \
  --text /home/chli/chLi/NeRF/keyboard/colmap/0 \
  --out /home/chli/chLi/NeRF/keyboard/transform.json

