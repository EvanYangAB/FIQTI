import pipy
 
packpath = "pyqtree.py"
pipy.define_upload(packpath,
                   author="Karim Bahgat",
                   author_email="karim.bahgat.norway@gmail.com",
                   license="MIT",
                   name="Pyqtree",
                   description="A pure Python quad tree spatial index for GIS or rendering usage.",
                   url="http://github.com/karimbahgat/Pyqtree",
                   keywords="GIS spatial index quad tree",
                   classifiers=["License :: OSI Approved",
                                "Programming Language :: Python",
                                "Development Status :: 4 - Beta",
                                "Intended Audience :: Developers",
                                "Intended Audience :: Science/Research",
                                'Intended Audience :: End Users/Desktop',
                                "Topic :: Scientific/Engineering :: GIS"],
                   changes=["Bump to first major version",
                            "Fix so returns list instead of set",
                            "Support inserting hashable items",
                            ],
                   )

pipy.generate_docs(packpath)
#pipy.upload_test(packpath)
#pipy.upload(packpath)

