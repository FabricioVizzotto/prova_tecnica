from controller import file_finder, analyse_data

if __name__=='__main__':
    try:
        analyse_data(file_finder())
    except BaseException:
        import sys
        print(sys.exc_info()[0])
        import traceback
        print(traceback.format_exc())
        print("Press Enter to continue ...")
        input()
