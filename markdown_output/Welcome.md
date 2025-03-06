![](images/collapse.gif) ![](images/expand.gif) ![](images/copycode.gif) ![](images/copycodeHighlight.gif) ![](images/drpdown.gif) ![](images/drpdown_orange.gif)  
  
---  
DriveWorks SDK Documentation  |   
---|---  
Welcome   
[Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic8.md)  
  
Glossary Item Box

# Welcome

Welcome to the DriveWorks Software Development Kit. This help and associated samples cover the API for DriveWorks Administrator, DriveWorks User, DriveWorks Autopilot, and DriveWorks Live.

Please also check out our [GitHub](https://github.com/DriveWorks) page! It has lots more examples of using the DriveWorks API.

# Important Notices

Please make sure to review these important notices before making use of the DriveWorks SDK.

## Deprecation / Removal of APIs

DriveWorks takes its obligation to provide a high-quality and stable API very seriously, however, under very rare circumstances, we may find it necessary to change our API surface. In these very rare cases, we will notify our intention to do so in this notices section to provide the opportunity for feedback and changes.

API | Location | Action | When | Explanation  
---|---|---|---|---  
AutopilotEmailNotificationSettings | [DriveWorks.Engine Assembly](topic2156.md) | Remove | DriveWorks 20 SP1 | This API was inadvertently made public in DriveWorks 20 SP0, and has been completely removed in DriveWorks 20 SP1.  
DriveWorks.Internal Namespaces | [DriveWorks.Engine Assembly](topic2156.md) | Deprecate | DriveWorks 20 SP1 |  Some namespaces were inadvertently made publicly available prior to DriveWorks 20, all starting with DriveWorks.Internal in the [DriveWorks Engine](topic2156.md). These namespaces were not intended to be publicly available. Starting in DriveWorks 20 SP0, these were hidden from the generated documentation, and as of DriveWorks 20 SP1 they have been hidden from the .NET Object Browser in Visual Studio. These APIs may be completely removed from a future version of DriveWorks.  
[DriveWorksCredentials.CreateFromHash](topic10678.md) | [DriveWorks.Engine Assembly](topic2156.md) | Deprecate | DriveWorks 21 SP0 | This API constructs a credentials object from an MD5 hash, which will no longer be supported as it is not secure and prevents the adoption of a more secure design. In DriveWorks 21 SP0, this method will throw an exception.  
  
# Introduction to Extensibility

There are two main types of extensibility in DriveWorks - you can use the table below to help work out which is appropriate for you: 

What do you want to do? | What DriveWorks extensibility concepts apply? | What else is there to know?  
---|---|---  
**Create a Macro** , e.g. to load some data from a text file into a running specification | [Project Extender](topic9.md) |  It's also worth looking into [Specification Macros](http://docs.driveworkspro.com/ProjectEditorSpecificationMacros.md) in the DriveWorks Help file, these often mean that you don't need to create an actual macro in code. You can also increase the capabilities available to Specification Macros by creating a Specification Flow Task in an [Extension Library](topic4.md).  
**Create a User Defined Function** to supplement the functions such as Sum, VLookup, and so on that are built-in to DriveWorks | [Project Extender](topic9.md) |   
**Create a Specification Flow Task** , to add additional capabilities to the Specification Flow/Specification Task toolbox | [Extension Library](topic4.md) |   
**Create a custom Document** , to supplement the documents that are already built in to DriveWorks | [Extension Library](topic4.md) |   
**Create a custom Table** , to supplement the documents that are already built in to DriveWorks | [Extension Library](topic4.md) |   
**Create a plugin to listen for model generation events** , to interact with the model generation process, e.g. to implement a PDM plugin, or do some sort of post processing | [Extension Library](topic4.md) | It's also possible to create SolidWorks macros which are called by DriveWorks during generation at certain points during the model generation process, for more information about these, see the [DriveWorks Help file](http://docs.driveworkspro.com/HowToCreateAMacroToRunOnASolidWorksFile.md).  
**Create a plugin to listen for specification events** , to interact with the specification process, e.g. to implement a PDM plugin, or do things at certain events during a specification | [Extension Library](topic4.md) | It's also possible to create SolidWorks macros which are called by DriveWorks during generation at certain points during the model generation process, for more information about these, see the [DriveWorks Help file](http://docs.driveworkspro.com/HowToCreateAMacroToRunOnASolidWorksFile.md).  
**Something else...** | [Extension Library](topic4.md) | If you're doing anything that isn't a macro or function, you probably want an extension library, if you have any questions, you can contact our API support address at [apisupport@driveworks.co.uk](mailto:apisupport@driveworks.co.uk) \- please note that although we try to respond as quickly as we can, API support can necessarily be more complex than regular support and so it may take a while to respond.  
  
©2024 DriveWorks Ltd. All Rights Reserved.
