Gem::Specification.new do |spec|
  spec.name          = "jekyll-rtd-theme"
  spec.version       = "2.0.6"
  spec.authors       = ["saowang"]
  spec.email         = ["saowang@outlook.com"]

  spec.summary       = "Opinionated github flavored standard document theme for open source projects, with few options, but everything!"
  spec.license       = "MIT"
  spec.homepage      = "https://github.com/rundocs/jekyll-rtd-theme"

  spec.files         = `git ls-files -z`.split("\x0").select { |f| f.match(%r!^(assets|_layouts|_includes|_sass|LICENSE|README)!i) }

  spec.add_runtime_dependency "github-pages", "~> 207"
end
