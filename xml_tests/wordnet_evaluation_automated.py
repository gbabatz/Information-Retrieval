# place this file inside trec_eval folder
import os


def run_eval(query_num):
    base_path = '/home/gbabatz/workspace/IR/IR-2019-2020-Project-1/'
    qrels_path = base_path + 'qrels.301-450.trec.adhoc'
    basic_file_names = ['titles_wordnet', 'titles_desc_wordnet', 'titles_desc_narr_wordnet']
    query_results_path = base_path + 'results/wordnet_enhanced/' + 'results_' + basic_file_names[query_num] + '.txt'
    save_results_path = base_path + 'results/wordnet_enhanced/' + 'eval_' + basic_file_names[query_num] + '.txt'

    command = './trec_eval ' + qrels_path + ' ' + query_results_path + ' > ' + save_results_path
    os.system(command)


def main():
    for qnum in [0, 1, 2]:
        run_eval(qnum)


main()
