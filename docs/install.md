---
hide:
  - toc
  - navigation
  - footer
---

# Install Babel

=== "pip"
`sh
    pip install 'babel-data' # (1)
    `

    1. Note that the `babel-data` package is *not* the same as the `babel` package in PyPI.

{% for mgr in ["conda", "mamba"] %}
=== "{{ mgr }}"

    ```sh
    {{ mgr }} install -c conda-forge babel-data
    ```

{% endfor %}

---

After you've successfully installed Babel, try going through the tutorial:

<div class="install-tutorial-button" markdown>
[Go to the Tutorial](https://github.com/babel-data/babel-examples){ .md-button .md-button--primary }
</div>
