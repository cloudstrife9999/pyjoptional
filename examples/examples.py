from pyoptional.pyoptional import PyOptional

p1: PyOptional[int] = PyOptional.of(1)
p2: PyOptional[str] = PyOptional.of("foo")
p3: PyOptional[bytes] = PyOptional.empty()