import os
import json
import random
import pandas as pd
from faker import Faker


def generate_float(*args, **kwargs):
    return round(abs(random.random() * random.randint(1000, 99999)), 2)


def currency_format_number(min_len=4, max_len=7, *args, **kwargs):
    if max_len > 10:
        max_len = 7
    val = round(abs(random.random() * random.randint(int('1' + '0'*(min_len -1)), int('9'*max_len))), 2)
    if random.random() > 0.1:
        return "{:,.2f}".format(val)
    return "{:,}".format(int(val)) + "."


def generate_date(format='%Y-%m-%d', *args, **kwargs):
    fake = kwargs.get('fake')
    date = fake.date_between(start_date='-7y')
    return date.strftime(format)


def employer_address(index=0, *args, **kwargs):
    fake = kwargs.get('fake')
    return fake.address().split('\n')[index]


def default_function(string='', *args, **kwargs):
    # Do not remove default function
    return string


def full_address(**kwargs):
    fake = kwargs.get('fake')
    addr1, addr2 =  fake.address().split('\n')
    return addr1 + ", " + addr2


def load_json_file(file_path):
    script_dir = os.path.dirname(__file__)
    print(script_dir)
    abs_file_path = os.path.join(script_dir, file_path)
    filehandle = open(abs_file_path)
    data = filehandle.read()
    filehandle.close()
    return json.loads(data)


def generate_random_number(start=0, end=1000000, **kwargs):
    return random.randint(start, end)


def get_total_amount(**kwargs):
    total_amount = 0.0
    sum_labels = kwargs.get('sum_labels', [])
    samples = kwargs.get('samples', {})
    index = kwargs.get('sample_index')
    difference_labels = kwargs.get('difference_labels', [])
    for label in sum_labels:
        label_values = samples.get(label,  None)
        # print(samples)
        # print(label)
        # print(label_values)
        if label_values is not None:
            val = str(label_values[index])
            val = val.replace(",", "")
            if len(val) > 0:
                val = float(val)
                total_amount += val
    for label in difference_labels:
        label_values = samples.get(label, None)
        if label_values is not None:
            val = str(label_values[index])
            # print(val)
            val = val.replace(",", "")
            if len(val) > 0:
                val = float(val)
                total_amount -= val
    if total_amount == 0.00:
        return ''
    return "{:,.2f}".format(total_amount)

def get_total_amount_in_int(**kwargs):
    total_amount = 0.0
    sum_labels = kwargs.get('sum_labels', [])
    samples = kwargs.get('samples', {})
    index = kwargs.get('sample_index')
    difference_labels = kwargs.get('difference_labels', [])
    for label in sum_labels:
        label_values = samples.get(label,  None)
        # print(samples)
        # print(label)
        # print(label_values)
        if label_values is not None:
            val = str(label_values[index])
            val = val.replace(",", "")
            if len(val) > 0:
                val = float(val)
                total_amount += val
    for label in difference_labels:
        label_values = samples.get(label, None)
        if label_values is not None:
            val = str(label_values[index])
            # print(val)
            val = val.replace(",", "")
            if len(val) > 0:
                val = float(val)
                total_amount -= val
    if total_amount == 0.00:
        return ''
    total_amount = int(total_amount)
    return f'{total_amount}'

def check_and_subtract(**kwargs):
    total_amount = 0.0
    sum_labels = kwargs.get('sum_labels', [])
    samples = kwargs.get('samples', {})
    index = kwargs.get('sample_index')
    empty_allowed = kwargs.get('empty_allowed',False)
    difference_labels = kwargs.get('difference_labels', [])
    check_type = kwargs.get('check_type',False)
    for label in sum_labels:
        label_values = samples.get(label,  None)
        # print(samples)
        # print(label)
        # print(label_values)
        if label_values is not None:
            val = label_values[index]
            # print(val)
            val = val.replace(",", "")
            if len(val) > 0:
                val = float(val)
                total_amount += val
    for label in difference_labels:
        label_values = samples.get(label, None)
        if label_values is not None:
            val = label_values[index]
            # print(val)
            val = val.replace(",", "")
            if len(val) > 0:
                val = float(val)
                total_amount -= val
    if total_amount < 0 :
        if check_type:
            total_amount = 0 - total_amount    
        elif empty_allowed:
            return ''
        else:
            return '0'
    return "{:,.2f}".format(total_amount)

