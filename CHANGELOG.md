# [3.0.0](https://github.com/hei-school/poja-cli/compare/v2.5.0...v3.0.0) (2023-11-14)


### Bug Fixes

* --with-gen-clients ([0b2d2ca](https://github.com/hei-school/poja-cli/commit/0b2d2ca502c9ceac613dad44943a03a397ebd8b0))
* DatasourceConf for handling optional appProp when --with-postgres ([9de177f](https://github.com/hei-school/poja-cli/commit/9de177feb05cc6026aa3369d095ff869ca034abe))
* touch doc/api.yml ([1aa0a65](https://github.com/hei-school/poja-cli/commit/1aa0a65a870887a2a4f632b7fdc974f4d31b21c4))


### Features

* --with-own-vpc ([d5418e1](https://github.com/hei-school/poja-cli/commit/d5418e1c7e1d6c79c84ac55b2436f8cb5c864a57))
* --with-own-vpc ([3ce4481](https://github.com/hei-school/poja-cli/commit/3ce44818c40e427dbac2e7f8771a59c4b36eefec))
* EnvConf is optional ([62b30b6](https://github.com/hei-school/poja-cli/commit/62b30b6ebd770a55a9a6e723781aba5f3cf4f51d))


### BREAKING CHANGES

* default value of --with-gen-client is false
* default value of --with-own-vpc is false



# [2.5.0](https://github.com/hei-school/poja-cli/compare/v2.4.3...v2.5.0) (2023-11-14)


### Features

* --with-publish-to-npm-registry ([3ae4850](https://github.com/hei-school/poja-cli/commit/3ae4850f8400e7e23a0d2e6b40bb4900222e40cf))



## [2.4.3](https://github.com/hei-school/poja-cli/compare/v2.4.2...v2.4.3) (2023-11-10)


### Bug Fixes

* do not save heading whitespace in varenvs ([d31f0fd](https://github.com/hei-school/poja-cli/commit/d31f0fd21b29603ab1ca214fa26038ec85304b09))



## [2.4.2](https://github.com/hei-school/poja-cli/compare/v2.4.1...v2.4.2) (2023-11-10)


### Bug Fixes

* allow spring-web in mailbox for instantions like spring-secu ([c9e8d46](https://github.com/hei-school/poja-cli/commit/c9e8d46d6c99677a38858ac0e768ab584a932194))



## [2.4.1](https://github.com/hei-school/poja-cli/compare/v2.4.0...v2.4.1) (2023-11-10)


### Bug Fixes

* --jacoco-min-coverage is a string ([085b676](https://github.com/hei-school/poja-cli/commit/085b676f854f73bebf3b6297cac3d1555914c7b8))



# [2.4.0](https://github.com/hei-school/poja-cli/compare/v2.3.0...v2.4.0) (2023-11-10)


### Features

* EnvConf for project-specific env vars ([da19a48](https://github.com/hei-school/poja-cli/commit/da19a48636fba36a9cede31fb82832c1c0c8d2c8))



# [2.3.0](https://github.com/hei-school/poja-cli/compare/v2.2.0...v2.3.0) (2023-11-10)


### Features

* make jacoco min coverage configurable ([6e78078](https://github.com/hei-school/poja-cli/commit/6e780788e6b974f8543f77dd6aeeb5b388922b39))



# [2.2.0](https://github.com/hei-school/poja-cli/compare/v2.1.0...v2.2.0) (2023-11-10)


### Bug Fixes

* revert "feat: rm writing permission on generated files" ([1e03204](https://github.com/hei-school/poja-cli/commit/1e0320466370123a61c531beab89f71c8597a1af))


### Features

* publish to mvn local and gen ts-axios ([9bb4ccc](https://github.com/hei-school/poja-cli/commit/9bb4cccce72d3650f0d5db3addca4afd79ab6c18))



# [2.1.0](https://github.com/hei-school/poja-cli/compare/v2.0.4...v2.1.0) (2023-11-09)


### Bug Fixes

* version.yml --> poja-version.yml ([7039e9b](https://github.com/hei-school/poja-cli/commit/7039e9b3031f67b9e4c4b59055526a418350f3a3))


### Features

* rm writing permission on generated files ([bb7679a](https://github.com/hei-school/poja-cli/commit/bb7679a72c9e14e92bd47a887cf91b95741a1d76))



## [2.0.4](https://github.com/hei-school/poja-cli/compare/v2.0.2...v2.0.4) (2023-11-09)


### Bug Fixes

* correctly set package name in build.gradle ([12f1275](https://github.com/hei-school/poja-cli/commit/12f1275b73b38e4098c498af4f656d4c300f6717))
* with_postgres is a string in cli ([1d831a1](https://github.com/hei-school/poja-cli/commit/1d831a131270d509a4a10cf453e47c4bf2b07243))



## [2.0.2](https://github.com/hei-school/poja-cli/compare/v2.0.1...v2.0.2) (2023-11-08)


### Bug Fixes

* no poja-base in db env vars ([124ac36](https://github.com/hei-school/poja-cli/commit/124ac3641f0552e9b13bdadbfd2f67ca1a0c57d0))



## [2.0.1](https://github.com/hei-school/poja-cli/compare/v2.0.0...v2.0.1) (2023-11-08)


### Bug Fixes

* java-deps: swagger and and hibernate-types ([d963481](https://github.com/hei-school/poja-cli/commit/d963481007debb6f68a4773af273ea71c5f0139b))



# [2.0.0](https://github.com/hei-school/poja-cli/compare/v1.4.0...v2.0.0) (2023-11-08)

### BREAKING CHANGES

* downgrade to Spring 2

### Features

* openapi-gen Java client

### Bug Fixes

* no cd-domain


# [1.4.0](https://github.com/hei-school/poja-cli/compare/v1.3.0...v1.4.0) (2023-11-07)


### Features

* --custom-java-env-vars ([c51e18b](https://github.com/hei-school/poja-cli/commit/c51e18b65a2c0a0102b213f733c4791fafc6d31e))
* --with-postgres ([a684996](https://github.com/hei-school/poja-cli/commit/a684996550b4a6b95bc21fcd224db6efdb4d0ade))



# [1.3.0](https://github.com/hei-school/poja-cli/compare/v1.2.1...v1.3.0) (2023-11-05)


### Features

* custom Java deps ([ac9676f](https://github.com/hei-school/poja-cli/commit/ac9676f0f5bcb1faa1246a5f18c1890be9223f39))



## [1.2.1](https://github.com/hei-school/poja-cli/compare/v1.2.0...v1.2.1) (2023-11-05)


### Bug Fixes

* manually add missing entries to CHANGELOG.md ([4fdf063](https://github.com/hei-school/poja-cli/commit/4fdf063387eb259908b0d05e2910e15a052bbc6b))



# [1.2.0](https://github.com/hei-school/poja-cli/compare/v1.1.0...v1.2.0) (2023-11-05)


### Features

* reflection for event routing ([ab01a26](https://github.com/hei-school/poja-cli/commit/ab01a2621289e9fe5e3862048cb9baee0cd2927b))



# [1.1.0](https://github.com/hei-school/poja-cli/compare/v1.0.0...v1.1.0) (2023-11-04)


### Features

* health check on async stack ([d307cb6](https://github.com/hei-school/poja-cli/commit/d307cb68c856f44913925ae847adb800aedda7f9))

* format.sh using Google Java Format
    
* fail tests under 0.8 line cov


# [1.0.0](https://github.com/hei-school/poja-cli/compare/v0.3.0...v1.0.0) (2023-11-03)


### Features

* event stack ([f186d82](https://github.com/hei-school/poja-cli/commit/f186d82ed886d16c5f6786186092e7e465466067))

* disable flyway migration during Mailbox

* push messages by batch of 5

### Bug Fixes

* SpringApp is Poja, not Mailbox

### BREAKING CHANGES

* POJA subnets must be private


# [0.3.0](https://github.com/hei-school/poja-cli/compare/v0.2.0...v0.3.0) (2023-11-02)


### Bug Fixes

* do not override target README ([b345b5c](https://github.com/hei-school/poja-cli/commit/b345b5c61fec507059d60d27221f1e4ed429cbe9))


### Features

* --package-full-name ([1ade51a](https://github.com/hei-school/poja-cli/commit/1ade51acbb6eb55189263134d68c7b796a756f5c))



# [0.2.0](https://github.com/hei-school/poja-cli/compare/v0.1.4...v0.2.0) (2023-11-02)


### Features

* configurable scaling down timeout for prod db ([35e31da](https://github.com/hei-school/poja-cli/commit/35e31da756706a7100b5d3817f5270f3da58fbbe))



## [0.1.4](https://github.com/hei-school/poja-cli/compare/v0.1.3...v0.1.4) (2023-11-01)


### Bug Fixes

* save conf after gen ([b2d57b9](https://github.com/hei-school/poja-cli/commit/b2d57b98048b23bd34d8f2a5291d0928cefd2068))



## [0.1.3](https://github.com/hei-school/poja-cli/compare/v0.1.2...v0.1.3) (2023-11-01)


### Bug Fixes

* do not print final gen output ([631d1f3](https://github.com/hei-school/poja-cli/commit/631d1f3efaaf2a38282e00a988f6f84d66efde80))



## [0.1.2](https://github.com/hei-school/poja-cli/compare/v0.1.1...v0.1.2) (2023-11-01)


### Bug Fixes

* pyyaml is a main dependency ([ee0e054](https://github.com/hei-school/poja-cli/commit/ee0e05469f0fa949901f4efcc321fdbb4ce73052))



## [0.1.1](https://github.com/hei-school/poja-cli/compare/v0.1.0...v0.1.1) (2023-11-01)


### Bug Fixes

* pretty print progression ([e673ce3](https://github.com/hei-school/poja-cli/commit/e673ce3a819c75ea35d1ebaee0d2530774db22da))



# [0.1.0](https://github.com/hei-school/poja-cli/compare/25a899959c3e74d8fbbef6840629c2c3a3c18cf1...v0.1.0) (2023-11-01)


### Features

* poja.gen ([25a8999](https://github.com/hei-school/poja-cli/commit/25a899959c3e74d8fbbef6840629c2c3a3c18cf1))
* py package ([5cf4f58](https://github.com/hei-school/poja-cli/commit/5cf4f58218cc6394704d1b3011be40933e19a35d))



