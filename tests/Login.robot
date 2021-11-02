*Settings*
Documentation       Authorization test suite

Resource            ${EXECDIR}/resources/Base.robot

Test Setup          Start Session
Test Teardown       Finish Session

*Test Cases*
User Login

    ${user}         Factory User Login

    Go To Login Page
    Fill Credentials        ${user}
    Submit Credentials
    User Should Be Logged In        ${user}

Incorrect Pass
    [Tags]      i_pass

    ${user}     Create Dictionary   email=rafael@msn.com     password=abc123

    Go To Login Page
    Fill Credentials   ${user}
    Submit Credentials
    Modal Content Should Be  Usuário e/ou senha inválidos.

User Not Found
    [Tags]      user_404

    ${user}     Create Dictionary   email=rafael@404.net     password=pwd123

    Go To Login Page
    Fill Credentials   ${user}
    Submit Credentials
    Modal Content Should Be  Usuário e/ou senha inválidos.

Incorrect Email
    [Tags]      i_email

    ${user}     Create Dictionary   email=rafael.com.br     password=pwd123

    Go To Login Page
    Fill Credentials   ${user}
    Submit Credentials
    Should Be Type Email