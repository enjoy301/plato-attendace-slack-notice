from check_lectures import CheckLectures as CL
import slack_notice as SN
from datetime import datetime


if __name__ == '__main__':
    cl = CL()
    cl.main()
    print_list = [':calendar: '+str(datetime.now())]
    for key in cl.my_dict:
        if len(cl.my_dict[key]) == 0:
            continue

        lecture_name = str(key).split('(')[0].strip()
        print_list.append(':middle_finger: ' + lecture_name + ' :middle_finger:')

        for video_name in cl.my_dict[key]:
            print_list.append(video_name)

    SN.main(print_list)
