cd _shared
./upload.bat
cd ../

git config --local user.name "PosetMage"
git config --local user.email "PosetMage@gmail.com"
git remote set-url origin git@POM:posetmage/Blog.git

git submodule update --recursive --remote

git pull
git add .
git commit -m "all"
git push