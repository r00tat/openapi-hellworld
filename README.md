# Hello World Example

Running from docker ub:

```bash
docker run --rm -p 9001:9001 paulwoelfel/openapi-helloworld
```

Running from source

```bash
docker build -t openapi-helloworld . && docker run --rm -p 9001:9001 openapi-helloworld
```

Now open your browser and go to http://localhost:9090/v1.0/ui/ to see the Swagger UI.

Example from [zalandao/connexion](https://github.com/zalando/connexion/tree/master/examples/openapi3/helloworld)
