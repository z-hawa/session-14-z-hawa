# Session 14 Context Managers

# Iterating over the file contents
This was done by simply using a function that yielded the file's contents. However, since the field's needed to be converted into their respective data type, there was more required. A for loop was initialised in which the changes would be made to the data. The data would already be in a list of columns and then this data would be sent into a namedtuple we would have initialised earlier with the first row.

# Combining all iterators into one single iterator
This was done by using a function to convert the namedtuples into a dictionary. These dictionaries would have `ssn` removed from them. A final dictionary would be made where all the temp dictionaries would get added into. The ssn field was added by not removing the `ssn` key from the first dictionary added. This dictionary would then be used to initialise a namedtuple used to store the data.

# Removing stale records
This was done by simply creating a datetime object of the minimum date and converting the last_updated into a datetime object. These two datetime objects were compared accordingly in a filter function's key.

# Largest car makes per gender
This was done by generating a dictionary of all carmakers using the dict.get() method. Count was incremented and then the car maker(key) field was updated with it. At the end, the largest car maker was found using a max() and count of the highest value. If the count of the highest value was more than twice, then the carmaker who tied was found and appended to a list.