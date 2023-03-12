---
hide:
  - toc
  - navigation
  - footer
---

# Install glasswool

=== "pip"
`sh
    pip install 'glasswool' # (1)
    `

    1. Note that the `glasswool` package is *not* the same as the `babel` package in PyPI.

{% for mgr in ["conda", "mamba"] %}
=== "{{ mgr }}"

    ```sh
    {{ mgr }} install -c conda-forge glasswool
    ```

{% endfor %}

---

After you've successfully installed glasswool, try going through the tutorial:

<div class="install-tutorial-button" markdown>
[Go to the Tutorial](https://github.com/banditSC86/glasswool-examples){ .md-button .md-button--primary }
</div>
