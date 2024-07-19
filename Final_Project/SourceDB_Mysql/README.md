MySQL Source Database Files
sourcedb contains scripts to compile Java source files, build Docker images, and run them to have the Gilhari instance listen at localhost:8082. The structure and execution are similar to examples/gilhari_simple_example shipped with the Gilhari SDK. Refer to the example for a better understanding.

In sourcedb/src/com/project6/gilhari, create Java class files as needed to define your JDX_JSONObject (derived from Software Tree's JDX). For example, create files like Student.java, Teacher.java, Course.java, and Allotted.java according to your project requirements. These files are generated using reveng/JDXReverseEngineer.

The compile.cmd script compiles all the added Java files in the above directory. Ensure that you include the correct references and names in sources.txt as needed. To run this application standalone, add necessary .jar files (e.g., jdx-json package and jxclasses.jar) to the lib/ directory, which can be found in the Gilhari SDK installation.

The classname mapping file and .jdx file, as mentioned in gilhari5_source_mysql_local.config, can be found in sourcedb/config. Edit attributes and relations in the ORM specification file as required. Also, ensure that the JDBC driver for your database is included in the same ./config directory.

Create a Dockerfile as shown and run build.cmd to build the Docker image. Then use run_docker_app.cmd to run the image.

For initial testing purposes, run curl commands using curlPopulate.cmd and curlStreamData.cmd. Open a new terminal window, navigate to the directory, and run the command files. Check the terminal window where Gilhari is running for confirmation that it is listening on port 8082.

Postman can also be used to perform REST API calls. Refer to the Gilhari API manual shipped with the SDK for more details.

