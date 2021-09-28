import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', lambda x: '%.5f' % x)


def load_dataset():
    """
    read dataset

    Returns
    -------
    dataframe
    """
    df = pd.read_excel("VERİSETLERİ/ımdb/imdb_top250.xlsx")
    df = df.iloc[:, 1:]
    return df


df = load_dataset()


def processing(dataframe):
    """
    edit ratings and convert to numeric value
    Parameters
    ----------
    dataframe: dataframe
    dataframe

    Returns
    -------
    dataframe
    """
    dataframe["10_points"] = [int(i.replace(",", "")) for i in dataframe["10_points"]]
    dataframe["9_points"] = [int(i.replace(",", "")) for i in dataframe["9_points"]]
    dataframe["8_points"] = [int(i.replace(",", "")) for i in dataframe["8_points"]]
    dataframe["7_points"] = [int(i.replace(",", "")) for i in dataframe["7_points"]]
    dataframe["6_points"] = [int(i.replace(",", "")) for i in dataframe["6_points"]]
    dataframe["5_points"] = [int(i.replace(",", "")) for i in dataframe["5_points"]]
    dataframe["4_points"] = [int(i.replace(",", "")) for i in dataframe["4_points"]]
    dataframe["3_points"] = [int(i.replace(",", "")) for i in dataframe["3_points"]]
    dataframe["2_points"] = [int(i.replace(",", "")) for i in dataframe["2_points"]]
    dataframe["1_points"] = [int(i.replace(",", "")) for i in dataframe["1_points"]]

    return dataframe


df = processing(df)


def total_vote(dataframe):
    """
    sums all points and assigns them to a single variable
    Parameters
    ----------
    dataframe: dataframe

    Returns
    -------
    dataframe
    """
    return dataframe["10_points"] + dataframe["9_points"] + dataframe["8_points"] + \
           dataframe["7_points"] + dataframe["6_points"] + \
           dataframe["5_points"] + dataframe["4_points"] + \
           dataframe["3_points"] + dataframe["2_points"] + dataframe["1_points"]


df["vote_count"] = total_vote(df)


def edit_title(dataframe):
    """
    edit the spaces in the title

    Parameters
    ----------
    dataframe: dataframe

    Returns
    -------
    dataframe
    """
    return [i.split("\n")[0].strip() + " " + i.split("\n")[1].strip() for i in dataframe["title"]]


df["title"] = edit_title(df)


def save_file(dataframe):
    """
    save file

    Parameters
    ----------
    dataframe: dataframe

    Returns
    -------
    None
    """
    dataframe.to_excel("imdb_clear_top250.xlsx")
