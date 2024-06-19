import wandb

run = wandb.init(
    project = 'nyc_airbnb',
    group = 'experiment_1',
    job_type = 'data_cleaning'
)

artifact = wandb.Artifact(
    name = 'sample.csv',
    type='data',
    description='An example of an artifact, it can be a single file or a directory',
    metadata={
        'key_1':'val_1'
    }
)

artifact.add_file('sample.csv')
run.log_artifact(artifact)

run.finish()