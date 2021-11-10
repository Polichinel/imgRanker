import pickle
# from functions import * # import util functions
#
# cwd = os.getcwd()
# indx_list = getIndexList(cwd)


indx_list = pickle.load( open( "indx_list.pkl", "rb" ) )
att_dict = pickle.load( open( "att_dict.pkl", "rb" ) )


print(att_dict)
print('list')
print(indx_list)
print('dict')
print(att_dict['indx'])

print(len(indx_list))
