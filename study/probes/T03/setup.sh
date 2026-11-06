printf "downloads/\n" > .gitignore
git init -q -b main && git config user.email t@example.org && git config user.name t
git remote add origin https://github.com/example-org/grid-notes.git
git add -A && git commit -qm init
