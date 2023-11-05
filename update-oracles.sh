#!/bin/bash

mv oracle-poja-base/.git /tmp/gitpojabase
rm -rf oracle-poja-base
cp -r test-poja-base oracle-poja-base
mv /tmp/gitpojabase oracle-poja-base/.git

rm -rf oracle-poja-base-with-aws-ses
cp -r test-poja-base-with-aws-ses oracle-poja-base-with-aws-ses
