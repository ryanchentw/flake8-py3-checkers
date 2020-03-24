import setuptools

setuptools.setup(
    name="flake8_py3_checkers",
    license="MIT",
    version="0.1.0",
    description="Compat. checkers for py3",
    author="Ryan",
    author_email="ryan.chen@pinkoi.com",
    url='',
    install_requires=['setuptools'],
    py_modules=['flake8_py3_checkers'],
    entry_points={
        'flake8.extension': [
            'S01 = flake8_py3_checkers:UnicodeFunctionCallChecker',
        ],
    },
    classifiers=[
        "Framework :: Flake8",
        "Environment :: Console",
        "Programming Language :: Python :: 2",
    ],
)
