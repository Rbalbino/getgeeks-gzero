*Settings*
Documentation           BeGeek test suit

Resource        ${EXECDIR}/resources/Base.robot

Test Setup          Start Session
Test Teardown       Finish Session

*Test Cases*
Be a Geek

    ${user}     Factory User        be_geek
    Do Login    ${user}

    Go to Geek Form
    Fill Geek Form   ${user}[geek_profile]
    Submit Geek Form
    Geek Form Should Be Success


Field alerts
   [TAGS]          F_Alert
   [Template]      Signup Field Alerts

   whatsapp         ${EMPTY}        O Whatsapp deve ter 11 digitos contando com o DDD 
   whatsapp         11              O Whatsapp deve ter 11 digitos contando com o DDD
   whatsapp         119876543219    O Whatsapp deve ter 11 digitos contando com o DDD
   desc             ${EMPTY}        Informe a descrição do seu trabalho
   cost             ${EMPTY}        Valor hora deve ser numérico
   cost             1p2             Valor hora deve ser numérico
   cost             abcd            Valor hora deve ser numérico
   cost             1*9             Valor hora deve ser numérico


*Keywords*
Signup Field Alerts

    [Arguments]     ${field}    ${validation}    ${span}

    ${user}     Factory User        field_alert
    Do Login    ${user}

   Go to Geek Form
   Fill Text            id=${field}     ${validation} 
   Submit Geek Form
   Alert Span Should Be     ${span}
   Back to Page
   Exit Page