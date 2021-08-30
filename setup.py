from distutils.core import setup
setup(
    name='mcpixelart',         # How you named your package folder (MyLib)
    packages=['mcpixelart'],   # Chose the same as "name"
    version='1.1',      # Start with a small number and increase it with every change you make
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='MIT',
    # Give a short description about your library
    description="This is a simple program that takes a source image, and returns the image in it's Minecraft Pixel Art form(a collection of blocks from the game Minecraft by Mojang). It uses Euclidian Distance to compare RGB values of the source image to the minecraft block images, then finds the closest match.",
    author='Noah Vendrig',                   # Type in your name
    author_email='noahvendrig@gmail.com',      # Type in your E-Mail
    # Provide either the link to your github or to your website
    url='https://github.com/noahvendrig/mcpixelart',
    # I explain this later on
    download_url='https://github.com/noahvendrig/mcpixelart/archive/refs/tags/v1.1.tar.gz',
    # Keywords that define your package best
    keywords=['minecraft', 'pixel art', 'pixel', 'art'],
    install_requires=[            # I get to this in a second
        'pillow',
        'tqdm',
        'pandas'
    ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
