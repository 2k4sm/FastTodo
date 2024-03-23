<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-api-open.svg" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">FastTodo</h1>
</p>
<p align="center">
    <em><code>► A simple Todo api created using FastAPI.</code></em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/last-commit/2k4sm/FastTodo?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/2k4sm/FastTodo?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/2k4sm/FastTodo?style=default&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>

<br><!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary><br>

- [ Overview](#-overview)
- [ Repository Structure](#-repository-structure)
- [ Getting Started](#-getting-started)
  - [ Setup](#setup)
  - [ Tests](#-tests)
- [ Project Roadmap](#-project-roadmap)
</details>
<hr>

##  Overview

<code>► A restful API for creating and managing todos.</code>

##  Repository Structure

```sh
└── FastTodo/
    ├── main.py
    ├── models
    │   ├── all_todos.py
    │   ├── create_todo.py
    │   ├── todo.py
    │   └── todos.py
    └── reqs.txt
```

##  Getting Started

**System Requirements:**

* **Python**: `version 3.*.*`

###  Setup

<h4>From <code>source</code></h4>

> 1. Clone the FastTodo repository:
>
> ```console
> $ git clone https://github.com/2k4sm/FastTodo
> ```
>
> 2. Change to the project directory:
> ```console
> $ cd FastTodo
> ```
>
> 3. Install the dependencies:
> ```console
> $ pip install -r requirements.txt
> ```

> 4. Run FastTodo using the command below:
> ```console
> $ uvicorn main:fastTodo --reload
> ```

###  Tests

> Run the test suite using the command below:
> ```console
> $ pytest
> ```

---

##  Project Roadmap

- [X] `► Create All Endpoints`
- [ ] `► Add basic CI/CD using github actions and docker.`
- [ ] `► Deploy to a free hosting service.`
- [ ] `► Migrate to own no-sql database`
- [ ] `► Add Logging`
- [ ] `► Add Authentication`
- [ ] `► Add Rate Limiting`


# Thanks for using FastTodo.