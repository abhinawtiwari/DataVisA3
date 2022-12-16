- Clone the project from github repo using below command: 
git clone https://github.com/abhinawtiwari/DataVisA3
- change directory to DataVisA3 folder 
cd DataVisA3
- checkout from master branch
git checkout -b master --track remotes/origin/master

- install nodejs from https://nodejs.org/en/ if not installed already.
- Check the installation of node.js using "node -v" command on terminal. If running this command gives this error, "node: The term 'node' is not recognized...", then node is not installed. Proceed to node installation from https://nodejs.org/en/ . Download the installer and press next next for default settings. After finishing the installation, proceed to next steps.

If node is installed, running the command "node -v" will give the version of the node installed. e.g., v18.12.1

- Run "npm i" to install node modules required for the project
- install http-server npm library using below command
    npm install -g http-server
- run the following command:
    http-server
- you should see the "Available on" message which shows the IP addresses on which the application is live. e.g., http://192.168.129.1:8080
- go to the IP address on your browser by appending "/globe" to the above IP. For example, if the IP was http://192.168.129.1:8080, go to http://192.168.129.1:8080/globe

- hover over on one of the categories on the top left of the screen to see the globe in action.
- hover over other categories to see other globe visualizations.