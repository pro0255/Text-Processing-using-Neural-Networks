from src.utils.create_dataset_from_dataframe import create_dataset_from_Xy


def get_train_test_valid_ds(X_train, X_valid, X_test, y_train, y_valid, y_test):
    train_ds = create_dataset_from_Xy(X_train, y_train)
    test_ds = create_dataset_from_Xy(X_test, y_test)
    val_ds = create_dataset_from_Xy(X_valid, y_valid)

    train_records: int = X_train.shape[0]
    test_records: int = X_test.shape[0]
    valid_records: int = X_valid.shape[0]

    return train_ds, val_ds, test_ds, train_records, valid_records, test_records
