from setuptools import setup, find_packages

setup(
    name='CyberProbe',                    # The name of the tool
    version='1.0.0',                       # Version of your tool
    packages=find_packages(),              # Automatically find packages in the current directory
    install_requires=[                    # List of dependencies
        'tqdm',                            # For progress bars
        'requests',                        # For HTTP requests
        'paramiko',                        # For SSH functionality (if using SSH features)
        'colorama',                        # For colored output in the terminal
    ],
    entry_points={                         # Command-line interface (CLI) entry points
        'console_scripts': [
            'cyberprobe=cyberprobe:main',  # Allows users to run "cyberprobe" from the terminal
        ],
    },
    classifiers=[                          # Classifiers to categorize your project on PyPI
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',                # Minimum required Python version
    long_description=open('README.md').read(),  # Description from README
    long_description_content_type='text/markdown',  # Ensure the README is rendered as markdown
)
