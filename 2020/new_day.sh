echo "Setting up new day $1"
mkdir "$1"
cd "$1"
cp ../utils/template_script.py ./script.py
touch data.txt
touch example.txt
cd ..
echo "Setup complete"