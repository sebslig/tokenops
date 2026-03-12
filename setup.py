from setuptools import setup, find_packages

setup(
    name='agentflow-sdk',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # Add any dependencies here, e.g., 'openai>=1.0.0'
    ],
    author='AgentFlow Team',
    description='A Python SDK for orchestrating multi-step AI agent workflows with tool calling.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/agentflow-sdk',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
