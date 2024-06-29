## Buildspec

```
version: 0.2
run-as: root

phases:
  install:
    runtime-versions:
      nodejs: 18
    commands:
      - npm install
  build:
    commands:
      - npm run build
      - mkdir -p build/scripts
      - cp -r scripts/* build/scripts/
      - cp appspec.yml build/
artifacts:
  files:
    - '**/*'
  base-directory: build
  discard-paths: no
cache:
  paths:
    - node_modules/
```

## Appspec

```
version: 0.0
os: linux
files:
  - source: /
    destination: /var/www/html
hooks:
  BeforeInstall:
    - location: scripts/install-dependencies.sh
      timeout: 300
      runas: root
  ApplicationStart:
    - location: scripts/start-server.sh
      timeout: 300
      runas: root
```
