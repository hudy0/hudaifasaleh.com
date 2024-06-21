## pygraphviz

1. First install if you are using `macOS`:
    ```
    brew install graphviz
    ```
2. install `pygraphviz` using pip in venv
    ```
    pip install pygraphviz
    ```

### note:

Graphviz may be installed in a location that is not on the default search path.
In this case, it may be necessary to manually specify the path to the
graphviz include and/or library directories

```
pip install --config-settings="--global-option=build_ext" \
--config-settings="--global-option=-I$(brew --prefix graphviz)/include/" \
--config-settings="--global-option=-L$(brew --prefix graphviz)/lib/" \
pygraphviz
``` 

See the [Advanced](https://pygraphviz.github.io/documentation/stable/install.html#advanced) section for details.

<br />

It is possible you can’t install it because it needs some C extensions to build.<br />
In that case you can try other methods to install, or you can use `pydot==2.0.0`
with the new macOS 15.<br /> it may not work
they do not provide support for this pre-release version.
