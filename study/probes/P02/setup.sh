git init -q -b main && git config user.email t@example.org && git config user.name t
git add -A && git commit -qm init
git init -q --bare ../$(basename "$PWD")_origin.git && git remote add origin ../$(basename "$PWD")_origin.git
git push -q origin main
