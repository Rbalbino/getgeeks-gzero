*Settings*
Documentation       Base Test


Library         RequestsLibrary
Library         factories/Users.py

Resource        routes/SessionsRoute.robot
Resource        routes/UsersRoute.robot
Resource        routes/GeeksRoute.robot

Resource        helpers.robot

*Variables*
${API_USERS}        https://getgeeks-users-balbino.herokuapp.com
${API_GEEKS}        https://getgeeks-geeks-balbino.herokuapp.com