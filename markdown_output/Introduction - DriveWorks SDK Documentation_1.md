![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

DriveWorks SDK Documentation  |   
---|---  
Introduction   
[Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13.md)  
  
Glossary Item Box

The DriveWorks Applications extensibility library is required for Extension Libraries that expose Application Plugins. It provides access to all application-level extensibility features for example:

  * [ISpecificationService Interface](topic489.md)



In addition, the DriveWorks Applications extensibility library provides access to application-specific extensibility features, i.e. for DriveWorks Administrator and DriveWorks Autopilot. For example:

  * [Designers for document extensions](topic1517.md) to enable people to add them to their projects and administer them.
  * [Designers for table extensions](topic1434.md) to enable people to add them to their projects and administer them.
  * [Connectors](topic1697.md) which can connect to databases and other sources of data, and feed them to DriveWorks Autopilot to create specifications.
  * [Translators](topic1801.md) which are used by some connectors which know how to retrieve data but don't know how to turn it in to a specification. For example a file connector might know when a file is created, but not understand the contents of the file - in this case it could ask DriveWorks Autopilot to interrogate the available translators to see if any of them understand the contents of the file.



©2024 DriveWorks Ltd. All Rights Reserved.
