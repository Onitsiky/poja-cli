#!/bin/bash

mv tests/oracles/oracle-poja-base/.git /tmp/gitpojabase
cp -r test-poja-base/* tests/oracles/oracle-poja-base
cp -r test-poja-base/.github/* tests/oracles/oracle-poja-base/.github
cp -r test-poja-base/.shell/* tests/oracles/oracle-poja-base/.shell
mv /tmp/gitpojabase tests/oracles/oracle-poja-base/.git

mv tests/oracles/oracle-poja-sqlite/.git /tmp/gitpojasqlite
cp -r test-poja-sqlite/* tests/oracles/oracle-poja-sqlite
cp -r test-poja-sqlite/.github/* tests/oracles/oracle-poja-sqlite/.github
cp -r test-poja-sqlite/.shell/* tests/oracles/oracle-poja-sqlite/.shell
mv /tmp/gitpojasqlite tests/oracles/oracle-poja-sqlite/.git

rm -rf tests/oracles/oracle-poja-base-without-own-vpc
cp -r test-poja-base-without-own-vpc tests/oracles/oracle-poja-base-without-own-vpc

rm -rf tests/oracles/oracle-poja-base-without-postgres
cp -r test-poja-base-without-postgres tests/oracles/oracle-poja-base-without-postgres

rm -rf tests/oracles/oracle-poja-base-with-java-env-vars
cp -r test-poja-base-with-java-env-vars tests/oracles/oracle-poja-base-with-java-env-vars

rm -rf tests/oracles/oracle-poja-base-with-publication-to-npm-registry
cp -r test-poja-base-with-publication-to-npm-registry tests/oracles/oracle-poja-base-with-publication-to-npm-registry