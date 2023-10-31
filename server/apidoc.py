apidoc = """API Documentation:

BASE URL: http://localhost/v2/dao


/{dacId}/custodians
Description: Also called the custodians endpoint. Get the current custodians for the planets naron with dacId naron, eyeke with dacId eyeke,
 veles with dacId veles, neri with dacId nerix, magor with dacId magor, kavian with dacId kavian
Parameters: 
dacId - string (path) *required - Filter the list by dacId - [Required] [length: 5-6 characters] - Example : nerix
Example: http://localhost/v2/dao/naron/custodians
Example: http://localhost/v2/dao/nerix/custodians

/dacs
Description: Provides information about DACs. Lists all available DACs along with their respective detailed information e.g. balance, statistics and globals.
Parameters: 
dacId - string (query) - Filter the list by dacId - [length: 5-6 characters] - Example : eyeke
limit - integer (query) - Maximum items to return. - [min: 1] - Example : 2
Example: http://localhost/v2/dao/dacs?dacId=eyeke&limit=2

/{dacId}/profile
Description: get user profile
Parameters: 
account - string (query) *required - Account(s) to fetch. It can accept multiple accounts separated by a comma. - [Required] [min length: 1] - Example : suzqu.wam,mgaqy.wam
dacId - string (path) *required - Filter the list by dacId - [Required] [length: 5-6 characters] - Example : nerix
Example: http://localhost/v2/dao/nerix/profile?account=suzqu.wam%2Cmgaqy.wam

/{dacId}/candidates
Description: Get candidates by planet
Parameters: 
dacId - string (path) *required - Filter the list by dacId - [Required] [length: 5-6 characters] - Example : nerix
Example: http://localhost/v2/dao/nerix/candidates

/candidates_voters_history
Description: Get a list of all the people that voted for a specified account on a specified dacId
Parameters: 
dacId - string (query) *required - Filter the list by dacId - [Required] [length: 5-6 characters] - Example : nerix
candidate - string (query) * required - Wallet Id of candidate or custodian - [Required] [min length: 1] - Example 51mqs.wam
skip - integer (query) - Number of items to skip - [min: 0] - Example: 0
limit - integer (query) - Maximum items to return. - [min: 1] - Example : 2
Example: http://localhost/v2/dao/candidates_voters_history?dacId=nerix&candidateId=t1dbe.wam&skip=0&limit=4


/voting_history
Description: Get the voter history for a specified account 
Parameters: 
dacId - string (query) *required - Filter the list by dacId - [Required] [length: 5-6 characters] - Example : nerix
voter - string (query) * required - Wallet Id of voter - [Required] [min length: 1] - Example .1uqy.wam
skip - integer (query) - Number of items to skip - [min: 0] - Example: 0
limit - integer (query) - Maximum items to return. - [min: 1] - Example : 2
Example: http://localhost/v2/dao/voting_history?dacId=nerix&voter=.1uqy.wam&skip=0&limit=100

/health
Description: Responds with server health status
Parameters: 
No parameters
Example: http://localhost/v2/dao/health

/ping
Description: Responds with server health status
Parameters: 
No parameters
Example: http://localhost/v2/dao/ping"""
