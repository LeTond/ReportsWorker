from Algorithm.reports_segmentation import *
from Keys.global_keys import *

from Keys.key_words_SPINE_mri import *

from Algorithm.export_authomatization import *
from time import time
from collections import deque

import multiprocessing as mp


def mri_preproc_start():
    start = time()
    for pat in key_for_area_list:
        process_jobs = deque()
        create_folder_area(pat[1], root)
        for fltr in os.listdir(root + path_mri_copy):
            p = mp.Process(target=start_segmentation,
                           args=(fltr, root, path_mri_copy, pat[0], pat[1]))
            process_jobs.append(p)
            p.start()
        for p in process_jobs:
            p.join()

    for pat in global_pathology_mri_list:
        create_folder_pathology(pat[1], root, pat[2])
        for fltr in os.listdir(root + '/' + pat[3].replace('//', '/')):
            continue_segmentation(fltr, root, key_words_for_remove, key_head_words, pat[0], pat[1], pat[2], pat[3])
    end = time()
    print(end - start)


def mri_preproc_end():
    start = time()

    for pat in global_pathology_mri_list:
        process_jobs = []
        for fltr in os.listdir(root + '/' + pat[3].replace('//', '/')):
            p = mp.Process(target=remove_segmented,
                           args=(fltr, root, pat[1], pat[2], pat[3]))
            process_jobs.append(p)
            p.start()
        for p in process_jobs:
            p.join()

    for pat in global_pathology_mri_list:
        process_jobs = []
        for fltr in os.listdir(root + '/' + pat[3].replace('//', '/')):
            p = mp.Process(target=segment_else,
                           args=(fltr, root, key_words_for_remove, key_head_words, pat[1]))
            process_jobs.append(p)
            p.start()
        for p in process_jobs:
            p.join()

    end = time()
    print(end - start)


def ct_preproc_start():
    # start = time()
    # process_jobs = []
    # for fltr in os.listdir(root + path_ct):
    #     p = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_ct,
    #                                                     ct_key_for_hip, ct_structure_hip, ct_key_name_hip))
    pass


if __name__ == "__main__":
    """
    Запуск алгоритма конвертиции из .doc в .docx
    """
    # @line_profile
    # docx_(root, path_mri)
    # docx_(root, path_ct)
    """
    Processing MRI reports
    """
    # mri_preproc_start()
    # mri_preproc_end()
    """
    Processing CT reports
    """
    # ct_preproc_start()
    """
    exporting reports to server
    """
    # export(export_link, root, recursion_way)
    # for dirpath, dirnames, filenames in os.walk('/path_to_data'):
    #     # перебрать каталоги
    #     for dirname in dirnames:
    #         if dirname.endswith("-"):
    #             print(os.path.join(dirpath, dirname))

    """
    
    """
    pass
