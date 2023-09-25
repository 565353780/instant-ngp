cd ..
git clone https://github.com/565353780/colmap-manage.git
git clone --recursive https://github.com/nvlabs/instant-ngp ingp

sudo apt-get install build-essential git python3-dev python3-pip libopenexr-dev libxi-dev \
	libglfw3-dev libglew-dev libomp-dev libxinerama-dev libxcursor-dev

cd colmap-manage
./setup.sh

cd ../ingp
cmake . -B build -DCMAKE_BUILD_TYPE=RelWithDebInfo
cmake --build build --config RelWithDebInfo -j