def multiply(**kwargs):
    label = kwargs.get('multiply_label', '')
    samples = kwargs.get('samples', {})
    index = kwargs.get('sample_index')
    label_values = samples.get(label, None)
    multiplier = kwargs.get('multiplier', 1)
    check = kwargs.get('check',False)
    check_label = kwargs.get('check_label')
    less_than = kwargs.get('less_than')
    if check:
        check_label = samples.get(check_label, None)
        check_val = check_label[index]
        check_val = check_val.replace(",", "")
        if len(check_val) > 0:
            check_val = float(check_val)
            less_than = float(less_than.replace(",",""))
            if check_val > less_than:
                return ''
    if label_values is not None:
        val = label_values[index]
        # print(val)
        val = val.replace(",", "")
        if len(val) > 0:
            val = float(val)
            val = val * float(multiplier)
    if val:
        return "{:,.2f}".format(val)
    else:
        return val


def get_same_value(**kwargs):
    label = kwargs.get('equal_label', '')
    samples = kwargs.get('samples', {})
    index = kwargs.get('sample_index')
    label_values = samples.get(label, None)
    if label_values is not None:
       return label_values[index]
    return ''


def names_shown_on_return(**kwargs):
    fake = kwargs.get('fake')
    operands = [" and ", " & ", ", "]
    val = random.uniform(0, 1)
    if val < 0.3:
        return fake.name()

    if 0.3 <= val < 0.5:
        return fake.name() + random.choice(operands) + fake.name()
    return fake.first_name() + random.choice(operands) + fake.name()

def find_smaller_value(**kwargs):
    '''
    to find value minimum value between the labels
    '''
    comp_labels = kwargs.get('comparison_labels', [])
    samples = kwargs.get('samples', {})
    index = kwargs.get('sample_index')
    value_list = []
    for label in comp_labels:
        label_values = samples.get(label,  None)
        if label_values is not None:
            val = label_values[index]
            # print(val)
            val = val.replace(",", "")
            if len(val) > 0:
                val = float(val)
                value_list.append(val)
    if len(value_list) == 0:
        return ''
    value_list.sort()
    return "{:,.2f}".format(value_list[0])

def person_first_name_and_middle_initials(**kwargs):
    fake = kwargs.get('fake')
    val = random.uniform(0,1)
    first_name = fake.first_name()
    if val < 0.5 :
        return first_name
    import string
    return first_name +' '+ random.choice(string.ascii_letters).upper()+'.'

def person_last_name(**kwargs):
    fake = kwargs.get('fake')
    return fake.last_name()

def person_first_name(**kwargs):
    fake = kwargs.get('fake')
    return fake.first_name()

def person_relationship(**kwargs):
    relation = ['Mother','Sister','Brother','Father','Daughter','Son','Friend','Cousin','Wife','Husband']
    return random.choice(relation)

def generate_street_address(**kwargs):
    faker_locale_list =  ['en_US']#,'cs_CZ','zh_CN','en_CA','en_GB','en_IN','en_NZ','en_PH','en_TH','en_IE']
    fake = Faker(faker_locale_list)
    return fake.street_address()

def generate_apt_no(**kwargs):
    fake = kwargs.get('fake')
    return fake.building_number()

def generate_city_or_po(**kwargs):
    faker_locale_list =  ['en_US','cs_CZ','zh_CN','en_CA','en_GB','en_IN','en_NZ','en_PH','en_TH','en_IE']
    fake = Faker(faker_locale_list)
    fake = kwargs.get('fake')
    return fake.city()

def generate_country(**kwargs):
    faker_locale_list =  ['en_US','cs_CZ','zh_CN','en_CA','en_GB','en_IN','en_NZ','en_PH','en_TH','en_IE']
    fake = Faker(faker_locale_list)
    fake =kwargs.get('fake')
    return fake.country()

def generate_postcode(**kwargs):
    fake = kwargs.get('fake')
    return fake.postcode()

def generate_zipcode(**kwargs):
    fake = kwargs.get('fake')
    return fake.zipcode()

def generate_province_or_state(**kwargs):
    faker_locale_list =  ['en_US','cs_CZ','zh_CN','en_CA','en_GB','en_IN','en_NZ','en_PH','en_TH','en_IE']
    fake = Faker(faker_locale_list)
    fake = kwargs.get('fake')
    val = random.uniform(0, 1)
    if val < 0.5:
        return fake.province()
    return fake.state()

