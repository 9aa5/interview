
import sys
def partial_result(result_list, prefix, remaining_str, remaining_counter):
    if remaining_counter == 0:
        result_list.append(prefix)
        return
    if len(remaining_str) <= remaining_counter:
        result = prefix + remaining_str
        result_list.append(result)
    else:
        prefix1 = prefix + remaining_str[0]
        remaining_str1 = remaining_str[1:]
        partial_result(result_list, prefix1, remaining_str1, remaining_counter - 1)
        partial_result(result_list, prefix, remaining_str1, remaining_counter)
        
def print_result(password, substr_len):
    result_list = []
    prefix = ""
    remaining_str = password
    partial_result(result_list, prefix, remaining_str, substr_len)
    for result in result_list:
        print result

def main():
    print_result(sys.argv[1], int(sys.argv[2]))

if __name__ == '__main__':
    main()
