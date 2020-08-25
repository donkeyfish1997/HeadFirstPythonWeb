import pickle
import athletelist as im


def put_to_store(files_list):
    all_athletes = {}
    for each_file in files_list:
        ath = im.get_coach_data(each_file)
        all_athletes[ath.name] = ath

    try:
        with open('athletes.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
    except IOError as err:
        print('IOError is ', err)

    return (all_athletes)


def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as err:
        print('IOError is', err)

    return (all_athletes)


if __name__ == '__main__':

    # path = 'data/'
    # files_list = [path + 'james.txt', path + 'julie.txt', path + 'mikey.txt', path + 'sarah.txt']
    #
    # data = put_to_store(files_list)
    #
    # for each_data in data:
    #     print(data[each_data].name, data[each_data].dob, data[each_data], sep='\t')
    print('fff')
    print(get_from_store())
