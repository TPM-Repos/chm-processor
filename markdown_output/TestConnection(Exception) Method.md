![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TestConnection(Exception) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1672.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [IAutopilotService Interface](topic1654.md) > [TestConnection Method](topic1670.md) : TestConnection(Exception) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_exception_
    The exception that was thrown when attempting to connect to Pro Server.

Glossary Item Box

Tests the connection to the group currently in use by the [IAutopilotService](topic1654.md). 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Overloads Function TestConnection( _
       ByRef _exception_ As Exception _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IAutopilotService](topic1654.md)
    Dim exception As Exception
    Dim value As Boolean
     
    value = instance.TestConnection(exception)  
  
C#|   
---|---  
      
    
    bool TestConnection( 
       ref Exception _exception_
    )  
  
#### Parameters

 _exception_
    The exception that was thrown when attempting to connect to Pro Server.

#### Return Value

True if the connection was successful, otherwise False.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IAutopilotService Interface](topic1654.md)   
[IAutopilotService Members](topic1655.md)   
[Overload List](topic1670.md)

©2024 DriveWorks Ltd. All Rights Reserved.
