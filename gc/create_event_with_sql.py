from datetime import datetime, timedelta
from cal_setup import calendar_service
from sqlquery import sql_data




def main():
   # creates one hour event tomorrow 10 AM IST
   service = calendar_service()
   results = sql_data()

   #reads last pushed event id
   with open('lastpushedevent.txt') as f:
    lastpushedid = f.read()

  #  print(type(int(lastpushedid)))


   for row in results:
        id = row[0]
        eventtype = row[1]
        customer = row[2]
        envtype = row[3]
        startdate = row[4]
        enddate = row[5]
        eventname = row[6]
        eventstarttime = row[7]
        eventendtime = row[8]
        eventsetuptime = row[9]
        eventdescription = row[10]
        inflatablesneeded = row[11]
        employeesneeded = row[12]
        location = row[13]

    

   if int(lastpushedid) < id:
      #date time formats for start and end date
      start1 = startdate.strftime("%Y-%m-%d") + 'T' + eventstarttime + ':00-05:00' 
      end1 = enddate.strftime("%Y-%m-%d") + 'T' + eventendtime + ':00-05:00' 

      #Description = EnviromentType + Setup + EventDescription + InflatablesNeeded + EmployeesNeeded

      event_result = service.events().insert(calendarId='f7f91dc6d2f7ed0287d391dd0d1b031dd83d47ddb85ba24f48499def44740b01@group.calendar.google.com',
          body={       
              "summary": eventname,
              "description": Description(customer, eventtype, envtype ,eventsetuptime ,eventdescription ,str(inflatablesneeded) ,str(employeesneeded)),
              "location": location,
              "start": {"dateTime": start1},
              "end": {"dateTime": end1},
            }
            ).execute()

      #print("created event")
      #print("id: ", event_result['id'])
      #print("summary: ", event_result['summary'])
      #print("description: ", event_result['description'])
      #print("starts at: ", event_result['start']['dateTime'])
      #print("ends at: ", event_result['end']['dateTime'])
      
      #writes newest id to file
      with open('lastpushedevent.txt', 'w') as w:
       w.write('%d' % id)
    

    


def Description (customer, eventtype, EnviromentType ,Setup ,EventDescription ,InflatablesNeeded ,EmployeesNeeded):  
    
    strDescription = "Customer Name: " + customer + "<br/>" + "Event Type: " + eventtype + "<br/>" + "Enviroment Type: " + EnviromentType + "<br/>" + "SetupTime: " + Setup + "<br/>" + "Event Description: " + EventDescription + "<br/>" + "Inflatables Needed: " +InflatablesNeeded + "<br/>" + "Employees Needed: " + EmployeesNeeded
    return strDescription



if __name__ == '__main__':
   main()  
   