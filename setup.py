from setuptools import setup


def main():
    kw = dict(
        name="xontib-kitty",
        description="Xonsh hooks for the Kitty terminal emulator",
        version="0.0.0",
        license="BSD-2-Clause",
        author="Anthony Scopatz",
        maintainer="Anthony Scopatz",
        author_email="scopatz@gmail.com",
        url="https://github.com/scopatz/xontrib-kitty",
        platforms="Cross Platform",
        classifiers=["Programming Language :: Python :: 3"],
        packages=["xontrib", "xontrib_kitty"],
        package_dir={"xontrib": "xontrib", "xontrib_kitty": "xontrib_kitty"},
        package_data={"xontrib": ["*.xsh"], "xontrib_kitty": ["*.xsh"]},
        python_requires=">=3.5",
    )
    setup(**kw)


if __name__ == "__main__":
    main()