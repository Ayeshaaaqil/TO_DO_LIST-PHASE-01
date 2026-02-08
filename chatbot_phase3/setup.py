from setuptools import setup, find_packages

setup(
    name="chatbot_backend",
    version="0.1.0",
    description="A chatbot backend with AI-powered todo management",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/chatbot_backend",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.12",
    install_requires=[
        "fastapi==0.104.1",
        "sqlmodel==0.0.16",
        "pydantic==2.5.0",
        "uvicorn==0.24.0",
        "psycopg2-binary==2.9.9",
        "python-multipart==0.0.6",
        "python-dotenv==1.0.0",
        "asyncpg==0.29.0",
        "passlib==1.7.4",
        "bcrypt==4.0.1",
        "pyjwt==2.8.0",
        "gradio==4.12.0",
        "requests==2.31.0",
        "torch==2.9.1",
        "transformers==4.36.0",
        "accelerate==0.25.0"
    ],
    extras_require={
        "dev": [
            "pytest",
            "black",
            "flake8",
            "mypy",
        ],
    },
)