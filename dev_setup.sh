cd ..
git clone git@github.com:565353780/colmap-manage.git
git clone https://ceres-solver.googlesource.com/ceres-solver
git clone --recursive https://github.com/nvlabs/instant-ngp

sudo apt install \
	git cmake build-essential libboost-program-options-dev libboost-filesystem-dev \
	libboost-graph-dev libboost-system-dev libboost-test-dev libeigen3-dev \
	libsuitesparse-dev libfreeimage-dev libmetis-dev libgoogle-glog-dev libgflags-dev \
	libglew-dev qtbase5-dev libqt5opengl5-dev libcgal-dev

sudo apt install \
	build-essential git python3-dev python3-pip libopenexr-dev libxi-dev \
	libglfw3-dev libglew-dev libomp-dev libxinerama-dev libxcursor-dev

sudo apt install libcgal-qt5-dev

sudo apt-get install libatlas-base-dev libsuitesparse-dev

pip install opencv-python tqdm

cd colmap-manage
./dev_setup.sh

cd ceres-solver
git checkout $(git describe --tags)
mkdir build
cd build
cmake .. -DBUILD_TESTING=OFF -DBUILD_EXAMPLES=OFF
make -j
sudo make install
cd ../..

cd instant-ngp
cmake . -B build
cmake --build build --config RelWithDebInfo -j
cd ..
