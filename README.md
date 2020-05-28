# quay-packages


Example Instructions
```
Create dir python3-alembic
Create .tito/packages/python3-alembic
Download tar.gz from pypi.org
Change Source0 to point to downloaded tar.gz
git add and git commit

pyp2rpm -r python3-alembic -v 1.3.3 -b 3 alembic > python3-alembic.spec

tito build --test --srpm
tito build --test --rpm


tito build --test --srpm | grep Wrote | awk '{print $2}'
```
