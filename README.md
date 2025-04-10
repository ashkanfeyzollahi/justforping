# Just For Ping

Imagine that you host your Discord bot or anything else on a free service that stops your bot after some inactivity, you use **uptimerobot** and maybe a minimal and light-weight web framework like **Flask** or **FastAPI** to keep your bot alive and running 24/7. This is a wrong approach though, you can instead use **justforping** instead of **Flask** and **FastAPI** since they are overpowered for this task and might use extra resources for just doing this task and make your bot slower.

### Why *justforping*?

I personally recommend using **justforping** since it is fast, light-weight, independent, doesn't use extra resources and enough to keep your bot alive 24/7

### Why not *justforping*?

Definitely nothing but no support for `Python<3.8`

## Installation

The easiest way to install is using **pip**:

```bash
pip install justforping
```

But you may also install it this way:

```bash
pip install git+https://github.com/ashkanfeyzollahi/justforping.git
```

Or you may want to build it from source:

```bash
git clone https://github.com/ashkanfeyzollahi/justforping.git
cd justforping
python -m build
```

And you may also wanna include **justforping** in `requirements.txt`, and here's how you do it:

```bash
# Get justforping from Pypi.org
justforping==0.1.0

# Get justforping directly from Github
justforping@git+https://github.com/ashkanfeyzollahi/justforping@main
```

## Example Usage

You may make a **justforping** server and serve it:

```python
from justforping import make_and_serve_justforping_server

make_and_serve_justforping_server("0.0.0.0", 8000)
```

Or you may just make a **justforping** server and **THEN** serve it:

```python
from justforping import make_justforping_server

justforping_server = make_justforping_server("0.0.0.0", 8000)

...

if __name__ == "__main__":
  justforping_server.serve_forever()
  ...
```

Or you may use another WSGI server (e.g `bjoern`) instead of built-in one (`wsgiref`) to serve **justforping** WSGI app, so in that case:

```python
import bjoern
from justforping import justforping_wsgi_app

bjoern.run(justforping_wsgi_app, "0.0.0.0", 8000)
```

