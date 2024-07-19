REM A script to insert 60 Allotted JSON objects into a running container image 
REM of the app-specific Gilhari microservice gilhari5_source_mysql_local:3.0.
REM
REM The responses are recorded in a log file (curl_allotted.log).
REM
REM This script assumes the default port number is 80, but you can 
REM specify a different port number as the first command line argument.
REM Example: curlCommands 8899

IF %1.==. GOTO DefaultPort
SET port=%1
GOTO Proceed

:DefaultPort
SET port=80
GOTO Proceed

:Proceed

echo ** BEGIN OUTPUT ** > curl_allotted.log
echo. >> curl_allotted.log

echo Using PORT number %port% >> curl_allotted.log
echo. >> curl_allotted.log

FOR /L %%i IN (1,1,60) DO (
    SET /A rollNumber=%%i
    SET /A teacherId=((%%i MOD 10) + 1)
    SET /A courseId=((%%i MOD 30) + 1)

    REM Add the curl command to the log file and execute it
    echo ** Inserting Allotted %%i ** >> curl_allotted.log
    curl -X POST "http://localhost:%port%/gilhari/v1/Allotted" -H "Content-Type: application/json" -d "{\"entity\":{\"rollNumber\": \"ROLL%%i\", \"teacherId\": %%teacherId%%, \"courseId\": %%courseId%%}}" >> curl_allotted.log
    echo. >> curl_allotted.log
)

echo **Completed inserting Allotted records** >> curl_allotted.log
echo. >> curl_allotted.log

echo ** Query all Allotted objects ** >> curl_allotted.log
curl -X GET "http://localhost:%port%/gilhari/v1/Allotted" -H "Content-Type: application/json" >> curl_allotted.log
echo. >> curl_allotted.log
echo. >> curl_allotted.log

echo ** END OUTPUT ** >> curl_allotted.log
echo. >> curl_allotted.log

type curl_allotted.log