def main():
    # Load JSON Config file
    # file_path = 'format.json'
    file_path = 'schema_1040_main_doc_2012.json'
    data = load_json_file(file_path)
    number_samples = data.get('number_of_samples', 100)
    shuffle_samples = data.get('shuffle_samples', True)

    # Initialize Faker 
    faker_locale_list = data.get('faker_locale_list', ['en_US'])
    fake = Faker(faker_locale_list)

    # Create a dict for pandas df
    # Sample - {'col' : ['row1', 'row2']}
    labels = data.get('labels', [])
    checkboxes = data.get('checkboxes', [])
    samples = {}

    # Iterating over all labels
    counter = 1
    fields_count = []
    for label_idx, label in enumerate(labels):
        label_name = label.get('label_name', f'label{label_idx}')
        label_type = label.get('label_type', 'str')
        shuffle_labels = label.get('shuffle_labels', True)
        options = label.get('options', [])

        label_samples = []
        for option_index, option in enumerate(options):
            # There can be plenty of options that can be available
            # for a single column with percentage
            function_type = option.get('function_type', 'custom_function')
            function_name = option.get('function_name', 'default_function')
            function_param = option.get('function_param', {})
            option_percentage = option.get('option_percentage', 1)
            on_dependent_label_names = function_param.get('on_dependent_label_names', [])
            dependent_compare_str = function_param.get('compare_string', '')
            operator = function_param.get('operator', "equals")
            # print(on_dependent_label_names)
            # print(option_percentage)
            # By option percentage divide the number of samples 
            current_length = len(label_samples)
            # Check if this is not last option 
            if option_index < len(options) - 1:
                required_samples = int(number_samples * option_percentage)
                # This is to ensure samples doesn't exceed number_samples
                required_samples = min(required_samples, number_samples - current_length)
            else:
                # If this is last option 
                required_samples = number_samples - current_length

            # Generate required_samples for this 
            if function_type == 'faker_function':
                for i in range(required_samples):
                    is_on_dependent_str_match = False

                    for dependent_label in on_dependent_label_names:
                        shuffle_labels = False
                        if samples[dependent_label] is not None:
                            if operator == 'equals':
                                if samples[dependent_label][i + 1] == dependent_compare_str:
                                    is_on_dependent_str_match = True
                                    break
                            else:
                                if samples[dependent_label][i + 1] != dependent_compare_str:
                                    is_on_dependent_str_match = True
                                    break
                    if is_on_dependent_str_match:
                        val = default_function(string=function_param.get('dependent_matched_string', ''))
                    else:
                        if function_param.get('on_dependent_label_names', None):
                            del function_param['on_dependent_label_names']
                            del function_param['compare_string']

                        if function_param.get('operator', None):
                            del function_param['operator']
                        if function_param.get('string', None):
                           del function_param['string']
                        val = getattr(fake, function_name)(**function_param)
                    if label_type == "str":
                        val = str(val)
                    label_samples.append(val)
            elif function_type == 'custom_function':
                function_param['fake'] = fake
                function_param['samples'] = samples
                for i in range(required_samples):
                    function_param['sample_index'] = i + 1
                    is_on_dependent_str_match = False
                    dependent_compare_str = function_param.get('compare_string', '')
                    for dependent_label in on_dependent_label_names:

                        if samples[dependent_label] is not None:
                            if samples[dependent_label][i+1] == dependent_compare_str:
                                is_on_dependent_str_match = True
                                break
                    if is_on_dependent_str_match:
                        val = default_function(string=function_param.get('dependent_matched_string', ''))
                    else:
                        val = globals()[function_name](**function_param)
                    label_samples.append(val)
            else:
                raise KeyError(f'Function type - {function_type} for label - {label_name} doesn\'t exists.')

        if shuffle_samples and len(on_dependent_label_names) == 0:
            random.shuffle(label_samples)
        print(label_samples)

        assert len(label_samples) == number_samples
        # if shuffle_labels:
        #     random.shuffle(label_samples)
        samples[label_name] = [label_type] + label_samples
        fields_count.append(counter)
        counter += 1

    samples_modified = {}

    counter = 1

    for key in samples.keys():
        lst = [key]
        lst.extend(samples[key])
        samples_modified[counter] = lst
        counter += 1

    # samples_df = pd.DataFrame(samples_modified)
    samples_df = pd.DataFrame(samples)
    if shuffle_samples:
        samples_df = pd.concat([samples_df[:1], samples_df[1:].sample(frac=1)]).reset_index(drop=True)
        # samples_df = pd.concat([samples_df[:2], samples_df[2:].sample(frac=1)]).reset_index(drop=True)
    # samples_df.iloc[0] = fields_count
    print(samples_df)
    samples_df.to_excel('jsongeneratedexcel/FinalData/DS/2021/samples_data_1040_main_2021.xlsx', index = False)


if __name__ == "__main__":
    main()
