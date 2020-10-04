DEBUG=JEKYLL_GITHUB_TOKEN=blank PAGES_API_URL=http://0.0.0.0

help:
	@echo "jekyll-rtd-theme -- Opinionated github flavored standard document theme for open source projects, with few options, but everything!\n"
	@echo "Usage:"
	@echo "    make [subcommand]\n"
	@echo "Subcommands:"
	@echo "    install   Install the theme dependencies"
	@echo "    format    Format all files"
	@echo "    report    Make a report from Google lighthouse"
	@echo "    clean     Clean the workspace"
	@echo "    dist      Build the theme css and script"
	@echo "    status    Display status before push"
	@echo "    theme     Make theme as gem and install"
	@echo "    site      Build the test site"
	@echo "    server    Make a livereload jekyll server to development"
	@echo "    rouge     Build the rouge scss"
	@echo "    checkout  Reset the theme minified css and script to last commit"

checkout:
	@git checkout _config.yml
	@git checkout assets/js/theme.min.js
	@git checkout assets/css/theme.min.css

rouge:
	@rougify style github | sass-convert --to scss > _sass/rougify/github.scss

install:
	@gem install jekyll bundler
	@npm install
	@bundle install

format:
	@npm run checkout

report:
	@npm run report

clean:
	@bundle exec jekyll clean

dist: format clean
	@npm run build

status: format clean checkout
	@git status

theme: dist
	@gem uninstall jekyll-rtd-theme
	@gem build *.gemspec
	@gem install *.gem && rm -f *.gem

site: dist
	@${DEBUG} bundle exec jekyll build --safe --profile

server: dist
	@${DEBUG} bundle exec jekyll server --safe --livereload
