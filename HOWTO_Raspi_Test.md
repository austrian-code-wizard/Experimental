## **Instructions for running the rolling test of the mini tumbleweed**

##### **Prerequesites** ####
1. Download & Unzip AngryIPScanner (https://angryip.org/download/#mac)
2. Download & Install Cyberduck (https://cyberduck.io/download/)
3. Clone the Experimental repository from github. To do this, open the Mac Terminal and run:<br/>
`git clone https://github.com/austrian-code-wizard/Experimental.git`

##### **Before the test** ####
(This assumes that the personal hotspot of the mobile phone used is already saved on the Raspberry Pi, so that it will connect automatically)
<br/>
1. Open System Preferences and select the option "Sharing". On the left, there is a list with sharing options. Activate "File sharing", "Remote Login", and "Remote Management".
Then select "Remote Login". On the right, your Hostname and IP address will show up (the name before the @ and the
number after the @). Note these down.
2. Power up the Rapsberry Pi by connecting it to a Power source. Wait for a minute until
it is finished booting. It should now be logged into your Hotspot.
2. Open AngryIPScanner.app. For the "IP Range", enter your IP, except that you replace the number after the last "." with a ".1" for the lower bound and a ".255" for the upper bound.
Now start the IP test and wait until it is complete. If only you and the Raspi are connected
to the network, it should find three hosts. The Raspis IP address is the one that does not 
end with ".1" and has no "Mac-Book..." in their host name (usually its host
name is [n/a]). Note this IP address.
3. Open Terminal and type: <br/>
`ssh pi@<enter the Pi's IP address> ` <br/>
You will then be asked for a password. Enter `"TWdev0x%"`
4. Then you will be connected to the Raspberry Pi. Next, type:<br/>
`cd tw3.0/Tests/Other`. Now you are ready to run the tests. IMPORTANT:
Make sure that the Pi and Mac will not be disconnected from the Hotspot from now on.

#### **Running the Tests** ####
1. Now, in order to start a test enter the following command:<br/>
`sudo ./run_raspi_test.sh <test duration in seconds> <name of the test> <camera trigger intervals in seconds>`
2. If the test is running correctly, you should see a steady stream of terminal output. Now, wait until the test is over.

#### **Analyzing Results** ####
1. In order to analyze the results, open Cyberduck.
2. Cick on the "+" button to create a new connection. For the connection config,
select "SFTP". "Server: " is the Pi's IP, "Username: " is "Pi", and "Password:" is 
"TWdev0x%". Then click on "Connect".
3. You will now see the Pi's file system. Open the "tumbleweed_data" folder and then
open the Folder that is named after the test name you entered before. Right-click on the "processed_data.csv" file and select "Download".
4. Open a second Terminal
5. To navigate to the git repository you cloned before, enter:<br/>
`cd Experimental`
6. To activate Python, type:<br/>
`. venv/bin/activate`
7. To Download the necessary dependencies, type:<br/>
`sudo venv/bin/python3 -m pip install -r requirements.txt` <br/>
and wait until the download is complete.
8. To visualize the data, now type: <br/>
`sudo 3D_Vector_Time_Series.py "/Users/<your hostname>/Downloads/processed_data.csv"`<br/>
When you run a second test and you attempt to download the data, Cyberduck will ask you to 
rename the new file because there's already an exisiting file with that name. You should do that,
but then remember to change the file name in this command as well to read
the right file.

#### **Finishing Up** ####
1. When you are done, power down the Pi (in the terminal connected to the pi)
type: <br/>
`sudo shutdown now` <br/>
If you are asked for a password, enter "TWdev0x%"
