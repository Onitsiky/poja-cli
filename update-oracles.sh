#!/bin/bash

mv oracle-poja-base/.git /tmp/gitpojabase
cp -r test-poja-base/* oracle-poja-base
cp -r test-poja-base/.github/* oracle-poja-base/.github
cp -r test-poja-base/.shell/* oracle-poja-base/.shell
mv /tmp/gitpojabase oracle-poja-base/.git

mv oracle-poja-sqlite/.git /tmp/gitpojasqlite
cp -r test-poja-sqlite/* oracle-poja-sqlite
cp -r test-poja-sqlite/.github/* oracle-poja-sqlite/.github
cp -r test-poja-sqlite/.shell/* oracle-poja-sqlite/.shell
mv /tmp/gitpojasqlite oracle-poja-sqlite/.git

rm -rf oracle-poja-base-without-own-vpc
cp -r test-poja-base-without-own-vpc oracle-poja-base-without-own-vpc

rm -rf oracle-poja-base-without-postgres
cp -r test-poja-base-without-postgres oracle-poja-base-without-postgres

rm -rf oracle-poja-base-with-java-env-vars
cp -r test-poja-base-with-java-env-vars oracle-poja-base-with-java-env-vars

rm -rf oracle-poja-base-with-publication-to-npm-registry
cp -r test-poja-base-with-publication-to-npm-registry oracle-poja-base-with-publication-to-npm-registry