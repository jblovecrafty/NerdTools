#this is a set of form utilites for wtf forms
#

#simple method for getting a list of just the form data
#
def getListOfFormData(passedWTFFormObs):
	listOfFormData = []	
	
	for field in passedWTFFormObs:
		if(field.data and field.widget.input_type != 'hidden' ):
			listOfFormData.append(field.data)
			
	return listOfFormData