## ML Workflow Orchestration With Prefect
* `Prefect` is a powerful and open-source workflow orchestration tool that lets users design, monitor, and respond to data and machine learning pipelines using Python code.

* Prefefct comes equipped with a range of features, such as automatic retries, scheduling, and caching, to name a few. It is a powerful tool that ultimately allows us to construct resilient and dynamic workflows.

### Core Components of Prefect

1. Prefect Task
A `Prefect Task` is a Python function decorated with `@task` decorator that represents discrete units of work within a Prefect workflow. We can also customize the task decorator with optional arguments like name, description, tags, cache settings, retries, and more.

In the code below, there are three machine learning tasks created with `@task` decorator that can be reused across flows.

```
@task
def train_model(X_train, X_test, y_train):
    # Selecting the best features
    ...

    # Train the model
    ...
    return model


@task
def get_prediction(X_test, model: LogisticRegression):
    ...
    return prediction


@task
def evaluate_model(y_test, prediction: pd.DataFrame):
    ...
```

### Prefect Flow
A Prefect Flow is a Python function decorated with the `@flow` decorator that encapsulates workflow logic. This makes it easier for users to define, configure, and execute complex data pipelines with flexibility and ease.

In the code below, we have created a Flow using the `@flow` decorator. The flow will run all the tasks sequentially, taking inputs from one to another.

```
@flow
def ml_workflow():
    model = train_model(X_train, X_test, y_train)
    predictions = get_prediction(X_test, model)
    evaluate_model(y_test, predictions)


if __name__ == "__main__":
    ml_worlflow()

```

### Prefect Deployments
Deployments are flows stored on the local server or on the cloud and include important information for orchestrating our workflow remotely, such as scheduling and execution details.

### Prefect Work Pools
Work pools serve as a mediator between orchestration and execution environments, enabling efficient flow run scheduling and execution. Users can set up their Agents (worker) for running workflows locally or leverage cloud infrastructure for seamless workflow execution.

Similar to a dedicated compute instance, Work Pools efficiently manage work allocation and prioritize tasks, offering flexibility in choosing the execution environment for optimal workflow performance and scalability.

## Orchestrating ML Workflow

### Setting Up Prefect
Install the Python package using PIP.
```
$ pip install -U prefect
```

### Create a Prefect Flow
We will preprocess the [`Bank Churn`](https://www.kaggle.com/datasets/rangalamahesh/bank-churn?select=train.csv) dataset from Kaggle, then use scikit-learn to train and evaluate the Random Forest Classifiers model.

Our machine learning `Prefect Flow` consists of seven tasks:

1. **load_data**: for loading and processing the CSV file using pandas.
2. **preprocessing**: preparing the data for training, filling missing values, encoding, and scaling.
3. **data_split**: splitting the data into testing and training sets.
4. **train_model**: selecting the top features and training the model.
5. **get_prediction**: generating the prediction using a testing set.
6. **evaluate_model**: calculate the accuracy and f1 score.
7. **save_model**: saving the model weights using skops.

We have now assembled all the necessary tasks into a `@flow` function named `ml_workflow`. Additionally, we have included extra arguments in the decorator to enable detailed logging.

The `ml_workflow` function takes the data file location as input and then connects various tasks in a chain.


### Deploying the Flow
Building and running a machine learning pipeline manually is a simple task that can be accomplished even with scikit-learn pipelines.

However, there are multiple benefits to using Prefect. These includes:
* the ability to monitor the pipeline.
* schedule it using CRON.
* automatically retry in case of failure.
* enable logging and observability.
* receive notifications.
* and create automated workflows that can run without human interventions.

Now, we will learn to automate our workflow by deploying it to the local Prefect server.

First, we must build the "Deployment" by providing the file and flow function names. We are also adding the tag "dev" to our Deployment.

**Note**: tags in Prefect can be used to categorize and organize flows, tasks, and deployments in the Prefect ecosystem.

```
$ prefect deployment build main.py:ml_workflow -n "ml_workflow_bank_churn" -a --tag dev
```


