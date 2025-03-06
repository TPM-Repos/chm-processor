![](images/collapse.gif) ![](images/expand.gif) ![](images/copycode.gif) ![](images/copycodeHighlight.gif) ![](images/drpdown.gif) ![](images/drpdown_orange.gif)  
  
---  
DriveWorks SDK Documentation  |   
---|---  
Project Extenders   
[Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic9.md)  
  
Glossary Item Box

# Project Extenders

## Location

In order to create a Project Extender you simply need to create a .NET class library in a specific location.

If for example you have a project called Project1 in C:\DriveWorks\Project1\Project1.driveproj, then DriveWorks will look in the following locations (in order) for a project extender:

  1. C:\DriveWorks\Project1\Project1.dll
  2. C:\DriveWorks\Project1\bin\Project1.dll
  3. C:\DriveWorks\Project1\Project1\bin\Release\Project1.dll
  4. C:\DriveWorks\Project1\Project1\bin\Debug\Project1.dll



The last two locations are specifically included so that it is possible to create a Visual Studio project in the same directory as the DriveWorks project.

For example, if in Visual Studio a class library project is created in C:\DriveWorks\Project1, named Project1, _and the option to create a solution directory is turned off_ , then when the class is built, it will be built to:

> C:\DriveWorks\Project1\Project1\Release\Project1.dll

## Implementation

For DriveWorks to load the Project Extender, you need to have a single class in the Project Extender class library which inherits from [ProjectExtender Class](topic7232.md).

An example of a project extender is shown below:

Project Extender Example | ![](images/copycode.gif)Copy Code  
---|---  
      
    
    Imports DriveWorks
    Imports DriveWorks.Extensibility
    Public Class MyExtender
        Inherits ProjectExtender
        ' The UDF attribute lets DriveWorks know that this
        ' is a user defined function that can be called
        ' from a DriveWorks project (Excel projects do not support this feature).
        ' The valid types that can be taken/returned by a UDF are
        ' String
        ' Double
        ' DateTime
        ' Boolean
        ' Object - the value passed to an object typed parameter will always be
        ' one of the above, and the value returned by an object typed
        ' method must always be one of the above.
        <Udf()> _
        Public Function MyUdf(ByVal value1 As Double, ByVal value2 As Double) As Double
            Return value1 * value2
        End Function
        ' The macro attribute lets DriveWorks
        ' know that this is a macro that can
        ' be called from a macro button or by using
        ' the RunDesignMasterMacro specification flow
        ' task
        <Macro()> _
        Public Sub MyMacro()
            ' You can work with the project in this macro
            ' by accessing Me.Project
        End Sub
    End Class
      
  

