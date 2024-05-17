source(findFile('scripts', 'python/bdd.py'))

source(findFile('scripts', '/bdd/steps.py'))
source(findFile('scripts', '/bdd/bdd_hooks.py'))

def main():
    testSettings.throwOnFailure = True
    runFeatureFile('test.feature')
