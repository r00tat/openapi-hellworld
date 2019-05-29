#!/usr/bin/env python3

import os
import connexion


def post_greeting(name: str) -> str:
    return 'Hello {name}'.format(name=name)


if __name__ == '__main__':
    app = connexion.FlaskApp(
        __name__, port=(os.getenv("PORT", 9001)), specification_dir='openapi/')
    app.add_api('helloworld-api.yaml', arguments={'title': 'Hello World Example'})
    app.run()
