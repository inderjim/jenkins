if [ ! -d "my-venv" ]; then
apt install pipx
python -m venv my-venv
my-venv/bin/pip install conan
fi

rm -rf build
./my-venv/bin/conan build .
./build/Release/common/demo
