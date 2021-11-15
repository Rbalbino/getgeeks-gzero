*Settings*
Documentation           BeGeek test suit

Resource        ${EXECDIR}/resources/Base.robot

Test Setup          Start Session
Test Teardown       Finish Session

*Test Cases*
Be a Geek

    ${user}     Factory User        be_geek
    Do Login    ${user}

    Go to Geek From
    Fill Geek Form   ${user}[geek_profile]
    Submit Geek Form
    Geek Form Should Be Success

Short Description

    ${user}     Factory User        short_desc
    Do Login    ${user}

    Go to Geek From
    Fill Geek Form   ${user}[geek_profile]
    Submit Geek Form
    Alert Span Should Be    A descrição deve ter no minimo 80 caracteres

Long Description

    ${user}     Factory User        long_desc
    Do Login    ${user}

   Go to Geek From
   Fill Geek Form   ${user}[geek_profile]
   Submit Geek Form
   Alert Span Should Be    A descrição deve ter no máximo 255 caracteres


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

   Go to Geek From
   Fill Text            id=${field}     ${validation} 
   Submit Geek Form
   Alert Span Should Be     ${span}
   Back to Page
   Exit Page