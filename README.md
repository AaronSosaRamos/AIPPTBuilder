# AIPPTBuilder 📊🚀

Welcome to **AIPPTBuilder**, an innovative backend module that leverages the power of **Google Generative AI** to create **PPTs from scratch**. Whether you're a professional, educator, or student, this tool streamlines the process of creating presentations by generating slides dynamically using cutting-edge AI technologies. Developed by **Wilfredo Aaron Sosa Ramos**, this project aims to redefine the way we approach presentation building.

## Table of Contents 📑

- [Introduction](#introduction-)
- [Key Features](#key-features-)
- [Use Cases](#use-cases-)
- [Tech Stack](#tech-stack-)
- [Architecture](#architecture-)
- [Versioning](#versioning-)
- [Installation Guide](#installation-guide-)
- [How to Use](#how-to-use-)
- [Contributing](#contributing-)
- [License](#license-)
- [Acknowledgments](#acknowledgments-)

---

## Introduction 🧠

AIPPTBuilder is an AI-powered solution designed to revolutionize the process of creating PowerPoint presentations. The backend module makes use of **Google Generative AI** for content generation and offers seamless interaction through **Gradio**-powered UIs, facilitating rapid development. With version control traced through **Jupyter Notebooks**, AIPPTBuilder ensures flexibility, accuracy, and ease of use in every stage of presentation creation.

---

## Key Features 🌟

- **Automated PPT Generation**: Use Google Generative AI to create structured presentations from scratch based on user input.
- **Interactive UI**: Developed with **Gradio**, offering a user-friendly interface to interact with the backend AI services.
- **Jupyter Notebook Support**: Includes drafts and development stages (version 1, 2, and 3) tracked via Jupyter Notebooks.
- **FastAPI Backend**: A high-performance, scalable backend framework for handling API requests.
- **Version Control**: Jupyter notebooks are used for tracing the evolution of the project across multiple versions.

---

## Use Cases 🛠️

AIPPTBuilder is built to cater to a variety of use cases, including but not limited to:

- **Educational Institutions**: Automatically generate educational slides for lectures, tutorials, or research presentations.
- **Business Professionals**: Create dynamic and professional presentations for pitches, reports, and meetings.
- **Students**: Simplify the process of creating presentation slides for assignments or group projects.
- **Content Creators**: Quickly generate well-structured slides for webinars, online courses, and tutorials.

---

## Tech Stack ⚙️

The following technologies are used in the development of AIPPTBuilder:

- **Python** 🐍: The backbone of the project, used for scripting, AI models, and FastAPI services.
- **FastAPI** ⚡: A modern, fast (high-performance) web framework for building APIs with Python.
- **Google Generative AI** 🤖: Powers the AI that generates presentation content dynamically based on prompts.
- **Langchain** 🔗: A framework for building AI-driven applications with language models.
- **Gradio** 🖥️: Provides a simple interface for the backend UI, enabling rapid interaction with the AI services.
- **Jupyter Notebooks** 📓: Used for drafting, versioning, and documenting the AI model's progression.

---

## Architecture 🏗️

The architecture of AIPPTBuilder follows a modular structure for optimal performance and scalability:

- **Frontend**: A minimal interface generated using Gradio for interacting with the AI model.
- **Backend**: Built on **FastAPI**, ensuring efficient handling of API requests and model inference.
- **AI Model**: **Google Generative AI** acts as the brain of the operation, creating slide content based on inputs.
- **Version Control**: Jupyter Notebooks keep track of drafts and progression across versions (1, 2, and 3).

![Architecture Diagram](https://link-to-architecture-diagram.com)

---

## Versioning 📌

AIPPTBuilder has undergone three main stages of development, each documented through **Jupyter Notebooks**:

- **Version 1**: Initial implementation of Google Generative AI for generating simple slide content.
- **Version 2**: Enhanced content generation capabilities with improvements in slide structuring and formatting.
- **Version 3**: Optimized for faster performance, improved scalability, and UI enhancements via **Gradio**.

---

## Installation Guide 🛠️

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Jupyter Notebook
- Docker (optional for containerization)

### Installation Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/AIPPTBuilder.git
    ```
2. **Navigate to the project directory**:
    ```bash
    cd AIPPTBuilder
    ```
3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4. **Run the Jupyter Notebooks** (for tracking versions):
    ```bash
    jupyter notebook
    ```
5. **Start the FastAPI server**:
    ```bash
    uvicorn app.main:app --reload
    ```

---

## How to Use 🤖

Once you've installed and set up the project, follow these steps to generate a PPT from scratch:

1. **Run the Gradio UI**: 
    - Access the interactive UI by starting the Gradio interface in the backend.
    - Enter a description or prompt for your presentation.
    - Select the number of slides you'd like to generate.
2. **Generate PPT**:
    - The backend will process the input using **Google Generative AI** and return a downloadable PPT file.
3. **Version Control**: 
    - If you'd like to review or modify earlier versions, access the corresponding **Jupyter Notebook** to trace the changes across versions.

---

## Contributing 🤝

We welcome contributions from developers and enthusiasts alike! Here's how you can get involved:

1. Fork the project.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

---

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Acknowledgments 🙏

Special thanks to the **Google Generative AI** and **Gradio** communities for their support and contributions to open-source development. This project wouldn’t have been possible without the fantastic open-source tools and frameworks provided by the Python ecosystem.

---

Made by: **Wilfredo Aaron Sosa Ramos** 💻
