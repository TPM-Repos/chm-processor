       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TestConnection() Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1671.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [IAutopilotService Interface](topic1654.md) > [TestConnection Method](topic1670.md) : TestConnection() Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Tests the connection to the group currently in use by the [IAutopilotService](topic1654.md). 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Overloads Function TestConnection() As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IAutopilotService](topic1654.md)
    Dim value As Boolean
     
    value = instance.TestConnection()  
  
C#|   
---|---  
      
    
    bool TestConnection()  
  
#### Return Value

True if the connection was successful, otherwise False.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IAutopilotService Interface](topic1654.md)   
[IAutopilotService Members](topic1655.md)   
[Overload List](topic1670.md)

©2024 DriveWorks Ltd. All Rights Reserved.
