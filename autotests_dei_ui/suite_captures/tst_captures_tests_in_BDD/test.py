source(findFile('scripts', 'python/bdd.py'))

setupHooks('../../shared/steps/bdd_hooks.py')
collectStepDefinitions('../../shared/steps')

def main():
    testSettings.throwOnFailure = True
    runFeatureFile('test.feature')
