echo "Setting up new day $1/$2"
cd "$1"
mkdir "$2"
cd "$2"
cp ../../utils/template_script.py ./script.py
touch data.txt
touch example.txt
echo "Setup of $1/$2 complete"