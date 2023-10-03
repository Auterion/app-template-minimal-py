# {{cookiecutter.app_name}}
Add a short description of your app.

# Building {{cookiecutter.app_name}}

This is an application developed for AuterionOS powered devices.
Build and install {{cookiecutter.app_name}} using `auterion-cli` commands inside the project folder.

**Build**

```shell
auterion-cli app build
```

Ths command will create an app artifact in `build/{{cookiecutter.developer_slug}}.{{cookiecutter.app_name}}.auterionos`.

After the build process is successfully terminated, connect your device to the development PC and run the following command to install the application on your device:

```shell
auterion-cli app install `build/{{cookiecutter.developer_slug}}.{{cookiecutter.app_name}}.auterionos`
```


The application execution can be monitored by running the following command:

```shell
auterion-cli app logs `{{cookiecutter.developer_slug}}.{{cookiecutter.app_name}} -f
```

You can stop and remove the application with the following commands:

```shell
auterion-cli app remove `{{cookiecutter.developer_slug}}.{{cookiecutter.app_name}}'
```

