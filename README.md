## Ansys Techcon 2022 - API Guidance and Best Practices

This repository contains the content for the API Guidance and Best Practices presentation.

These slides were generated using the [Ansys Beamer Template](https://github.com/ansys/beamer-template)

Excellent example API at [OpenAI API](https://openai.com/blog/openai-api/).

### Comments or Suggestions

Please feel free to point out any problems with this presentation by opening an [issue](https://github.com/ansys/techcon-2022-api-presentation/issues).

### View the Presentation

Visit [api_techcon_2022.pdf](https://ansys.github.io/techcon-2022-api-presentation/api_techcon_2022.pdf) to see the full generated presentation.

## Build it Yourself

Due to the usage of ttf fonts, this template requires [LuaTeX](https://www.luatex.org/).

On Linux (Debian) install with:

```
sudo apt update
sudo apt install -y latexmk texlive-luatex texlive-fonts-extra
```

On Windows, use a distribution like [MiKTeX](http://miktex.org/). See [Get LaTeX](https://www.latex-project.org/get/).


### Build

Clone this repository with:
```
git clone https://github.com/ansys/beamer-template/
cd beamer-template
```

Build with:

```
latexmk -pdflatex=lualatex -pdf sample.tex -interaction=nonstopmode -outdir=./build
```

Or simply:
```
make
```

This will output `sample.pdf` in the `build` directory. You can feel free to rename the main `sample.tex` file for your own presentation.
