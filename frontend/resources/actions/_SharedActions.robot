*Settings*
Documentation       Shared actions

*Keywords*

Modal Content Should Be
    [Arguments]         ${expected_text}

    ${title}        Set Variable        css=.swal2-title
    ${content}      Set Variable        css=.swal2-html-container

    Wait For Elements State     ${title}         visible     5
    Get Text                    ${title}         equal       Oops...

    Wait For Elements State     ${content}       visible     5
    Get Text                    ${content}       equal       ${expected_text}

Alert Span Should Be
    [Arguments]     ${expected_notice}

    Wait For Elements State     css=span[class=error] >> text=${expected_notice}
    ...                         visible     5

Alert Spans Should Be 
    [Arguments]     ${expected_alersts}

    @{got_alerts}   Create List      

    ${spans}        Get Elements    xpath=//span[@class="error"]

    FOR     ${span}     IN      @{spans}

    ${text}             Get text            ${span}
    Append To List      ${got_alerts}       ${text}

    END

    Lists Should Be Equal       ${expected_alersts}     ${got_alerts} 