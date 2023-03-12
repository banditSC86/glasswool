---
hide:
  - toc
---

# Setting Up a Development Environment

## Required Dependencies

- [`git`](https://git-scm.com/)

=== "Nix"

    #### Support Matrix

    |      Python Version :material-arrow-right: |                       Python 3.8                       |                     Python 3.9                     |                    Python 3.10                     |
    | -----------------------------------------: | :----------------------------------------------------: | :------------------------------------------------: | :------------------------------------------------: |
    | **Operating System** :material-arrow-down: |                                                        |                                                    |                                                    |
    |                                  **Linux** |  {{ config.extra.support_levels.supported.icon }}[^1]  |  {{ config.extra.support_levels.supported.icon }}  |  {{ config.extra.support_levels.supported.icon }}  |
    |                         **macOS (x86_64)** |    {{ config.extra.support_levels.supported.icon }}    |  {{ config.extra.support_levels.supported.icon }}  |  {{ config.extra.support_levels.supported.icon }}  |
    |                                **Windows** | {{ config.extra.support_levels.unsupported.icon }}[^3] | {{ config.extra.support_levels.unsupported.icon }} | {{ config.extra.support_levels.unsupported.icon }} |

    1. [Install `nix`](https://nixos.org/download.html)
    1. Install `gh`:

        === "`nix-shell`"

            ```sh
            nix-shell -p gh
            ```

        === "`nix-env`"

            ```sh
            nix-env -iA gh
            ```

    1. Fork and clone the glasswool repository:

        ```sh
        gh repo fork --clone --remote banditSC86/glasswool
        ```

    1. Set up the public `glasswool` Cachix cache to pull pre-built dependencies:

        ```sh
        nix-shell -p cachix --run 'cachix use glasswool'
        ```

    1. Run `nix-shell` in the checkout directory:

        ```sh
        cd glasswool
        nix-shell
        ```

        This may take a while due to artifact download from the cache.

=== "Conda"

    !!! info "Some optional dependencies for Windows are not available through `conda`/`mamba`"

        1. `clickhouse-cityhash`. Required for compression support in the ClickHouse backend.

    #### Support Matrix

    |      Python Version :material-arrow-right: |                      Python 3.8                      |                      Python 3.9                  |                  Python 3.10                     |
    | -----------------------------------------: | :--------------------------------------------------: | :----------------------------------------------: | :----------------------------------------------: |
    | **Operating System** :material-arrow-down: |                                                      |                                                  |                                                  |
    |                                  **Linux** | {{ config.extra.support_levels.supported.icon }}[^1] | {{ config.extra.support_levels.supported.icon }} | {{ config.extra.support_levels.supported.icon }} |
    |                                  **macOS** |   {{ config.extra.support_levels.supported.icon }}   | {{ config.extra.support_levels.supported.icon }} | {{ config.extra.support_levels.supported.icon }} |
    |                                **Windows** |   {{ config.extra.support_levels.supported.icon }}   | {{ config.extra.support_levels.supported.icon }} | {{ config.extra.support_levels.supported.icon }} |

    {% set managers = {"conda": {"name": "Miniconda", "url": "https://docs.conda.io/en/latest/miniconda.html"}, "mamba": {"name": "Mamba", "url": "https://github.com/mamba-org/mamba"}} %}
    {% for manager, params in managers.items() %}

    === "`{{ manager }}`"

        1. Install [{{ params["name"] }}]({{ params["url"] }})

        1. Install `gh`

            ```sh
            {{ manager }} install -c conda-forge gh
            ```

        1. Fork and clone the glasswool repository:

            ```sh
            gh repo fork --clone --remote banditSC86/glasswool
            ```

        1. Create a Conda environment from a lock file in the repo:

            {% set platforms = {"Linux": "linux", "MacOS": "osx", "Windows": "win"} %}
            {% for os, platform in platforms.items() %}
            === "{{ os }}"

                ```sh
                cd glasswool
                {{ manager }} create -n glasswool-dev --file=conda-lock/{{ platform }}-64-3.9.lock
                ```
            {% endfor %}

        1. Activate the environment

            ```sh
            {{ manager }} activate glasswool-dev
            ```

        1. Install your local copy of `glasswool` into the Conda environment.

            ```sh
            cd glasswool
            pip install -e .
            ```

        1. If you want to run the backend test suite you'll need to install `docker-compose`:

            ```sh
            {{ manager }} install docker-compose -c conda-forge
            ```

    {% endfor %}

=== "pip"

    !!! warning "`pip` will not handle installation of system dependencies"

        `pip` will not install system dependencies needed for some packages
        such as `psycopg2` and `kerberos`.

        For a better development experience see the `conda` or `nix` setup
        instructions.

    1. [Install `gh`](https://cli.github.com/manual/installation)

    1. Fork and clone the glasswool repository:

        ```sh
        gh repo fork --clone --remote banditSC86/glasswool
        ```

    1. Change directory into `glasswool`:

        ```sh
        cd glasswool
        ```

    1. Install development dependencies

        ```sh
        pip install 'poetry>=1.2'
        pip install -r requirements.txt
        ```

    1. Install glasswool in development mode

        ```sh
        pip install -e .
        ```

## Building the Docs

!!! warning "You **must** set up an environment with Nix as above to build the website and docs."

Then, run:

```sh
mkdocs serve
```

{% for data in config.extra.support_levels.values() %}
[^{{ loop.index }}]: {{ data.description }}
{% endfor %}
