from setuptools import setup

setup(
    name='MicroTagger',
    version='0.1',
    packages=['MicroTagger'],
    url='',
    include_package_data=True,
    data_files=[(
        '',
        [
            'MicroTagger/hmm_model_data/A.pickle',
            'MicroTagger/hmm_model_data/B.pickle',
            'MicroTagger/hmm_model_data/vocabulary.pickle'
        ]
    )],
    license='MIT',
    author='Xiaoquan Kong',
    author_email='u1mail2me@gmail.com',
    description='A micro Python package for NLP tagger'
)
