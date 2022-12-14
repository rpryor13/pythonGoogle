import pymssql
#print(pymssql.version)

# Database credentials and variables
server = 'db1.cuphpje8f5yu.us-east-1.rds.amazonaws.com'
user = 'admin'
password = 'CPDM2022'
database = 'dbJHMS'

def sql_data():
    # Connect to SQL database
    database_connection = pymssql.connect(server, user, password, database)


    cursor = database_connection.cursor()
    #sql = "SELECT TOP 1 TE.intEventID, TE.strEventType, TC.strFirstName +  ' ' + TC.strLastName as Name, TET.strEnvironmentType, TE.dteEventStartDate, TE.dteEventEndDate, TE.strEventName, TE.strEventStartTime, TE.strEventendTime, TE.strEventSetupTime, TE.strEventDescription, TE.intInflatablesNeeded, TE.intEmployeesForTheEvent, TE.strLocation FROM TEvents as TE JOIN TCustomers as TC ON TE.intCustomerID = TC.intCustomerID JOIN TEnvironmentTypes as TET  ON TE.intEnvironmentTypeID = TET.intEnvironmentTypeID order by TE.intEventID DESC"
    sql = "SELECT TOP 1 TE.intEventID, TE.strEventType, TC.strFirstName +  ' ' + TC.strLastName as Name, TET.strEnvironmentType, TE.dteEventStartDate, TE.dteEventEndDate, TE.strEventName, TE.strEventStartTime, TE.strEventendTime, TE.strEventSetupTime, TE.strEventDescription, TE.intInflatablesNeeded, TE.intEmployeesForTheEvent, TE.strLocation FROM TEvents as TE JOIN TCustomers as TC ON TE.intCustomerID = TC.intCustomerID JOIN TEnvironmentTypes as TET  ON TE.intEnvironmentTypeID = TET.intEnvironmentTypeID order by TE.intEventID DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    #for row in results:
    #    print (row)


    return results