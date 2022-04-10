class NNExpConf:
    def __init__(
        self,
        nn_model,
        train_ds,
        valid_ds,
        test_ds,
        learning_settings,
        description,
        save_model,
        save_best
    ) -> None:
        self.nn_model = nn_model
        self.train_ds = train_ds
        self.valid_ds = valid_ds
        self.test_ds = test_ds
        self.learning_settings = learning_settings
        self.description = description
        self.save = save_model
        self.save_best = save_best

    def get_model(self):
        return self.nn_model

    def get_train(self):
        return self.train_ds

    def get_test(self):
        return self.test_ds

    def get_valid(self):
        return self.valid_ds

    def get_learning_settings(self):
        return self.learning_settings

    def get_description(self):
        return self.description

    def get_save_model(self):
        return self.save

    def get_save_best(self):
        return self.save_best
