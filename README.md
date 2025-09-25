# Bulk converter Figma to Sketch for GitHub action

This is an experimental script to convert multiple Figma files to sketch
using parallel computation.

## Install in a virtual environment

Using a Python virtual environment with Rust and Cargo installed type

```sh
export PATH="$HOME/.cargo/bin:$PATH"
pip install "fig2sketch[fast]"
```