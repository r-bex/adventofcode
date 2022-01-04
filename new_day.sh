new_dir=solutions/$1/$2
echo "Setting up new day at $new_dir"
mkdir $new_dir
cp utils/template_script.py $new_dir/script.py
touch $new_dir/data.txt
touch $new_dir/example.txt
echo "Setup of $new_dir complete"
