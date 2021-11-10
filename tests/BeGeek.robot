*Settings*
Documentation           BeGeek test suit

Resource        ${EXECDIR}/resources/Base.robot

Test Setup          Start Session
Test Teardown       Finish Session

*Test Cases*
Be a Geek

    ${user}     Factory User Be Geek
    Do Login    ${user}

    Go to Geek From
    Fill Geek Form   ${user}[geek_profile]
    Submit Geek Form
    Geek Form Should Be Success
