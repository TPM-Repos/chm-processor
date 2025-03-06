![](images/collapse.gif) ![](images/expand.gif) ![](images/copycode.gif) ![](images/copycodeHighlight.gif) ![](images/drpdown.gif) ![](images/drpdown_orange.gif)  
  
---  
DriveWorks SDK Documentation  |   
---|---  
Extension Library Creation   
[Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic7.md)  
  
Glossary Item Box

# Creating an Extension Library

The first step before creating an extension is to create and register an extension library.

The easist way to do this is to use the project template installed into Visual Studio by the DriveWorks SDK.

# Creating an Extension Library Manually

  1. Create a new Class Library project in either C# or Visual Basic by using Visual Studio
  2. [Add references](topic10.md) to required DLLs (DriveWorks.Engine.dll is the absolute minimum)
  3. Add one or more plugins by creating a class and implementing the [IApplicationPlugin Interface](topic2004.md).




