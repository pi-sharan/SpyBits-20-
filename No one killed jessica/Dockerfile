FROM ubuntu:18.04

FROM python:3.7-alpine

RUN apk add --no-cache \
        --virtual=.build-dependencies \
        g++ file binutils \
        musl-dev python3-dev cython && \
    apk add libstdc++ openblas && \
    ln -s locale.h /usr/include/xlocale.h && \
    pip install numpy && \
    rm -r /root/.cache && \
    find /usr/lib/python3.*/ -name 'tests' -exec rm -r '{}' + && \
    find /usr/lib/python3.*/site-packages/ -name '*.so' -print -exec sh -c 'file "{}" | grep -q "not stripped" && strip -s "{}"' \; && \
    rm /usr/include/xlocale.h && \
    apk del .build-dependencies


RUN apk update && apk add socat gcc g++ make openssl-dev python3-dev python-dev libffi-dev autoconf

RUN pip install parse pycryptodome

RUN adduser -Dh /bin/sh ctf

WORKDIR /home/ctf/5007

COPY secret.py .
COPY server.py .

RUN  chown -R root:root /home/ctf

USER ctf

EXPOSE 5007

CMD ["socat", "TCP-LISTEN:5007,reuseaddr,nodelay,fork", "EXEC:python /home/ctf/5007/server.py"]
