## Feature branch for Payment python class

This class is currently incomplete, as payment services integration is not in the project scope of this sprint.
Current class structure and unit test coverage is expected to be iterated upon down the line as payment services enter the project scope.
The final version of the class will likely have the following functionality:
1. Payment object attributes directly correspond to the MySQL data model so BE to DB communication is easy
2. Use of a .env file to hold login credentials for the MySQL database, so methods in this class can read/write/query the database
3. Integration with a payment services API of our choosing, making the required API calls and storing the right information to keep a historyof payments made 

**Payment Class & app.py for Order Page**

This feature branch carries an incomplete payment class, which will be iterated on and fleshed out once a payment service has entered the project scope.
This branch also carries a flask application that is to be merged/ consolidated with other branch flask apps to construct our WeGo web app.
The current files located in this branch do not constitute all dependencies/ references needed for the app.py to work.

---

**External Dependencies**

Below is a list of the files used in imports or referenced in render_template calls not included in this branch

1. The Order class (located in the branch feature/order_class), app needs an order object to pass data from the FE form into
2. MapServices, specifically the file mapquest.py (located in the MapServices_VSIM repo, under the dev branch), this is needed for converting addresses taken from the FE form into geocodes that the Order class stores
3. Template for the Order page labsampleorder.html (located in the FE_Demand repo under the lab_Sample_Delivery branch), which carries the form the app uses data from
4. Static CSS references for the pages referenced under templates (also found in feature/lab_Sample_Delivery branch of FE_Demand repo)

---

**Acknowledgements & Future**

This section holds project details and general steps for the further development of this branch

1. Map Services is intended to interact with the Supply cloud, but is required for returning geocodes: further iteration of System Architecture is needed to reflect this dependency, or the app.py of this branch needs to be reworked
2. Other BE dependencies of this repo branch can be resolved by merging the feature branches of the other classes into dev, where finalized versions will be pushed to main: branch merging and consolidation of flask apps for organized push required
3. Outside dependencies of this repo branch are to be addressed on demand-side system organization, as is assumed to be true of other repo file needs: server-side tests and comprehensive file interaction analysis required

---

## Usage and Scope To Be Added Once Payment Services Integration Begins